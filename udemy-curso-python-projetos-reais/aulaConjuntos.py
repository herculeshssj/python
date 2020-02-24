# add (adiciona), update (atualiza), clear, discard
# union | (une)
# intersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)

if __name__ == '__main__':
    print('Conjuntos em Python')

    s1 = {1, 2, 3, 4, 5}  # Conjunto

    sou_uma_lista = [1, 2, 3, 4, 5]
    sou_uma_tupla = (1, 2, 3, 4, 5)
    sou_um_conjunto = {1, 2, 3, 4, 5}
    sou_um_dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

    s2 = {}  # É um dicionario
    s3 = set()  # É um set (conjunto)

    # Adiciona um elemento
    s1.add(10)
    print(s1)

    # Atualiza um elemento
    # Obs: O set não aceita elementos duplicados
    s1.update([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(s1)

    # Elimina um elemento
    s1.discard(6)
    print(s1)

    l1 = [1, 2, 3, 4, 5]
    l2 = [5, 4, 3, 2, 1]
    s4 = set(l1)
    s4.update(l2)
    print(s4)

    s5 = s1 | s3  # Union
    print(s5)

    s6 = s3 & s5  # Intersection
    print(s6)

    s7 = s1 - s3  # Diference
    print(s7)

    s8 = s1 ^ s3  # symmetric difference
    print(s8)
