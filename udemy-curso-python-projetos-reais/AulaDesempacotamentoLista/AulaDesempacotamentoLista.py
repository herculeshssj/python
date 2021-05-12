"""
Desempacotamento de listas em Python
"""
if __name__ == '__main__':
    print('Desempacotamento de listas')

    lista = ['Luiz', 'João', 'Maria']
    n1, n2, n3 = lista
    print(f'Valor de n1: {n1}')
    print(f'Valor de n2: {n2}')
    print(f'Valor de n3: {n3}')
    print()

    # Desempacotando quando a lista tem mais valores que a quantidade de variáveis atribuídas
    n1, n2, *outra_lista = lista
    print(f'Valor de n1: {n1}')
    print(f'Valor de n2: {n2}')
    print(f'Outra lista, com o restante dos valores: {outra_lista}')
    print()

    # Obtendo o último valor da lista
    lista = ['Luiz', 'João', 'Maria', 'José', 'Tomas', 'Cristina']
    n1, n2, *outra_lista, ultimo_da_lista = lista
    print(f'Valor de n1: {n1}')
    print(f'Valor de n2: {n2}')
    print(f'Outra lista, com o restante dos valores: {outra_lista}')
    print(f'Último da lista: {ultimo_da_lista}')

    # Indicar que você não irá utilizar o restante dos valores da lista
    n1, n2, *_ = lista
    print(f'Valor de n1: {n1}')
    print(f'Valor de n2: {n2}')