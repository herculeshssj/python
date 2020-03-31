"""
04.252.011/0001-10
40.688.134/0001-61
71.506.168/0001-11
12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro dígito = 1 (Se o dígito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segunro digito
"""

import re

if __name__ == '__main__':

    # Declaração das variáveis globais
    nome = ''
    cnpj = ''

    # Loop while que pede o nome e o CPF do usuário
    while True:
        # Solicita o nome do usuário
        nome = input('Informe o nome fantasia da empresa: ')

        # Solicita o CNPJ da empresa
        cnpj = input('Informe o CNPJ (formato: 99.999.999/9999-99): ')

        # Verifica se o usuário informou o nome e o CNPJ
        if not nome:
            print('Nome não infomado!')
            continue
        elif not cnpj:
            print('CNPJ não informado!')
            continue

        # Faz a limpeza do CPF
        # cnpj = cnpj.replace('.', '').replace('-', '').replace('/', '') # Substituído por Regex
        cnpj = re.sub(r'[^0-9]', '', cnpj)

        # Verifica se nenhum outro caractere foi digitado no CPF
        if not cnpj.isnumeric():
            print('CNPJ deve conter somente números!')
            continue
        elif len(cnpj) != 14:
            print('CNPJ deve conter 14 números!')
            continue
        else:
            # CNPJ prontro para validar
            break

    # Guardando os doze primeiros números do CNPJ informado
    cnpj_validado = cnpj[0:12]

    # Variável que guardará a soma dos valores do CPF
    soma_numeros_cnpj = 0

    # Índice
    indice = 5

    # Itera o CNPJ para realizar a primeira parte do cálculo
    for numero in cnpj_validado:
        soma_numeros_cnpj += int(numero) * indice
        indice -= 1
        if indice < 2:
            indice = 9

    # Calcula o primeiro dígito verificador
    dv1 = 11 - (soma_numeros_cnpj % 11)
    if dv1 > 9:
        cnpj_validado += '0'
    else:
        cnpj_validado += str(dv1)

    # Zera as variáveis auxiliares
    soma_numeros_cnpj = 0
    indice = 6

    # Itera o CNPJ validado para realizar a segunda parte do cálculo
    for numero in cnpj_validado:
        soma_numeros_cnpj += int(numero) * indice
        indice -= 1
        if indice < 2:
            indice = 9

    # Calcula o segundo dígito verificador
    dv2 = 11 - (soma_numeros_cnpj % 11)
    if dv2 > 9:
        cnpj_validado += '0'
    else:
        cnpj_validado += str(dv2)

    # Verifica se o CNPJ gerado é idêntico ao CNPJ informado
    if cnpj == cnpj_validado:
        print('O CNPJ informado é válido!')
    else:
        print('O CNPJ informado não é válido!')