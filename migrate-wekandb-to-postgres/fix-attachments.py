from pymongo import MongoClient
from pprint import pprint

if __name__ == '__main__':
    # Conecta no MongoDB
    client = MongoClient('mongodb://root:root@vm-debian-11-docker:27017')
    # db = client.admin

    # serverStatusResult = db.command('serverStatus')
    # pprint(serverStatusResult)
    # Seta a base de dados
    db = client.wekan

    # card = db.cards.find_one({'_id':'MhtTWzwybrt4rKKyw'})
    # cards = db.cards.find({}).count()
    # pprint(cards)

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
        


