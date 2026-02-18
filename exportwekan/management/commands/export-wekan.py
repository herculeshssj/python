from pathlib import Path
import re
import socket
from urllib.parse import urljoin
from django.core.management.base import BaseCommand
from django.utils import timezone
from pymongo import MongoClient
import requests
import gridfs
from bson import ObjectId

"""
PROMPT: O objetivo deste comando é exportar as informações contidas nos cards do Wekan salvando em arquivos no formato Markdown (.md).

O comando fará a leitura da coleção 'cards' da base do Wekan, e para cada card encontrado irá criar um arquivo Markdown
com as seguintes informações:
- Título do card em H1 (caso não exista, usar o ID do card)
- Nome do usuário que criou o card (caso não exista, usar "Desconecido")
- Data de criação do card (caso não exista, usar "Data desconhecida")
- Quadro (board) ao qual o card pertence (caso não exista, usar "Quadro desconhecido")
- Raia (swimlane) do card (caso não exista, usar "Raia desconhecida")
- Lista (list) a qual o card pertence (caso não exista, usar "Lista desconhecida")
- Lista de etiquetas (tags) associadas ao card (caso não exista, usar "Sem etiquetas")
- Descrição do card (caso não exista, usar "Sem descrição")
- Lista de membros associados ao card, formatada como uma lista de nomes (caso não exista, usar "Sem membros")
- Lista de anexos do card, formatada como uma lista de arquivos com nome e link no formato `[[nome_do_arquivo.ext]]` (caso não exista, usar "Sem anexos")
- Checklist do card, formatado como uma lista de itens (caso não exista, usar "Sem checklist")
- Comentários do card, formatados como uma lista de comentários com o nome do autor e a data (caso não exista, usar "Sem comentários")

Após a exportação dos cards, o comando deve efetuar a exportação dos anexos associados aos cards, salvando-os em uma pasta específica. 
O nome do arquivo de cada anexo deve ser o mesmo do arquivo original, e o conteúdo deve ser o mesmo do arquivo original.

O comando aceitará como parâmetro o caminho do diretório onde os arquivos Markdown e os anexos serão salvos. Se o diretório não existir, o comando 
deve criá-lo automaticamente.

O comando deve mostrar mensagens de progresso durante a execução, indicando quantos cards foram processados e quantos arquivos foram exportados.

A versão do Wekan utilizada é a 7.93, usando o MongoDB 6.0.26. O comando deve ser compatível com esta versão e deve lidar com possíveis variações na estrutura dos dados dos cards,
garantindo que a exportação seja realizada de forma robusta e sem erros, mesmo que alguns campos estejam ausentes ou tenham formatos inesperados.
"""


def safe_get(obj, *keys, default=None):
    """Acessa de forma segura um caminho de chaves/atributos aninhados em dicionários/objetos.

    Exemplos:
    - safe_get(card, 'createdBy', 'username')
    - safe_get(activity, 'user', 'name', default='Anon')

    Retorna `default` se qualquer nível estiver faltando ou não puder ser acessado.
    """
    cur = obj
    for key in keys:
        if cur is None:
            return default
        try:
            if isinstance(cur, dict):
                cur = cur.get(key, default)
            else:
                # tentar acesso por atributo
                cur = getattr(cur, key, default)
        except Exception:
            return default
    return cur if cur is not None else default

