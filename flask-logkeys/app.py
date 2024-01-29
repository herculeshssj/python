import os
import sqlite3
import uuid

from flask import Flask, request
from werkzeug.utils import secure_filename
from contextlib import closing
from datetime import datetime


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello! App started successfully =D'


@app.route('/receive_log', methods=['POST'])
def receive_log():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join('/tmp', filename))

    save_to_sqlite(filename)

    return 'OK'


def save_to_sqlite(filename):
    with closing(sqlite3.connect("/data/logkeys.db")) as connection:
        with closing(connection.cursor()) as cursor:
            # Abre o arquivo enviado
            with open('/tmp/' + filename) as fp:
                linhas = fp.readlines()
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
    


if __name__ == '__main__':
    app.run()
