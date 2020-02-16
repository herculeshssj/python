"""
Lambdas (funções anônimas) em Python
"""


# Função tradicional em Python
def funcao(argumento1, argumento2):
    return f'Argumento 1: {argumento1}; Argumento 2: {argumento2}'


def func(item):
    return item[1]


if __name__ == '__main__':
    print('Lambdas (funções anônimas) em Python')

    var = funcao('a1', 'a2')
    print(var)

    # Lambda
    a = lambda x, y: x * y
    print(a(2, 2))

    lista = [
        ['P1', 30],
        ['P2', 20],
        ['P3', 10],
        ['P4', 40],
        ['P5', 55],
        ['P6', 25]
    ]

    lista2 = [
        ['P1', 30],
        ['P2', 20],
        ['P3', 10],
        ['P4', 40],
        ['P5', 55],
        ['P6', 25],
        ['P7', 53]
    ]

    lista.sort(key=func, reverse=True)
    print(lista)

    # Usando Lambda
    lista2.sort(key=lambda item: item[1], reverse=True)
    print(lista2)

    lista3 = lista + lista2
    print(sorted(lista3, key=lambda i: i[0], reverse=False))
