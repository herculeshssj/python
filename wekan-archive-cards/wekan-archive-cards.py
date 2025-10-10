import os
from pymongo import MongoClient
from datetime import datetime,timedelta

"""
Efetua o arquivamento dos cards com mais de 6 meses abertos do quadro 'UAb' todo sábado às 23:59.
A definição do horário é determinada pela hora que o script é executado pelo cron.
"""

if __name__ == '__main__':

    try:
    
        # Pega os dados de conexão da variável de ambiente
        connection_string = os.getenv('MONGODB_CONNECTION_STRING')

        # Pega o BoardId das variáveis de ambiente
        boardId = os.getenv('BOARDID')
        
        # Conecta no MongoDB
        client = MongoClient(connection_string)

        # Seta a base de dados
        db = client.wekan

        # Seta a data e hora atual
        data_atual = datetime.today()

        # Define a data limite para arquivamento (6 meses atrás)
        seis_meses_atras = datetime.today() - timedelta(days=6*30)

        # Executa o update na base
        db.cards.update_many(
            {
                "boardId": boardId,
                "archived": False,
                "createdAt": { "$lt": seis_meses_atras }
            },
            {
                "$set": {
                    "archived": True,
                    "archivedAt": data_atual,
                }
            }
        )

    
    except Exception as ex:
        print('Exception:')
        print(ex)
