"""
Desafio 5
"""

if __name__ == '__main__':
    lista_invertida = list(range(10, 0, -1))
    print(lista_invertida)

    for indice, valor in enumerate(lista_invertida):
        print(f'{indice}, {valor}')