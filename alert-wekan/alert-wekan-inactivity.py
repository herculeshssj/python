import requests, json
import sqlite3
from pymongo import MongoClient
from datetime import datetime, timedelta
from discord_webhook import DiscordWebhook

"""
Por hora só ficarei com o alerta de raias inativas.
Posteriormente verei os alertas para as pessoas que
estou devendo uma resposta.
"""

"""
def inicializa_base_sqlite():
    # Conecta na base SQlite
    conn = sqlite3.connect('filaespera.db')

    # Objeto cursor
    cursor = conn.cursor()

    # Cria a tabela caso não exista
    query = ""
        create table if not exists fila_espera (
            id text primary key not null,
            cliente text not null,
            pedido text not null
        )
    ""
    cursor.execute(query)

    # Commita as alterações e encerra a conexão
    conn.commit()
    conn.close()
"""

if __name__ == '__main__':
    # Conecta no MongoDB
    client = MongoClient('mongodb://root:root@localhost:27017')

    discord_url = ''

    # Seta a base de dados
    db = client.wekan

    # Seta as variáveis
    to_date = datetime.today()
    from_date = datetime.today() - timedelta(hours=72)

    # Consulta as raias em movimento
    raias_em_movimento = db.activities.aggregate([
            {
                "$match": {
                    "userId": { 
                        "$in": ["ng6ezgdC555We6fvr", "pk6eq8m7oqndKWdpe"]
                    },
                    "createdAt" : {
                        "$gte": from_date,
                        "$lt": to_date
                    }
                }
            },
            {
                "$project" : {
                    "swimlaneId": 1
                }
            },
            {
                "$group": {
                    "_id": "_id",
                    "activityId": {
                        "$addToSet": "$swimlaneId"
                    }
                }
            }
        ])
    
    raias_selecionadas = []
    for r in raias_em_movimento:
        raias_selecionadas = r['activityId']

    # Realiza a consulta
    inercia = db.activities.aggregate([
            {
                "$lookup": {
                    "from": "swimlanes" ,
                    "localField": "swimlaneId",
                    "foreignField": "_id",
                    "as": "swimlane_table"
                }
            },
            {
                "$lookup": {
                    "from": "boards",
                    "localField": "boardId",
                    "foreignField" : "_id",
                    "as": "board_table"
                }
            },
            {
                "$match": {
                    "userId": {
                        "$in": ["ng6ezgdC555We6fvr", "pk6eq8m7oqndKWdpe"]
                    },
                    "swimlane_table.archived": False,
                    "board_table.archived": False,
                    "board_table.title": {
                        "$ne": "Templates"
                    },
                    "swimlaneId" :{
                        "$nin": raias_selecionadas
                    } 
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "board_table.title": 1,
                    "swimlane_table.title": 1			
                }
            },
            {
                "$group": {
                    "_id": "$swimlane_table.title",
                    "boardName": { "$last": "$board_table.title"},
                    "quantidade": {
                        "$count": {}
                    }
                }
            },
            {
                "$sort": {
                    "quantidade": 1
                }
            }
        ])

    quant_registros = 0

    # Constrói a mensagem
    mensagem_discord = 'Nenhuma atividade foi detectada nos seguintes quadros:\n'
    for atividade in inercia:
        quant_registros += 1
        mensagem_discord = mensagem_discord + str(quant_registros) + '. ' + atividade['boardName'][0] + ' -> ' + atividade['_id'][0] + '\n'


    # Envia a mensagem de aviso
    if quant_registros != 0:
        print(mensagem_discord) # Impressão no console, para fins de debug.
        webhook = DiscordWebhook(url=discord_url, content=mensagem_discord)
        response = webhook.execute()
        

    """
    Fila de espera para atendimento
    ""

    # Inicializa a base SQlite
    inicializa_base_sqlite()

    # Declaração dos objetos da base
    conn = sqlite3.connect('filaespera.db')
    cursor = conn.cursor()

    limite_espera = datetime.today() - timedelta(hours=24)

    # Busca os solicitantes que estão na fila de espera
    fila_espera = db.cards.find(
            {
                "archived" : False,
                "requestedBy": {
                    "$not" : {
                        "$eq" : ""
                    }
                },
                "dateLastActivity": {
                    "$lt": limite_espera
                }
            },
            {
                "_id": 1,
                "title": 1,
                "requestedBy" : 1
            }
        )

    # Integração com o app Outsystems 'Fila do Pão' que informa as pessoas que preciso responder.
    url_api = 'https://personal-8gsrdrii.outsystemscloud.com/filadopaoapi/rest/v1/novo'

    # Itera a fila de espera para registrar no aplicativo
    for cliente in fila_espera:
        # Verifica se o cliente já entrou na fila de espera
        cursor = conn.execute("select * from fila_espera where id = '" + cliente['_id'] + "'")
        if not cursor.fetchall():
            # Cadastra o cliente na base
            queryInsert = ("insert into fila_espera (id, cliente, pedido) values (:ID, :CLIENTE, :PEDIDO);")
            paramsInsert = {
                'ID': cliente['_id'],
                'CLIENTE': cliente['requestedBy'],
                'PEDIDO': cliente['title']
            }
            conn.execute(queryInsert, paramsInsert)
            conn.commit()

            # Prepara a requisição
            data = {
                "Cliente": cliente['requestedBy'],
                "Pedido": cliente['title'],
                "PrazoAtendimentoId": 14
            }
            data_json = json.dumps(data)
            headers = {'Content-type': 'application/json'}

            # Registra o cliente na aplicação
            response = requests.post(url=url_api, data=data_json, headers=headers)

            print(response.json()) # impressão no console, para fins de debug'
            print('Cliente ' ,cliente['requestedBy'], ' incluído na fila de espera.')
        else:
            print('Cliente ' ,cliente['requestedBy'], ' está na fila de espera.')


    # Encerra a conexão com a base SQlite
    conn.close()

    """