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
    prompt = """I am looking for scientific articles in the context of the Internet of Things (IoT) that discuss the management of health data or personal data of older adults by third parties (doctors, nurses, caregivers, family members, friends) in cases where the older adults are unable to manage their own data due to complications or limitations arising from a medical event (e.g., fall, accident) or deterioration in their chronic health condition (e.g., diabetes, hypertension).

Critically and scientifically analyze the following title and abstract and determine whether it fits my research criteria or not fits. Answer with 'yes' if it fits and give an justification, and 'no' if it does not fit. Do not provide any additional information or explanations when answer 'no'.
    """

    # Criação do prompt para cada entrada da planilha
    df['prompt'] = prompt + '\n\n' + '**Title:** ' + df['Title'].astype(str) + '\n' + '**Abstract:** ' + df['Abstract'].astype(str)

    # Inclusão da coluna para guardar as respostas
    df['response'] = ''

    # Inclusão da coluna para guardar o tempo de processamento
    df['processing_time'] = 0

    # Conectar ao banco de dados SQLite (ou criar se não existir)
    conn = sqlite3.connect('wot-screening.sqlite')

    # Salvar o dataframe na tabela 'articles'
    df.to_sql('articles', conn, if_exists='replace', index=False)

    # Fechar a conexão com o banco de dados para persistir todas as operações
    conn.close()
