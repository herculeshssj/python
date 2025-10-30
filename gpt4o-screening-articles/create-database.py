"""
Script para realizar o processo de screening de títulos e resumos de artigos
usando a API da OpenAI, e usando o modelo GPT-4o e GPT-4o-mini
"""

import pandas as pd
import sqlite3

if __name__ == '__main__':

    # Ler a planilha Excel (por exemplo, 'planilha.xlsx')
    df = pd.read_excel('planilha.xlsx')

    # Texto inicial que será enviado no prompt
    prompt = """I am selecting scientific articles that align with my PhD research
**Research problem:** _How should health data of older adults with cognitive impairment be managed by third parties (doctors, nurses, caregivers, family members, friends) considering the growing concerns for personal data sovereignty, emphasized by legal regulations such as the GDPR?_
**Research question:** _How can we enable the delegated management of personal data in IoT/WoT environments for older adults with cognitive impairment, in a secure, auditable manner, and in compliance with regulations such as the GDPR, respecting your data sovereignty?_
**Objective:** _To explore the delegated management of data stored in PODs in the context of the IoT/WoT for older adults with cognitive impairment, to ensure the continuity of assistance by third parties in line with the principles of GDPR and data sovereignty._
**Hypothesis:** _It is possible to design a delegated management architecture based on Solid protocol that ensures security, traceability, and compliance with the GDPR in the context of IoT for older adults with cognitive impairment._

Critically and scientifically analyze the following title and abstract and determine whether it fits my PhD research or not fits, based on context of research problem. Answer with 'yes' if it fits and give an justification, and 'no' if it does not fit. Do not provide any additional information or explanations when answer 'no'. If the abstract is empty, ignore the article.
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
