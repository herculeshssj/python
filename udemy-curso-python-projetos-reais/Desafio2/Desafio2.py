"""
Faća um programa que peća ao usuário para digital um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faća um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudaćão apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faća um programa que peća o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

from AulaFuncoesBuiltIn.AulaFuncoesBuiltIn import *

if __name__ == '__main__':
    print('##### Desafio 2 #####')

    print('***** Exercício 1 *****')
    numero = input('Digite um número inteiro: ')
    if is_int(numero):
        numero = int(numero)
        if numero % 2 == 0:
            print('É par!')
        else:
            print('É ímpar!')
    else:
        print('Não é um número inteiro!')

    print('***** Exercício 2 *****')
    hora_atual = input('Informe a hora atual (0-23): ')
    if is_int(hora_atual):
        hora_atual = int(hora_atual)
        if hora_atual >=0 and hora_atual <= 23:
            if hora_atual >=0 and hora_atual <=11:
                print('Bom Dia!')
            elif hora_atual > 11 and hora_atual <=17:
                print('Boa Tarde!')
            else:
                print('Boa Noite!')
        else:
            print('Hora fora do intervalo!')
    else:
        print('Hora inválida!')

    print('***** Exercício 3 *****')
    nome_usuario = input('Digite seu nome: ')
    if len(nome_usuario) <= 4:
        print('Seu nome é curto.')
    elif len(nome_usuario) > 4 and len(nome_usuario) <= 6:
        print('Seu nome é normal.')
    else:
        print('Seu nome é muito grande.')