class Command(BaseCommand):
    help = 'Exporta cards do Wekan para arquivos Markdown e baixa anexos.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--outdir', '-o',
            type=str,
            help='Diretório de saída para arquivos .md e anexos',
            default='wekan_export'
        )
        parser.add_argument(
            '--mongo-uri',
            type=str,
            help='URI de conexão MongoDB (ex: mongodb://user:pass@host:27017/dbname)'
        )
        parser.add_argument('--host', type=str, help='Mongo host', default='localhost')
        parser.add_argument('--port', type=int, help='Mongo port', default=27017)
        parser.add_argument('--db', type=str, help='Mongo database name', default='wekan')
        parser.add_argument('--limit', type=int, help='Limitar número de cards processados', default=0)

    def handle(self, *args, **options):
        outdir = Path(options['outdir'])
        mongo_uri = options.get('mongo_uri')
        host = options.get('host')
        port = options.get('port')
        db_name = options.get('db')
        limit = int(options.get('limit') or 0)

        if MongoClient is None:
            self.stderr.write('pymongo não está instalado. Instale com: pip install pymongo')
            return 1

        if requests is None:
            self.stderr.write('requests não está instalado. Instale com: pip install requests')
            return 1

        outdir.mkdir(parents=True, exist_ok=True)
        attachments_dir = outdir / 'attachments'
        attachments_dir.mkdir(exist_ok=True)

        # Conectar MongoDB
        try:
            if mongo_uri:
                client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
            else:
                client = MongoClient(host=host, port=port, serverSelectionTimeoutMS=5000)
            # Forçar seleção de servidor
            client.server_info()
        except Exception as e:
            self.stderr.write(f'Erro ao conectar ao MongoDB: {e}')
            return 1

        db = client[db_name]

        # Coleção padrão de cards no Wekan
        cards_col = db.get_collection('cards')

        query = {}
        cursor = cards_col.find(query)
        if limit > 0:
            cursor = cursor.limit(limit)

        total = cards_col.count_documents(query)
        processed = 0
        md_exported = 0
        attachments_downloaded = 0
        # registrar _id (ObjectId) de arquivos GridFS já exportados
        exported_gridfs_ids = set()

        self.stdout.write(f'Iniciando exportação de {total} cards (limit={limit})...')

        for card in cursor:
            processed += 1
            try:
                card_id = str(card.get('_id'))
                title = card.get('title') or card.get('titlePlain') or card_id
                created_by = safe_get(card, 'createdBy', 'username') or safe_get(card, 'createdBy', 'name') or 'Desconhecido'
                created_at = card.get('createdAt') or card.get('createdAt2') or card.get('createdAt', None)
                if hasattr(created_at, 'isoformat'):
                    created_at_str = created_at.isoformat()
                else:
                    created_at_str = str(created_at) if created_at else 'Data desconhecida'

                board_id = card.get('boardId') or card.get('board') or None
                board_name = 'Quadro desconhecido'
                if board_id:
                    board = db.get_collection('boards').find_one({'_id': board_id}) if isinstance(board_id, (str,)) else None
                    if not board:
                        try:
                            board = db.get_collection('boards').find_one({'_id': board_id})
                        except Exception:
                            board = None
                    if board:
                        board_name = board.get('title') or board.get('name') or board_name

                swimlane = card.get('swimlaneId') or card.get('swimlane') or None
                swimlane_name = 'Raia desconhecida'
                if swimlane:
                    lw = db.get_collection('swimlanes').find_one({'_id': swimlane})
                    if lw:
                        swimlane_name = lw.get('title') or lw.get('name') or swimlane_name

                list_id = card.get('listId') or card.get('list') or None
                list_name = 'Lista desconhecida'
                if list_id:
                    lst = db.get_collection('lists').find_one({'_id': list_id})
                    if lst:
                        list_name = lst.get('title') or lst.get('name') or list_name

                tags = card.get('labels') or card.get('tags') or []
                tags_line = ', '.join([t.get('name') if isinstance(t, dict) else str(t) for t in tags]) if tags else 'Sem etiquetas'

                description = card.get('description') or card.get('desc') or 'Sem descrição'

                members = []
                members_list = card.get('members') or []
                if members_list:
                    for m in members_list:
                        if isinstance(m, dict):
                            members.append(m.get('username') or m.get('name') or str(m.get('_id', '')))
                        else:
                            # buscar usuário na coleção users pelo _id
                            try:
                                u = db.get_collection('users').find_one({'_id': m})
                                if u:
                                    members.append(u.get('username') or u.get('name') or str(u.get('_id')))
                                else:
                                    members.append(str(m))
                            except Exception:
                                members.append(str(m))
                members_text = '\n'.join([f'- {n}' for n in members]) if members else 'Sem membros'

                # Attachments: Wekan normalmente guarda em collection 'attachments' e também no card.attachments
                attachments = []
                card_attachments = card.get('attachments') or []
                if card_attachments:
                    for att in card_attachments:
                        # preservar o documento completo para suportar GridFS metadata
                        if isinstance(att, dict):
                            attachments.append(att)
                        else:
                            attachments.append({'name': str(att), 'url': None})
                else:
                    # tentar buscar em collection attachments por cardId (pode estar em meta.cardId)
                    try:
                        cid = card.get('_id')
                        queries = [{'cardId': cid}, {'meta.cardId': cid}]
                        try:
                            cid_str = str(cid)
                        except Exception:
                            cid_str = None
                        if cid_str:
                            queries.extend([{'cardId': cid_str}, {'meta.cardId': cid_str}])

                        atts = db.get_collection('attachments').find({'$or': queries})
                        for att in atts:
                            # att já é o documento; preservar para extrair GridFS
                            attachments.append(att)
                    except Exception:
                        pass

                attachments_text = 'Sem anexos'
                if attachments:
                    lines = []
                    for a in attachments:
                        filename = a.get('name') or 'anexo'
                        lines.append(f'- [[{filename}]]')
                    attachments_text = '\n'.join(lines)

                # Checklist
                checklist_items = []
                checklists = card.get('checklists') or card.get('checklist') or []
                if isinstance(checklists, dict):
                    # possivelmente map de id->checklist
                    checklists = list(checklists.values())
                for cl in checklists:
                    if isinstance(cl, dict):
                        items = cl.get('items') or cl.get('checkItems') or []
                        for it in items:
                            if isinstance(it, dict):
                                text = it.get('text') or it.get('name') or str(it)
                            else:
                                text = str(it)
                            checklist_items.append(text)
                checklist_text = '\n'.join([f'- [ ] {i}' for i in checklist_items]) if checklist_items else 'Sem checklist'

                # Comments (card_comments)
                comments_text = 'Sem comentários'
                try:
                    card_comments = db.get_collection('card_comments').find({'cardId': card.get('_id')})
                except Exception:
                    card_comments = []
                comments = []
                for comment in card_comments:
                    text = comment.get('text')
                    user_id = comment.get('userId')
                    created = comment.get('createdAt')
                    
                    if text:
                        # Buscar informações do usuário pela userId
                        author = 'Autor desconhecido'
                        if user_id:
                            try:
                                user = db.get_collection('users').find_one({'_id': user_id})
                                if user:
                                    author = user.get('username') or user.get('name') or str(user_id)
                            except Exception:
                                author = str(user_id)
                        
                        if hasattr(created, 'isoformat'):
                            cstr = created.isoformat()
                        else:
                            cstr = str(created) if created else 'Data desconhecida'
                        comments.append(f'- {author} ({cstr}): {text}')
                if comments:
                    comments_text = '\n'.join(comments)

                # Montar conteúdo Markdown
                md_lines = []
                md_lines.append(f'# {title}')
                md_lines.append('')
                md_lines.append(f'- **Criado por:** {created_by}')
                md_lines.append(f'- **Criado em:** {created_at_str}')
                md_lines.append(f'- **Quadro:** {board_name}')
                md_lines.append(f'- **Raia:** {swimlane_name}')
                md_lines.append(f'- **Lista:** {list_name}')
                md_lines.append(f'- **Etiquetas:** {tags_line}')
                md_lines.append('')
                md_lines.append('## Descrição')
                md_lines.append('')
                md_lines.append(description or 'Sem descrição')
                md_lines.append('')
                md_lines.append('## Membros')
                md_lines.append('')
                md_lines.append(members_text)
                md_lines.append('')
                md_lines.append('## Anexos')
                md_lines.append('')
                md_lines.append(attachments_text)
                md_lines.append('')
                md_lines.append('## Checklist')
                md_lines.append('')
                md_lines.append(checklist_text)
                md_lines.append('')
                md_lines.append('## Comentários')
                md_lines.append('')
                md_lines.append(comments_text)

                safe_title = re.sub(r'[\\/:*?"<>|]+', '_', title)[:150]
                md_filename = outdir / f"{safe_title or card_id}.md"
                # Garantir único se houver duplicata
                counter = 1
                base_md = md_filename
                while md_filename.exists():
                    md_filename = outdir / f"{safe_title}_{counter}.md"
                    counter += 1

                with md_filename.open('w', encoding='utf-8') as f:
                    f.write('\n'.join(md_lines))
                md_exported += 1

                # Baixar anexos (se houver URLs acessíveis)
                for a in attachments:
                    # `a` pode ser o documento completo da collection attachments ou um dicionário vindo do card
                    url = a.get('url') if isinstance(a, dict) else None
                    name = a.get('name') or a.get('fileName') or 'anexo'
                    # tentar extrair de GridFS se o anexo estiver armazenado lá
                    gridfs_id = None
                    try:
                        versions = a.get('versions') if isinstance(a, dict) else None
                        if versions and isinstance(versions, dict):
                            # procurar em qualquer versão por meta.gridFsFileId
                            for v in versions.values():
                                if not isinstance(v, dict):
                                    continue
                                meta = v.get('meta') or {}
                                gf = meta.get('gridFsFileId') or meta.get('gridFsId')
                                if gf:
                                    gridfs_id = gf
                                    break
                        # também checar campos top-level que indiquem GridFS
                        if not gridfs_id:
                            storage = a.get('storage') if isinstance(a, dict) else None
                            if storage == 'gridfs':
                                gridfs_id = a.get('gridFsFileId') or a.get('gridFsId')
                    except Exception:
                        gridfs_id = None

                    safe_name = re.sub(r'[\\/:*?"<>|]+', '_', name)
                    attach_path = attachments_dir / safe_name

                    if gridfs_id:
                        try:
                            oid = ObjectId(gridfs_id) if isinstance(gridfs_id, (str,)) else gridfs_id
                            # Procurar em todas as collections que terminam com '.files' para achar o bucket correto
                            found = False
                            for coll in db.list_collection_names():
                                if not coll.endswith('.files'):
                                    continue
                                try:
                                    file_doc = db[coll].find_one({'_id': oid})
                                except Exception:
                                    file_doc = None
                                if file_doc:
                                    prefix = coll[:-6]
                                    fs = gridfs.GridFS(db, collection=prefix)
                                    gfile = fs.get(oid)
                                    with open(attach_path, 'wb') as af:
                                        while True:
                                            chunk = gfile.read(8192)
                                            if not chunk:
                                                break
                                            af.write(chunk)
                                    attachments_downloaded += 1
                                    try:
                                        exported_gridfs_ids.add(oid)
                                    except Exception:
                                        pass
                                    found = True
                                    break
                            if not found:
                                self.stderr.write(f'GridFS file id {gridfs_id} não encontrado em nenhum bucket (.files)')
                                # continuar para tentar fallback via URL
                            else:
                                continue
                        except Exception as e:
                            self.stderr.write(f'Falha ao extrair GridFS id {gridfs_id}: {e}')

                    # se não houver GridFS ou falhar, tentar via URL/HTTP
                    if not url:
                        continue
                    # nome seguro
                    safe_name = re.sub(r'[\\/:*?"<>|]+', '_', name)
                    attach_path = attachments_dir / safe_name
                    # se for um caminho relativo no servidor, tentar construir
                    try:
                        # suportar quando url é blob id que precisa busca na collection 'attachments'
                        if url.startswith('/'):
                            # se houver um campo 'serverUrl' no db, usar
                            server_url = db.get_collection('settings').find_one({'_id': 'public'})
                            server_base = safe_get(server_url, 'serverUrl') or ''
                            full_url = urljoin(server_base, url)
                        else:
                            full_url = url
                    except Exception:
                        full_url = url

                    try:
                        r = requests.get(full_url, stream=True, timeout=15)
                        if r.status_code == 200:
                            with open(attach_path, 'wb') as af:
                                for chunk in r.iter_content(chunk_size=8192):
                                    if chunk:
                                        af.write(chunk)
                            attachments_downloaded += 1
                    except (requests.exceptions.RequestException, socket.error):
                        # Ignorar falhas de download, apenas logar
                        self.stderr.write(f'Falha ao baixar anexo {full_url} para {attach_path}')

                self.stdout.write(f'[{processed}/{total}] Exportado card: {title}')

            except Exception as e:
                self.stderr.write(f'Erro ao processar card {card.get("_id")}: {e}')

        self.stdout.write('---')
        self.stdout.write(f'Cards processados: {processed}')
        self.stdout.write(f'Arquivos Markdown exportados: {md_exported}')
        self.stdout.write(f'Anexos baixados: {attachments_downloaded}')

        # Exportar buckets adicionais que podem existir como collections GridFS (.files)
        target_buckets = [
            'attachments',
            'cfs_gridfs._tempstore',
            'cfs_gridfs.attachments',
            'cfs_gridfs.avatars',
        ]

        self.stdout.write('Exportando conteúdos de buckets ausentes...')
        for prefix in target_buckets:
            matched = False
            for coll in db.list_collection_names():
                if not coll.endswith('.files'):
                    continue
                base_prefix = coll[:-6]
                # aceitar correspondência exata ou prefixo que contenha o nome pedido
                if base_prefix == prefix or base_prefix.startswith(prefix):
                    matched = True
                    bucket_dir = attachments_dir / base_prefix.replace('.', '_')
                    bucket_dir.mkdir(parents=True, exist_ok=True)
                    fs = gridfs.GridFS(db, collection=base_prefix)
                    try:
                        for file_doc in db[coll].find():
                            fid = file_doc.get('_id')
                            if fid in exported_gridfs_ids:
                                continue
                            fname = file_doc.get('filename') or str(fid)
                            safe_fname = re.sub(r'[\\/:*?"<>|]+', '_', fname)
                            out_path = bucket_dir / safe_fname
                            try:
                                gfile = fs.get(fid)
                                with open(out_path, 'wb') as of:
                                    while True:
                                        chunk = gfile.read(8192)
                                        if not chunk:
                                            break
                                        of.write(chunk)
                                attachments_downloaded += 1
                                try:
                                    exported_gridfs_ids.add(fid)
                                except Exception:
                                    pass
                            except Exception as e:
                                self.stderr.write(f'Falha ao exportar {fid} de {coll}: {e}')
                    except Exception as e:
                        self.stderr.write(f'Erro ao iterar collection {coll}: {e}')
            if not matched:
                self.stdout.write(f'Bucket não encontrado: {prefix}')

        self.stdout.write('---')
        self.stdout.write(f'Anexos totais baixados (incluindo buckets finais): {attachments_downloaded}')

        return 0

