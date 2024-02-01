import os
import sqlite3
import uuid

from contextlib import closing
from datetime import datetime

def save_to_sqlite():
    with closing(sqlite3.connect("/data/logkeys.db")) as connection:
        with closing(connection.cursor()) as cursor:
            # Abre o arquivo enviado
            with open('/tmp/logkeys.log') as fp:
                print('Loading to database...', end=' ')
                linhas = fp.readlines()
                num_linhas = len(linhas)
                contador = 0
                porcentagem = 0
                for linha in linhas:
                    if ' > ' in linha:
                        id_registro = str(uuid.uuid4())

                        # Isolando o timestamp contido na linha
                        string_timestamp = linha.split(' ')[0]+' '+linha.split(' ')[1]
                        data_hora = string_timestamp.replace('-0300', '')

                        # Extraindo somente a data
                        data_extraida = datetime.strptime(data_hora, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')

                        # Extraindo somente a hora
                        hora_extraida = datetime.strptime(data_hora, '%Y-%m-%d %H:%M:%S').strftime('%H')

                        # Extraindo somente o minuto
                        minuto_extraida = datetime.strptime(data_hora, '%Y-%m-%d %H:%M:%S').strftime('%M')

                        # Extraindo o(s) caracter(es)
                        caractere = linha.split(' > ')[1]

                        # Salvando os dados na base
                        cursor.execute("INSERT INTO log (data_hora, id, caractere, data, hora, minuto) VALUES(?, ?, ?, ?, ?, ?)", 
                                       (data_hora, id_registro, caractere, data_extraida, hora_extraida, minuto_extraida))
                        connection.commit()

                    ## começa aqui
                    contador += 1
                    if ((contador / num_linhas) * 100) > porcentagem:
                        print(str(porcentagem) + '%...', end=' ')
                        porcentagem += 10

                print('100%!')
    


if __name__ == '__main__':
    save_to_sqlite()
