import pandas as pd
import matplotlib.pyplot as plt

# Ler a planilha
dados = pd.read_excel("pesquisa.xlsx")

# Usando a coluna específica
coluna = "Renda Mensal"

# Contar os valores
contagem = dados[coluna].value_counts()

# Criar gráfico
contagem.plot(kind='bar')

# Ajustes
plt.xlabel("Renda Mensal")
plt.ylabel("Quantidade de Entrevistados")

# Mostrar gráfico
plt.show()