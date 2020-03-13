"""
Itertools - count
Contadores infinitos
A função count() retorna um iterador
A função range() é um iterável
"""
from itertools import count, combinations, permutations, product

if __name__ == '__main__':
    print('Itertools - count()')

    contador = count()

    # Não executar!!!
    #for valor in contador:
    #    print(valor)

    for valor in contador:
        print(valor)

        if valor >= 10:
            break;

    print()

    contador = count(start=10, step=10)
    for valor in contador:
        print(valor)

        if valor >= 1000:
            break;

    print()

    # Com ponto flutuante
    contador = count(start=5, step=0.1)
    for valor in contador:
        print(round(valor, 2))

        if valor >= 10:
            break;

    print()

    # Invertido
    contador = count(start=9, step=-1)
    for valor in contador:
        print(round(valor, 2))

        if valor >= 10 or valor <= -10:
            break;

    print()

    contador = count()
    lista = ['João', 'Maria', 'Luiz', 'Manoel']
    lista = zip(contador, lista)
    print(list(lista))
    print()

    """
    Combination, Permutations e Product - Itertools

    Combinação - Ordem não importa
    Permutação - Ordem importa
    Ambos não repetem valores úncis
    Produto - Ordem importa e repete valores únicos
    """

    pessoas = ['João', 'Maria', 'Luiz', 'Manoel', 'André', 'Eduardo', 'Letícia', 'Jéssica']

    for grupo in combinations(pessoas, 2):
        print(grupo)

    print()

    for grupo in permutations(pessoas, 2):
        print(grupo)

    print()

    for grupo in product(pessoas, repeat=2):
        print(grupo)
