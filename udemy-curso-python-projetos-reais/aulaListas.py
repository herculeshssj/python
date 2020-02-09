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
