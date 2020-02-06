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


