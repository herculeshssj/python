"""
Tuplas em Python
"""
if __name__ == '__main__':
    print('Tuplas em Python')

    t1 = (1, 2, 3, 'a', 'b', 'c')  # Uma tupla
    print(type(t1))
    print(t1)

    for v in t1:
        print(v)

    print(t1[2:]) # Fatiamento

    # Tupla sem parênteses
    t2 = 1, 2, 3
    print(t2)

    # Tupla com um elemento
    t3 = 1, # é necessário colocar a vírgula
    print(t3, type(t3))

    # Concatenação
    t4 = t1 + t2 + t3
    print(t4)

    # Desempacotar
    n1, n2, n3, *l1 = t1
    print(l1)

    # Multiplicar tupla
    t5 = t2 * 20
    print(t5)

    # Converter tupla em lista
    l2 = list(t2)
    print(l2, type(l2))

    # Converter lista em tupla
    t6 = tuple(l2)
    print(t6, type(t6))
