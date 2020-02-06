'''
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar. Caso o
usuário não digite um número inteiro, informe que não é um número inteiro.
'''

if __name__ == '__main__':
    entrada = input('Informe um número inteiro: ')

    numero = 0;

    if entrada.isnumeric():
        numero = int(entrada)

        if numero % 2 == 0:
            print('O número informado é par.')
        else:
            print('O número informado é ímpar')

    else:
        print('O número informado não é um inteiro válido')
