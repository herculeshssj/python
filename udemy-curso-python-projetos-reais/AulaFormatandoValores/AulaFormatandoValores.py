"""
Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d, ou f)

> - Esquerda
< - Direita
^ - Centro

São usados com F-String e a funćão format()
"""

if __name__ == '__main__':
    print('Formatando valores com modificadores')
    num_1 = 10
    num_2 = 3
    divisao = num_1 / num_2
    print(f'{divisao}')
    print('{}'.format(divisao))
    print('{:.2f}'.format(divisao))
    print(f'{divisao:.2f}')
    print()
    # Tamanho padrão
    # :(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d, ou f)
    print(num_1)
    print(f'{num_1:0>10}')  # preenchendo com zeros à esquerda
    num_3 = 1150
    print(f'{num_3:0>10}')  # preenchendo com zeros à esquerda
    print(f'{num_3:0<10}')  # preenchendo com zeros à direita
    print(f'{num_3:0^10}')  # preenchendo com zeros à direta e à esquerda
    print(f'{num_3:.2f}')  # formatando o número como float
    print(f'{num_3:0>10.2f}')  # formatando o número como float e preenchendo com zeros à esquerda
    print()
    nome = ' José '
    print(f'{nome:#^50}')  # Preenchendo a string com cerquilha
    nome_formatado = '{:*^50}'.format(nome)
    print(nome_formatado)

    # Funćões built-in de strings
    # ljust()
    print(nome.ljust(50, '#'))  # Preenche com '#' à esquerda da string
    # rjust()
    print(nome.rjust(50, '#'))  # Preenche com '#' à direita da string
    # zfill()
    print(nome.zfill(50))  # Preenche a string com zero
    # lower()
    print(nome.lower())  # Tudo minúsculo
    # upper()
    print(nome.upper())  # Tudo maiúsculo
    # title()
    print(nome.title())  # Primeiras letras em maiúsculas
