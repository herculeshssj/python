"""
Primeiro passo: iniciar o ambiente virtual do Python:
1º - abra o VS Code, e vá no menu File > Open Folder, e selecione a pasta onde estão os arquivos do projeto.

2º - abra o terminal integrado do VS Code e crie um ambiente virtual com o comando: 

python -m venv venv

3º - com o ambiente virtual criado, ative-o com o comando:
- No Windows: venv\Scripts\activate.bat
- No macOS/Linux: source venv/bin/activate

4º - com o ambiente virtual ativado, instale as bibliotecas necessárias com o comando:

pip install pandas matplotlib openpyxl

5º - agora, com o ambiente virtual configurado e as bibliotecas instaladas, você pode executar o código do arquivo 
analise.py para ler a planilha e criar o gráfico de barras com os dados da coluna "Renda Mensal".

ATENÇÃO: Certifique-se de que o arquivo "pesquisa.xlsx" esteja na mesma pasta do arquivo "analise.py".

OBS: Caso aparece mensagens pop-up do VS Code, ignore-as e siga os passos descritos acima.
"""


"""
Compreendendo o código do arquivo analise.py
"""

# Importação das bibliotecas necessárias
import pandas as pd # pandas - Biblioteca para manipulação de dados
import matplotlib.pyplot as plt # matplotlib - Biblioteca para criação de gráficos
# openpyxl - Biblioteca para ler arquivos Excel (.xlsx) - Apesar de não ser importada diretamente, 
# é necessária para que o pandas possa ler arquivos Excel.

# Leitura da planilha Excel usando o pandas
# Os dados da planilha são carregados em um DataFrame do pandas, que é uma estrutura de dados tabular.
dados = pd.read_excel("pesquisa.xlsx")

# Plus: para conseguir ver uma pequena amostra dos dados carregados, você pode usar o método head() do DataFrame:
# print(dados.head()) # Descomente esta linha para ver as primeiras linhas do DataFrame e entender a estrutura dos dados.

# Usando a coluna específica
# Esta variável armazena o nome da coluna que queremos analisar, neste caso, "Renda Mensal".
coluna = "Renda Mensal"

# Contar os valores
# O método value_counts() conta a quantidade de ocorrências de cada valor único na coluna especificada.
contagem = dados[coluna].value_counts()

# Plus: para ver a contagem dos valores, você pode imprimir a variável contagem:
# print(contagem) # Descomente esta linha para ver a contagem dos valores únicos na coluna especificada.

# Cria o gráfico de barras usando o método plot() do pandas, especificando o tipo de gráfico como 'bar'.
contagem.plot(kind='bar')

# Ajustes - Adiciona título e rótulos aos eixos do gráfico para melhor compreensão.
plt.xlabel("Renda Mensal") # Rótulo do eixo x
plt.ylabel("Quantidade de Entrevistados") # Rótulo do eixo y

# Mostrar o gráfico, abrindo uma janela com a visualização do gráfico de barras criado.
plt.show()