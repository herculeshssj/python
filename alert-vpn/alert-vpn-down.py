import requests, json
import os, sys
from datetime import datetime, timedelta
from discord_webhook import DiscordWebhook

"""
Alerta via Discord quando a conexão com o Raspberry PI caiu
"""

if __name__ == '__main__':
    print('Hello World')
    """
    # Conecta no MongoDB
    client = MongoClient(os.getenv('MONGO_URL'))

    #discord_url = ''
    discord_url = os.getenv('DISCORD_URL')

    # Seta a base de dados
    db = client.wekan

    # Seta as variáveis
    to_date = datetime.today()
    from_date = datetime.today() - timedelta(hours=24)

    # Consulta as raias em movimento
    raias_em_movimento = db.activities.aggregate([
            {
                "$lookup": {
                    "from": "swimlanes" ,
                    "localField": "swimlaneId",
                    "foreignField": "_id",
                    "as": "swimlane_table"
                }
            },
            {
                "$match": {
                    "swimlane_table.archived": False,
                    "userId": { 
                        "$in": ["Ka4PjcMopQ4E5mNWv"]
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
                "$lookup": {
                    "from": "cards",
                    "localField": "cardId",
                    "foreignField": "_id",
                    "as": "card_table"
                }
            },
            {
                "$match": {
                    "userId": {
                        "$in": ["Ka4PjcMopQ4E5mNWv"]
                    },
                    "swimlane_table.archived": False,
                    "board_table.archived": False,
                    "card_table.archived": False,
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

    # Busca os cartões não arquivados em todos os quadros
    cartoes_nao_arquivados = db.cards.find({
            "archived": False,
            "userId": {
                "$in": ["Ka4PjcMopQ4E5mNWv"]
            }
        })
    quant_cartoes_pendentes = 0
    for cartao in cartoes_nao_arquivados:
        quant_cartoes_pendentes += 1

    # Adiciona a quantidade de cartões pendentes na mensagem
    mensagem_discord = mensagem_discord + '\n' + 'Atualmente existem ' + str(quant_cartoes_pendentes) + ' cartões pendentes de resolução.'

    # Envia a mensagem de aviso
    if quant_registros != 0:
        print(mensagem_discord) # Impressão no console, para fins de debug.
        webhook = DiscordWebhook(url=discord_url, content=mensagem_discord)
        response = webhook.execute()
"""