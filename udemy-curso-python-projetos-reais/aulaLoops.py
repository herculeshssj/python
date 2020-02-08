"""
Aulas sobre loops em Python
"""
if __name__ == '__main__':
    print('Estrutura while')
    i = 0
    while i <= 10:
        i += 1
        if i % 2 == 0:
            continue
        if i > 10:
            break
        print(f'Valor de i: {i}')


    contador = 0
    while contador < 10:
        print(f'Valor do contador: {contador}')
        contador += 1
    else:
        print('Entrei no else do while')

    print('Estrutura for')
