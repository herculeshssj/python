# Lista
mesesList = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

# Tupla imutável
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

n = 1

while(n < 4):
    mes = int(input("Escolha um mês (1-12): "))
    if 1 <= mes <= 12:
        print('O mês é {}'.format(meses[mes-1]))
    n += 1

# Range
for valor in range(1,10):
    print(valor)


# Conjunto (set()). Os conjuntos não são ordenados e não aceitam valores duplicados
frutas = {'laranja', 'banana', 'uva', 'pera', 'laranja', 'uva', 'abacate'}

a = set('abacate')
b = set('abacaxi')
print(a)
print(b)
print(a - b) # diferença
print(a | b) # união
print(a & b) # interseção
print(a ^ b) # diferença simétrica

# Para criar um conjunto vazio, precisa usar set(). Usar {} cria um dicionário vazio
c = set()
d = {}
print(type(c))
print(type(d))

# Dicionário
pessoa = {'nome': 'João', 'idade': 25, 'cidade': 'São Paulo'}
print(pessoa)
pessoa['pais'] = 'Brasil'
print(pessoa)