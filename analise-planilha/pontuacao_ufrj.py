"""
Objetivo: obter um ranking de candidatos que obtiveram pontuação geral acima de 39,00, ordenado por pontuação geral.

A planilha "pontuacaoUFRJ.xlsx" contém a listagem geral de candidatos aprovados na prova. A planilha foi fruto da 
conversão da listagem original em PDF via Adobe Acrobat. No processo de conversão, a coluna "CADP" (coluna K) ficou mesclada 
com outras colunas (de C a J). Usei o próximo MS-Excel para remover a mesclagem e deixar todas as colunas individuais.

Tarefas:
- Ler todas as linhas das colunas C a J em busca de algum conteúdo, e mover para a coluna J;
- Gerar uma nova planilha com o mesmo número de colunas, mantendo apenas as linhas que contenham os candidatos com pontuação 
igual ou maior que 39 (coluna O contém a pontuação).

Atenção: existem ao longo das linhas entradas de texto, que eram justamente o cabeçalho que aparecia no início das páginas 
no arquivo PDF. É necessário ignorar estas linhas. Para identificar, verifique se na coluna A contém a palavra "INSCRIÇÃO".
"""
if __name__ == "__main__":
    import pandas as pd

    # Ler a planilha original
    df = pd.read_excel("pontuacaoUFRJ.xlsx")

    # Criar uma nova coluna 'CADP' a partir das colunas C a J
    df['CADP'] = df[df.columns[2:10]].apply(lambda x: ' '.join(x.dropna().astype(str)), axis=1)

    # Filtrar os candidatos com pontuação geral >= 39 e ignorar linhas de cabeçalho
    # Antes de comparar o número, é necessário converter a coluna 'PONTOS' para numérica, tratando erros de conversão
    df['PONTOS'] = pd.to_numeric(df['PONTOS'], errors='coerce')
    filtered_df = df[(df['PONTOS'] >= 39) & (~df['INSCRIÇÃO'].str.contains("INSCRIÇÃO", na=False))]

    # Selecionar as colunas desejadas para a nova planilha
    final_df = filtered_df[['INSCRIÇÃO', 'NOME', 'CADP', 'COGE', 'COIN', 'CEAD', 'PONTOS']]

    # Salvar a nova planilha
    final_df.to_excel("ranking_candidatos_ufrj.xlsx", index=False)