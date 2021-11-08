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
    #attachments = db.cfs.attachments.filerecord.find({})
    cardComments = db.card_comments.find({})
    # pprint(attachments)
    # Itera a coleção de cardComments para setar o quadro correto
    for cardComment in cardComments:
        # print(attachment, type(attachment))
        # print('Quadro: ', attachment['boardId'], ' Raia: ', attachment['swimlaneId'], ' Lista: ', attachment['listId'], ' Cartão: ', attachment['cardId'], 'Usuário: ', attachment['userId'])

        # Busca o cartão
        card = db.cards.find_one({"_id": cardComment['cardId']})
        # print(card['_id'])

        # Atualiza o comentário com o quadro atual do cartão
        result = db.card_comments.update_many({'cardId': card['_id']},{'$set': {
            'boardId': card['boardId']
        }})
        print('Matched: ', result.matched_count, ' Modified: ', result.modified_count)

        # Verifica se o comentário está presente na tabela de atividades
        """
        activities = db.activities.find({
            "activityType":"addComment",
            "cardId":card['_id']
        })

        print('Comments found: ', activities.)
        break;
        """
        numActivities = db.activities.count_documents({
            "activityType":"addComment",
            "commentId":cardComment['_id']
        })
        print('Card coment: ', cardComment['_id'], 'Comments found: ', numActivities, type(numActivities))

        if numActivities == 0:
            resultInsert = db.activities.insert_one({
                '_id': cardComment['_id'],
                'userId': card['userId'],
                'activityType': 'addComment',
                'boardId': card['boardId'],
                'cardId': card['_id'],
                'commentId': cardComment['_id'],
                'listId': card['listId'],
                'swimlaneId': card['swimlaneId'],
                'createdAt': cardComment['createdAt'],
                'modifiedAt': cardComment['modifiedAt']
            })
            # break;
        


