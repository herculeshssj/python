from django.core.management.base import BaseCommand
from django.utils import timezone

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
        parser.add_argument('--host', type=str, help='Mongo host', default=DEFAULT_DB_HOST)
        parser.add_argument('--port', type=int, help='Mongo port', default=DEFAULT_DB_PORT)
        parser.add_argument('--db', type=str, help='Mongo database name', default=DEFAULT_DB_NAME)
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
                        name = att.get('name') or att.get('title') or att.get('originalName') or att.get('fileName') or att.get('url', '')
                        url = att.get('url') or att.get('link') or att.get('path') or None
                        attachments.append({'name': name, 'url': url})
                else:
                    # tentar buscar em collection attachments por cardId
                    try:
                        atts = db.get_collection('attachments').find({'cardId': card.get('_id')})
                        for att in atts:
                            attachments.append({'name': att.get('name') or att.get('fileName'), 'url': att.get('url') or att.get('link')})
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

                # Comments (activities/messages)
                comments_text = 'Sem comentários'
                try:
                    activities = db.get_collection('activities').find({'cardId': card.get('_id')})
                except Exception:
                    activities = []
                comments = []
                for act in activities:
                    # procurar por tipo de comentário
                    text = act.get('text') or act.get('message') or act.get('description')
                    author = safe_get(act, 'user', 'username') or safe_get(act, 'user', 'name') or act.get('userId') or 'Autor desconhecido'
                    created = act.get('createdAt') or act.get('date') or act.get('time')
                    if text:
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
                    url = a.get('url')
                    name = a.get('name') or 'anexo'
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

        return 0

