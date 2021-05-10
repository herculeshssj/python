"""
Listas em Python
fatiamento
append, insert, pop, del, clear. extend, +
min, max
range
"""

if __name__ == '__main__':
    print('Listas em Python')

    # Uma lista
    uma_lista = [1, 2, 3, 4, 'string', True, 10.5]

    # Criaćão de lista e acessando os valores
    lista = ['A', 'B', 'C', 'D', 'E']
    print(f'Acessando o valor "A" da lista criada: {lista[0]}')
    # As listas aceitam índices negativos, que nem as strings

    # Imprimindo a lista inteira
    print(f'Imprimindo o conteúdo da lista: {lista}')

    # Modificando o item da lista
    lista = ['A', 'B', 'C', 'D', 'E', 10.5]
    print(f'Lista: {lista}')
    lista[5] = 'F'
    print(f'Lista modificada: {lista}')

    # Fatiamento
    print(f'Mostrando os índices 2 a 5 da lista: {lista[2:5]}')
    print(f'Mostrando os primeiros três índices da lista: {lista[:3]}')
    print(f'Mostrando os últimos três índices da lista: {lista[3:]}')
    print(f'Usando step: {lista[::2]}')
    print(f'Mostrando a lista de forma invertida: {lista[::-1]}')
    print()

    ### Usando funćões para manipular listas ###
    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    print(f'Lista 1: {l1}')
    print(f'Lista 2: {l2}')

    # Concatenaćão de listas
    l3 = l1 + l2
    print(f'Concatenaćão de listas: {l3}')
    # Concatenaćão de listas usando a funćão extend()
    l4 = [7, 8, 9]
    l3.extend(l4)
    print(f'Concatenaćão de listas usando extend(): {l3}')

    # Inserir um valor no final da lista
    l3.append(10)
    print(f'Inserćão de valores usando append(): {l3}')

    # Inserindo um valor em uma posićão na lista
    l3.insert(0, 0)
    print(f'Inserido o valor "0" no início da lista: {l3}')

    # Removendo o último elemento da lista
    l3.pop(len(l3) - 1)  # Usando len() para obter o tamanho da lista
    print(f'Removido o valor "10" do final da lista: {l3}')

    # Excluindo elementos da lista
    del (l3[3:6])
    print(f'Usando funćão del(); excluído os elementos do índice 3 a 6: {l3}')

    # Mínimo e máximo valor da lista
    print(f'Maior valor da lista: {max(l3)}')
    print(f'Menor valor da lista: {min(l3)}')
    print()

    # Usando range()
    l5 = list(range(0, 100, 8))
    print(f'Lista gerada a partir da funćão range(): {l5}')

    # Iterando a lista
    soma = 0
    for valor in l5:
        soma += valor
    print(f'Soma dos valores da lista: {soma}')
