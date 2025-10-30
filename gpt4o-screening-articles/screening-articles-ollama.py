"""
Script para realizar o processo de screening de títulos e resumos de artigos
usando a API do Ollama, e LLMs opensource.
"""

from ollama import Client
import sqlite3
import time

if __name__ == '__main__':
    # Abre uma nova conexão com a base para poder armazenar os resultados
    conn = sqlite3.connect('wot-screening.sqlite')
    conn.row_factory = sqlite3.Row  # Para acessar colunas pelo nome
    cursor = conn.cursor()

    # Para cada linha do dataframe
    for row in cursor.execute("select * from articles where response = ''").fetchall():
        # Verifica se a chave já foi processada 
        if row['response'] != '':
            print('Key ' + row['Key'] + ' already processed!')
            continue

        # Inicia o tempo de processamento
        start_time = time.time()

        # Cria o cliente apontando para o servidor remoto
        client = Client(host="http://aceraspire5:11434")
        # Aumenta o timeout para 600 segundos
        client.timeout = 600
        response = client.chat(
            model="llama3.2",
            messages=[
                {"role": "system", "content": row['prompt']},
                {"role": "user", "content": f"**Title:** {row['Title']}\n**Abstract:** {row['Abstract']}"}
            ]
        )
        # Extrair o texto da resposta do modelo
        response_text = response['message']['content']

        processing_time = time.time() - start_time

        ## Faz a atualização dos dados
        cursor.execute("update articles set response = ?, processing_time = ? where key = ?", (response_text, processing_time, row['Key']))
        conn.commit()
        
        print('Key ' + row['Key'] + ' processed!')
        time.sleep(5)

    # Fechar a conexão com o banco de dados
    conn.close()