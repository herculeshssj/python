"""
Listas em Python
"""
if __name__ == '__main__':
    print('Listas em Python')

    # Uma lista aceita qualquer tipo de objeto. Ex.:
    lista = [1, 2, 3, 4, 'João', True, 10.25, range(1, 10)]

    # O índice das listas começam com 0, e aceita valores negativos
    vogais = ['a', 'e', 'i', 'o', 'u']
    print(vogais)

    # Listas suportam fatiamento
    print(vogais[1::2])

    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    consoantes = []
    for letra in alfabeto:
        if letra not in 'aeiou':
            consoantes.append(letra)  # Adiciona elementos na lista

    print(consoantes)
    print(consoantes[::2])

    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    l3 = l1 + l2  # Usando o operador '+' para concatenar listas
    print(l3)

    l4 = []
    l4.extend(l1)  # Posso adicionar elementos na lista usando o método extend()
    print(l4)

    # Insere um elemento no índice informado
    l3.insert(3, '#')
    print(l3)

    # Tabuada de 19 de 1 até 100
    tabuada19 = list(range(0, 100, 19))
    print(tabuada19)

    # Vendo os tipos de elementos da lista
    for elem in lista:
        print(f'O tipo do elemento {elem} é {type(elem)}')

    # Enumerate
    for indice, valor in enumerate(tabuada19):
        print(f'Índice: {indice}; Valor: {valor}')

    # Nested lists (listas dentro lista)
    nested_list = [
        [0, 2, 4, 6, 8],
        [1, 3, 5, 7, 9]
    ]
    print(nested_list)

    # Usando enumerate para iterar nested lists
    for indice, valor in enumerate(nested_list):
        print(f'Índice: {indice}; Valor: {valor}')

    # Desempacotamento de listas
    lista_nomes = ['Luiz', 'João', 'Maria']
    n1, n2, n3 = lista_nomes
    print(n2)

    lista_nomes = ['Luiz', 'João', 'Maria', 'Rebeca', 'Mônica', 'Yuri']
    n1, n2, *outra_lista, ultimo_da_lista = lista_nomes
    print(n1, n2, outra_lista, ultimo_da_lista)
    # *outra_lista vai armazenar os valores da lista que não puderam ser associados a uma variável
    # as variáveis iniciais serão associadas aos primeiros valores da lista até encontrar o *outra_lista
    # o mesmo ocorre com os valores finais, eles serão associados com as variáveis que aparecem após *outra_lista

    # Convenção
    n1, n2, *_ = lista_nomes
    # O ' *_ ' indica para outros desenvolvedores que não irei utilizar os demais valores da lista

    # Desempacotamento de listas
    print('Desempacotamento de listas')
    uma_lista = [1, 2, 3, 4, 5]
    print(*uma_lista)
    print(*uma_lista, sep=',')  # Desempacotamento com separador

    ###### List Comprehension #####
    l10 = range(0, 100)
    l11 = [variavel for variavel in l10]
    print(l11)

    ex1 = [v * 2 for v in l10]
    print(ex1)

    ex2 = [(v1, v2) for v1 in l10 for v2 in range(0, 100)]
    print(ex2)

    ex3 = [v.replace('a', '@') for v in alfabeto]
    print(ex3)

    ex4 = [v for v in l10 if v % 2 == 0]
    print(ex4)

    ex5 = [v if v % 3 == 0 else -1 for v in l11]
    print(ex5)
