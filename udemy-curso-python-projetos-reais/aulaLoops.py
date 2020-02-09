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

    print('Iteração de strings')
    minha_string = 'O rato roeu a roupa do rei de Roma.'
    print(minha_string[2])

    contador = 0
    string_cebolinha = ''
    while contador < len(minha_string):
        print(minha_string[contador])

        if minha_string[contador] == 'r':
            string_cebolinha += 'l'
        elif minha_string[contador] == 'R':
            string_cebolinha += 'L'
        else:
            string_cebolinha += minha_string[contador]

        contador += 1
    else:
        print('Fim da string')

    print(f'String à la Cebolinha: {string_cebolinha}')
    print('Quantidade de "L" inseridos: ', string_cebolinha.count('L'))
    print('Quantidade de "l" inseridos: ', string_cebolinha.count('l'))

    print()
    print('Estrutura for')
    texto = 'Python'
    for letra in texto:
        print(letra)

    # Mostrando o índice
    for n, letra in enumerate(texto):
        print(n, letra)

    print()
    # range( start=0, stop, step=1)
    for numero in range(1, 10, 2): # Inicia no 1, até 10, 2 passos
        print(numero)

    print()
    for n in range(20, 10, -1):
        print(n)

    # Break, continue e else também são válidos no loop for
    numeros = list(range(0,11))
    for n in numeros:
        if n % 2 == 0:
            print(f'{n} é par')
        else:
            print(f'{n} é ímpar')
    else:
        print('Todos os números da lista foram exibidos.')

