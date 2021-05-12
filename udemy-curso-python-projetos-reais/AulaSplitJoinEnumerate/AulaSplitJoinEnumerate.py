"""
Split, Join, Enumerate em Python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # list / iteráveis
"""
if __name__ == '__main__':
    print('Split, Join e Enumerate em Python')

    # Split
    string = 'O Brasil é o o o país do futebol, o Brasil é penta.'
    lista_1 = string.split(' ')
    lista_2 = string.split(',')

    print(f'Lista 1: {lista_1}')
    print(f'Lista 2: {lista_2}')
    print()

    # Iterando a lista 1
    palavra = ''
    contagem = 0
    for valor in lista_1:
        # Quantas vezes a palavra apareceu na lista
        print(f'Item da lista: {valor}; quantidade de vezes: {lista_1.count(valor)}')
        qtd_vezes = lista_1.count(valor)

        if qtd_vezes > contagem:
            contagem = qtd_vezes
            palavra = valor

    print()
    print(f'Palavra que apareceu mais vezes: {palavra} ({contagem}x)')
    print()
    for valor in lista_2:
        print(valor.strip().capitalize())  # strip() - remove os espaćos em branco no início e fim da string

    print()

    # Join
    string2 = 'A B C'
    lista_3 = string2.split(' ')
    string3 = ','.join(lista_3)
    print(string3)

    string4 = 'a b c'
    string5 = 'd e f'
    lista_4 = string4.split(' ')
    lista_5 = string5.split(' ')
    string6 = ','.join(lista_4)
    print(string6)
    string6 = string6 + ','.join(lista_5)
    print(string6)
    print()

    ### Enumerate ###
    frase = 'O Brasil é penta.'
    lista = frase.split(' ')
    for indice, valor in enumerate(lista):
        print(f'Índice: {indice} - Valor: {valor}')

    print()
    lista_10 = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]
    # Desempacotando a lista
    for i, v in lista_10:
        print(f'Índice: {i} Valor: {v}')

    # Desempacotando a lista usando enumerate()
    for i, v in enumerate(lista_10):
        print(f'Índice: {i} Valor: {v}')

    # Enumerate - tira dúvidas
    # Lista dentro de lista = lista de duas dimensões
    print(f'Elemento do índice 1 da lista 0: {lista_10[0][1]}')  # Elemento do índice 1 da lista 0

    # Lista enumerada
    lista_enumerada = enumerate(lista_10)
    print(list(lista_enumerada))

    for i, v in enumerate(range(1, 11)):
        print(f'Sequencial: {i}, Valor : {v}')
