import sys
import requests, json
from pymongo import MongoClient
from datetime import datetime, timedelta
from discord_webhook import DiscordWebhook

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
                    "boardName": { "$first": "$board_table.title"}
                }
            },
            {
                "$sort": {
                    "swimlane_table.title": 1
                }
            }
        ])

    quant_registros = 0

    # Constrói a mensagem
    mensagem_discord = 'Nenhuma atividade foi detectadas nos seguintes quadros:\n'
    for atividade in inercia:
        quant_registros += 1
        mensagem_discord = mensagem_discord + '* ' + atividade['boardName'][0] + ' -> ' + atividade['_id'][0] + '\n'

    # Impressão no console, para fins de debug.
    print(mensagem_discord)

    # Envia a mensagem de aviso
    if quant_registros == 0:
        sys.exit(0)
    else:
        webhook = DiscordWebhook(url=discord_url, content=mensagem_discord)
        response = webhook.execute()

    # Integração com o app Outsystems 'Fila do Pão' que informa as pessoas que preciso responder.
    url_api = 'https://personal-8gsrdrii.outsystemscloud.com/filadopaoapi/rest/v1/novo'

    data = {
        "Cliente": "Wekan",
        "Pedido": "Verificar os quadros e raias sem atividade no Wekan.",
        "PrazoAtendimentoId": 6
    }

    data_json = json.dumps(data)
    headers = {'Content-type': 'application/json'}
    response = requests.post(url=url_api, data=data_json, headers=headers)
    
    print(response.json()) # impressão no console, para fins de debug
