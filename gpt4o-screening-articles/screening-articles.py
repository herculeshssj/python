"""
Script para realizar o processo de screening de títulos e resumos de artigos
usando a API da OpenAI, e usando o modelo GPT-4o, GPT-4o-mini e GPT-4.1-nano.
"""

from openai import OpenAI
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

        client = OpenAI(api_key='<api_key>')  # Substitua <api_key> pela sua chave de API
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": row['prompt']},
                {"role": "user", "content": f"**Title:** {row['Title']}\n**Abstract:** {row['Abstract']}"}
            ],
            temperature=1,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        # Extrair o texto da resposta do modelo
        response_text = response.choices[0].message.content

        processing_time = time.time() - start_time

        ## Faz a atualização dos dados
        cursor.execute("update articles set response = ?, processing_time = ? where key = ?", (response_text, processing_time, row['Key']))
        conn.commit()
        
        print('Key ' + row['Key'] + ' processed!')
        time.sleep(1)

    # Fechar a conexão com o banco de dados
    conn.close()