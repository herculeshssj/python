"""
Aulas de try...except e raise

Built-in exceptions: https://docs.python.org/3/library/exceptions.html

"""


def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        #print('Houve divisão por zero! Retornando o valor 0')
        #print('Houve divisão por zero! Retornando a exceção...')
        raise ValueError('Houve divisão por zero!')


if __name__ == '__main__':
    print('Try, except e raise')

    try:
        # print('Ocorrerá uma exceção')
        # a = []
        print(a)
    except NameError as erro:
        print('Ocorreu uma exceção: ', erro)
    except Exception as err:
        print('Ocorreu um erro inesperado! Erro: ', err)
    else:
        print('Bloco else do try')
    finally:
        print('Bloco finally, fechando os recursos abertos...')

    print('O código continua...')

    print('Lançando exceções...')

    try:
        print(divide(10, 0))
    except Exception as error:
        print('Erro:', error)
