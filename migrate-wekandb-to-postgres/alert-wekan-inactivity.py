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
    from_date = datetime.today() - timedelta(hours=24)
    
    # Realiza a consulta na tabela de atividades
    inercia = db.activities.find({"userId": {"$in": ["ng6ezgdC555We6fvr","pk6eq8m7oqndKWdpe"]}, "createdAt": {"$gte":from_date, "$lt":to_date}})

    quant_registros = 0

    for atividade in inercia:
        quant_registros +=1

    if quant_registros == 0:
        print('Não houve atividade nas últimas 24 horas! Enviando notificação...')        

        webhook = DiscordWebhook(url=discord_url, content='Nenhuma atividade detectada no Wekan! Vá lá e atualize os quadros!!! >:(')
        response = webhook.execute()

    #for atividade in inercia:
    #    print(atividade)
    
    
    #print('from: ', from_date, ' to: ', to_date)

    #from datetime import datetime, timedelta
    #d = datetime.today() - timedelta(hours=24)
    #print(d)

    # Consulta a tabela de atividades para verificar se houve ou não atividade nas últimas 24 horas
    # inercia = db.activities.find()

    #from_date = datetime.datetime(2010, 12, 31, 12, 30, 30, 125000)
    #print(from_date)
#to_date = datetime.datetime(2011, 12, 31, 12, 30, 30, 125000)

#for post in posts.find({"date": {"$gte": from_date, "$lt": to_date}}):
#    print(post)


    # db = client.admin

    # serverStatusResult = db.command('serverStatus')
    # pprint(serverStatusResult)
    

    #card = db.cards.find_one({'_id':'3H9yyZ2An9JSDvr4w'})
    #cards = db.cards.find({}).count()
    #pprint(card)
"""
    # Busca todos os objetos da coleção
    attachments = db.cfs.attachments.filerecord.find({})
    # pprint(attachments)
    # Itera a coleção de attachments para setar o quadro, raia e lista corretos
    for attachment in attachments:
        # print(attachment, type(attachment))
        # print('Quadro: ', attachment['boardId'], ' Raia: ', attachment['swimlaneId'], ' Lista: ', attachment['listId'], ' Cartão: ', attachment['cardId'], 'Usuário: ', attachment['userId'])

        # Busca o cartão
        card = db.cards.find_one({"_id": attachment['cardId']})
        # print(card['_id'])

        # Atualiza o anexo com o quadro, lista e raia atual do cartão
        result = db.cfs.attachments.filerecord.update_many({'cardId': card['_id']},{'$set': {
            'boardId': card['boardId'],
            'swimlaneId': card['swimlaneId'],
            'listId': card['listId']
        }})
        print('Matched: ', result.matched_count, ' Modified: ', result.modified_count)
        
"""

