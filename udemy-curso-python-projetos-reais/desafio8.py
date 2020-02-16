"""
Desafio 8 - funções parte 2

1 - Crie uma funcao1 que recebe uma funcao2 como parâmetro e retorne o valor da funcao2 executada.

2 - Crie uma funcao1 que recebe uma funcao2 como parâmetro e retorne o valuro da funcao2 executada. Faça a funcao1
executar duas funções que recebam um número diferente de argumentos.
"""

"""
1 - Crie uma funcao1 que recebe uma funcao2 como parâmetro e retorne o valor da funcao2 executada.
"""


def exerc1_funcao1(param):
    return param()


def exerc1_funcao2():
    print('Função 2 foi executada')


"""
2 - Crie uma funcao1 que recebe uma funcao2 como parâmetro e retorne o valuro da funcao2 executada. Faça a funcao1
executar duas funções que recebam um número diferente de argumentos.
"""


def exerc2_funcao1(var):
    exerc2_funcao3(10)
    exerc2_funcao4(10, 20)
    return var()


def exerc2_funcao2():
    return 'Sou a função 2'


def exerc2_funcao3(n1):
    print(f'Valor de n1: {n1}')


def exerc2_funcao4(n1, n2):
    print(f'Valor de n1: {n1}; Valor de n2: {n2}')


if __name__ == '__main__':
    print('Desafio 8 - funções parte 2')

    print('Exercício 1')
    funcao = exerc1_funcao2
    exerc1_funcao1(funcao)

    funcao2 = exerc2_funcao2
    print(exerc2_funcao1(funcao2))

# ***** Gabarito *****

"""


1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada.


# def ola_mundo():
#     return 'Olá mundo!'
#
#
# def mestre(funcao):
#     return funcao()
#
#
# print(ola_mundo())


2 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada. Faça a função1 executar duas funções que recebam um número 
diferente de argumentos.



def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'Oi {nome}'


def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


executando = mestre(fala_oi, 'Luiz')
executando2 = mestre(saudacao, 'Luiz', saudacao='Bom dia!')
print(executando)
print(executando2)


"""