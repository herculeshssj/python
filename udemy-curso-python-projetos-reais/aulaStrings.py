"""
Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NUMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

if __name__ == '__main__':
    num1 = 10
    num2 = 3
    divisao = num1 / num2
    print('{:.2f}'.format(divisao))
    print(f'{divisao:.2f}')

    nome = 'João'
    print(f'{nome:s}')

    cpf = 123456789
    print(f'{cpf:0>11}')

    print(f'{nome:#>50}')
    nome_formatado = '{:@^50}'.format(nome)
    print(nome_formatado)

    """
    Manipulação de strings
    """

    # Qualquer string pode ser manipulada como um array de caracteres
    # Índice[012345678]
    texto = 'Python s2'
    print(texto[2])

    # Índices negativos
    # Os índices negativos começam do (len(string) + 1) * -1 até o -1.
    # O índice 0 fica nos índices positivos
    print(texto[-2])

    # Fatiamento de strings
    nova_string = texto[2:6]  # início (inclusivo) : fim (exclusivo)
    print(nova_string)
    # Ao sublimir o valor inicial, a linguagem presume o índice 0
    nova_string = texto[:6]  # início (inclusivo) : fim (exclusivo)
    print(nova_string)
    # Ao sublimir o valor final, a linguagem presume do índice inicial até o fim da string
    nova_string = texto[4:]  # início (inclusivo) : fim (exclusivo)
    print(nova_string)

    # Loop 'For' embutido na string
    # inicio:fim:passo
    nova_string = texto[0:6:2]
    print(nova_string)

    # Função split()
    # É idêntico ao método split() da classe String no Java
    frase1 = 'O Brasil é o país do futebol, O Brasil é penta.'
    lista1_frase1 = frase1.split(' ')
    lista2_frase1 = frase1.split(',')
    print(lista1_frase1)
    print(lista2_frase1)

    print(f'Letra "a" apareceu {frase1.count("a")} vezes na frase.')
    print(f'Letra "e" apareceu {frase1.count("e")} vezes na frase.')
    print(f'Letra "i" apareceu {frase1.count("i")} vezes na frase.')
    print(f'Letra "o" apareceu {frase1.count("o")} vezes na frase.')
    print(f'Letra "u" apareceu {frase1.count("u")} vezes na frase.')

    # Função join()
    frase2 = ','.join(lista1_frase1)
    print(frase2)