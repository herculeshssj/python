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
I am preparing a literature scoping review on the Web of Things in the context of active and healthy ageing, privacy and data protection, with the following research objective, research questions and inclusion criteria:
- Objective: Understanding the role of the Web of Things (WoT) in supporting active and healthy aging, while addressing critical challenges such as privacy and data protection.
- Research questions: RQ1 - How does the Web of Things (WoT) support active and healthy aging?; RQ2 - How does WoT address known challenges in active and healthy aging, such as privacy and data protection?

Critically and scientifically analyze the title and abstract of the following article, and determine whether the article is suitable or not for inclusion in the review, or it is necessary a full read of the paper. For the not suitable articles, inform it is not directly related of the objective and research questions, or it is outside of scope of the review. Inform the decision in a single sentence, and justifying your choice in the following sentences.
    """

    # Criação do prompt para cada entrada da planilha
    df['prompt'] = prompt + '\n\n' + '**Title:** ' + df['Title'].astype(str) + '\n' + '**Abstract:** ' + df['Abstract'].astype(str)

    # Inclusão da coluna para guardar as respostas
    df['response'] = ''

    # Conectar ao banco de dados SQLite (ou criar se não existir)
    conn = sqlite3.connect('wot-screening.sqlite')

    # Salvar o dataframe na tabela 'articles'
    df.to_sql('articles', conn, if_exists='replace', index=False)

    # Fechar a conexão com o banco de dados para persistir todas as operações
    conn.close()

    # Abre uma nova conexão com a base para poder armazenar os resultados
    conn = sqlite3.connect('wot-screening.sqlite')
    cursor = conn.cursor()

    # Para cada linha do dataframe
    for _, row in df.iterrows():
        client = OpenAI(api_key='<api_key>')
        response = client.chat.completions.create(
            model="gpt-4o",
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

        ## Faz a atualização dos dados
        cursor.execute("update articles set response = ? where key = ?", (response_text, row['Key']))
        conn.commit()
        
        print('Key ' + row['Key'] + ' processed!')
        time.sleep(5)

    # Fechar a conexão com o banco de dados
    conn.close()