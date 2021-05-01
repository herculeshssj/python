"""
While em Python
Utilizado para realizar aćões enquanto uma condićão for verdadeira

Requisitos: entender condićões e operadores
"""

from AulaFuncoesBuiltIn.AulaFuncoesBuiltIn import *

if __name__ == '__main__':
    print('While em Python')

    while True:  # loop infinito
        nome = input('Qual o seu nome (0 - sair)? ')
        # Condićão para poder sair do loop infinito
        if nome == '0':
            break  # Encerra a execućão do bloco While
        else:
            print(f'Olá {nome}')
    print()

    x = 0
    while x < 100:
        print(x)
        x = x + 1
    print('Acabou!')
    print()

    # Usando a palavra continue
    x = 0
    while x < 100:
        if x % 3 == 0:
            print(x)
        x = x + 1
        continue

    print('Acabou!')
    print()

    # While dentro do while
    x = 0  # coluna

    while x < 10:
        y = 0  # linha
        while y < 5:
            print(f'X vale {x} e Y vale {y} - ({x},{y})')
            y += 1
        x += 1  # x = x + 1
    print('Acabou!')
    print()

    print("*** Calculadora ***")
    print("Digite 0 no operador para sair")
    while True:
        operador = input('Digite um operador (+, -, *, /): ')
        num_1 = input('Digite um número: ')
        num_2 = input('Digite outro número: ')

        if not is_number(num_1) or not is_number(num_2):
            print('Valores digitados não são válidos')
            continue

        num_1 = int(num_1)
        num_2 = int(num_2)

        if operador == '+':
            print(f'Soma: {num_1 + num_2}')
        elif operador == '-':
            print(f'Subtraćão: {num_1 - num_2}')
        elif operador == '*':
            print(f'Multiplicaćão: {num_1 * num_2}')
        elif operador == '/':
            print(f'Divisão: {num_1 / num_2}')
        elif operador == '0':
            print('Tchau!')
            break
        else:
            print('Operador inválido!')
