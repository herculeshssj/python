from pymongo import MongoClient
from pprint import pprint
from datetime import date, datetime, timedelta
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
                    "createdAt" : {
                        "$lt": from_date
                    },
                    "swimlane_table.archived": False,
                    "board_table.archived": False,
                    "board_table.title": {
                        "$ne": "Templates"
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

    # Constrói a mensagem
    mensagem_discord = 'Nenhuma atividade foi detectadas nos seguintes quadros:\n'
    for atividade in inercia:
        mensagem_discord = mensagem_discord + '* ' + atividade['boardName'][0] + ' -> ' + atividade['_id'][0] + '\n'

    print(mensagem_discord)

    # Envia a mensagem de aviso
    webhook = DiscordWebhook(url=discord_url, content=mensagem_discord)
    response = webhook.execute()
