import pandas as pd

if __name__ == '__main__':
    print('Extrair texto')

    # Substitua 'seu_arquivo.xlsx' pelo caminho do seu arquivo Excel
    caminho_arquivo = 'poster.xlsx'

    # Carrega o arquivo Excel em um DataFrame
    df = pd.read_excel(caminho_arquivo)

    # Extrai a última palavra de todas as linhas da primeira coluna
    primeira_coluna = df.iloc[:, 0]
    ultima_palavra_todas_linhas = primeira_coluna.str.split().str[-1]

    # Exibe as últimas palavras
    for indice, palavra in enumerate(ultima_palavra_todas_linhas):
        print(f"Última palavra da linha {indice + 1}: **{palavra}**")

    # Cria um novo DataFrame com as últimas palavras
    df_resultado = pd.DataFrame({'Ultima_Palavra': ultima_palavra_todas_linhas})

    # Salva o DataFrame em um arquivo CSV
    caminho_arquivo_csv = 'resultado.csv'
    df_resultado.to_csv(caminho_arquivo_csv, index=False)

    print(f"Resultado salvo em '{caminho_arquivo_csv}'")
