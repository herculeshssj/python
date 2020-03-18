"""
Decoradores
"""

from time import time
from time import sleep


# def master():  # Função master
#    def slave():  # Função slave
#        print('Oi')
#    return slave # Master está retornando a função slave

# Função decoradora
def master(funcao):  # Função master recebe uma função como parâmetro
    def slave():  # Função slave irá executar a função que master recebeu como parâmetro
        funcao()

    return slave  # Master está retornando a função slave


@master
def fala_oi():  # Usando o '@' para decorar a função fala_oi()
    print('Oi')


# Teste com decoradores
def velocidade(funcao):  # Função decoradora
    def interna(*args, **kwargs):
        start_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f'A função {funcao.__name__} levou {tempo:.2f} ms para executar.')
        return resultado

    return interna


@velocidade
def demora():
    for i in range(5):
        print(i)
        sleep(1)


if __name__ == '__main__':
    print('Decoradores')

    # fala_oi()  # Chamando uma função. Nada de novo até o momento
    #
    # # Salvando uma função em uma variável
    # variavel = fala_oi
    # variavel()
    # print(type(variavel))  # Mostrando o tipo
    #
    # master()  # Chamando a função master. Ao rodar o programa nada acontece
    # funcao_slave = master()  # Salvando a função slave em uma variável
    # funcao_slave()  # Executando a função slave()
    #
    # fala_oi = master(fala_oi)  # Função fala_oi foi decorada com a função master()
    # fala_oi()

    demora()
