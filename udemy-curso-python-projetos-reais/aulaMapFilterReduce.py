"""
Map, Filter e Reduce
"""

from functools import reduce

produtos = [
    {'nome': 'p1', 'preco': 50.7},
    {'nome': 'p2', 'preco': 40.54},
    {'nome': 'p3', 'preco': 30.2},
    {'nome': 'p4', 'preco': 20.21},
    {'nome': 'p5', 'preco': 50.6},
    {'nome': 'p6', 'preco': 58.9},
    {'nome': 'p7', 'preco': 45},
    {'nome': 'p8', 'preco': 32.2},
    {'nome': 'p9', 'preco': 23.1},
    {'nome': 'p0', 'preco': 40.4}
]

pessoas = [
    {'nome': 'Luiz', 'idade': '23'},
    {'nome': 'Maria', 'idade': '34'},
    {'nome': 'João', 'idade': '45'},
    {'nome': 'Gustavo', 'idade': '37'},
    {'nome': 'Henrique', 'idade': '29'},
    {'nome': 'Débora', 'idade': '50'},
    {'nome': 'Marta', 'idade': '48'},
    {'nome': 'Sérgio', 'idade': '27'},
    {'nome': 'Cintia', 'idade': '40'},
    {'nome': 'Souza', 'idade': '36'}
]

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def aumenta_preco(p):
    p['preco'] = round((p['preco'] * 1.05), 2)
    return p


if __name__ == '__main__':
    nova_lista = map(lambda x: x * 2, lista)
    print(lista)
    print(nova_lista)
    print(list(nova_lista))
    print()

    for produto in produtos:
        print(produto)
    print()

    precos = map(lambda p: p['preco'], produtos)
    for preco in precos:
        print(preco)
    print()

    novos_produtos = map(aumenta_preco, produtos)
    for produto in novos_produtos:
        print(produto)

    # Filter
    nova_lista = filter(lambda x: x > 5, lista)
    print(list(nova_lista))

    # Filter também aceita uma função para realizar o filtro dos valores
    # A função precisa retornar True ou False

    # Reduce
    # Reduce funciona como um acumulador
    soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
    print(soma_lista)


