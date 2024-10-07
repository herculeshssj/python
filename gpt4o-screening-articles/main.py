"""
Script para realizar o processo de screening de títulos e resumos de artigos
usando a API da OpenAI, e usando o modelo GPT-4o e GPT-4o-mini
"""

from openai import OpenAI
import pandas as pd
import sqlite3
import time

if __name__ == '__main__':

    # Ler a planilha Excel (por exemplo, 'planilha.xlsx')
    df = pd.read_excel('planilha.xlsx')

    # Texto inicial que será enviado no prompt
    prompt = """
I am preparing a literature scoping review on the Web of Things in the context of active and healthy ageing, with the following research questions: 'RQ1: How does the Web of Things (WoT) support active and healthy aging?'; 'RQ2: How does WoT address known challenges in active and healthy aging, such as privacy and data protection?'

Analyze the title and abstract of the following article, and determine whether the article is suitable or not for inclusion in the review, or it is necessary a full read of the paper. Inform the decision in a single sentence, and justifying your choice in the following sentences.
    """

    # Criação do prompt para cada entrada da planilha
    df['prompt'] = prompt + '\n\n' + '**Title:** ' + df['Title'].astype(str) + '\n' + '**Abstract:** ' + df['Abstract'].astype(str)

    # Inicializar uma lista para armazenar as respostas
    responses = []

    # Para cada linha do dataframe
    for _, row in df.iterrows():
        client = OpenAI(api_key='<api_key>')
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": f"**Title:** {row['Title']}\n**Abstract:** {row['Abstract']}"}
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        # Extrair o texto da resposta do modelo
        response_text = response.choices[0].message.content
        responses.append(response_text)

        print('Key ' + row['Key'] + ' processed!')
        time.sleep(5)

    # Adicionar a coluna 'response' ao dataframe
    df['response'] = responses

    # Conectar ao banco de dados SQLite (ou criar se não existir)
    conn = sqlite3.connect('wot-screening.sqlite')

    # Salvar o dataframe na tabela 'articles'
    df.to_sql('articles', conn, if_exists='replace', index=False)

    # Fechar a conexão com o banco de dados
    conn.close()