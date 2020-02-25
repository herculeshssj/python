import copy

"""
Dicionários (Maps) em Python
"""
if __name__ == '__main__':
    print('Dicionários (Maps) em Python')

    d1 = {'chave1': 'valor'}
    print(d1, type(d1))

    # Adicionar uma nova chave
    d1['nova_chave'] = 'Nova chave no dict'
    print(d1)

    # Acessando uma chave específica
    print(d1['chave1'])

    # Criando dicionários usando dict
    d2 = dict(chave1='valor1', chave2='valor2', chave3='valor3')
    print(d2)

    # Criação de um dicionário vazio
    d3 = {}

    # Os dicionários aceitam qualquer tipo de dado imutável como chave
    # Tipos aceitos: int, str e tuple

    # Quando uma chave não existe, o Python lança uma exceção.
    if 'chave' in d2:
        print('Chave existe')
    else:
        print('Chave não existe')

    # O método get() do dicionário evita o lançamento de exceção
    if d2.get('chave1') is not None:
        print('Chave existe')
    else:
        print('Chave não existe')

    # Outra forma de atualizar o valor de uma chave é usar a função update()
    d3.update({'nova_chave': 'novo valor'})
    print(d3)

    # Processando os valores do dicionário
    print('chave1' in d2.values())
    print(d2.values())

    # Imprimindo as chaves do dicionário
    print(d2.keys())

    # Tamanho do dicionário
    print(f'Tamanho do dicionário d1: {len(d1)}')

    # Iterar sobre um dicionário
    for k in d2.items(): # Cada chave/valor é retornado em forma de tupla
        print(k)

    # Posso também iterar o dicionário e pegar a chave e o valor separadamente
    for k, v in d2.items():
        print(f'Chave: {k}; Valor: {v}')

    # Cópia de dicionários
    d5 = d1.copy()
    print(d5)
    # Para copiar sem que o dicionário destino afete o dicionário origem, usando a função deepcopy() do pacote copy
    # Deep copy
    d6 = copy.deepcopy(d5)

    # Listas contendo listas de chaves e valores, posso converter para um dicionário
    lista_dict = [
        ['c1', 1],
        ['c2', 2],
        ['c3', 3]
    ]
    d7 = dict(lista_dict)
    print(d7)

    # Método pop() remove uma chave do dicionário
    # Método popitem() remove a última chave do dicionário

    # Concatenação de dicionários
    d8 = {}
    d8.update(d1)
    d8.update(d2)
    print(d8)

    # Dict comprehension
    lista = [
        ('chave1', 'valor1'),
        ('chave2', 'valor2'),
        ('chave3', 'valor3'),
    ]

    d10 = {x: y for x, y in lista}
    print(d10)

    d11 = {x: y.upper() for x, y in lista}
    print(d11)
