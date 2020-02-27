"""
Iteráveis, iteradores e geradores
"""
import sys
import time


def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)

def gera1():
    variavel = 'valor 1'
    yield variavel
    variavel = 'valor 2'
    yield variavel
    variavel = 'valor 3'
    yield variavel

if __name__ == '__main__':
    g = gera()

    g1 = gera1()

    print(next(g))

    for v in g:
        print(v)

    print(hasattr(g, '__iter__'))
    print(hasattr(g, '__next__'))

    print(next(g1))
    print(next(g1))
    print(next(g1))

    # Memory
    lista = list(range(1000))
    print(sys.getsizeof(lista))
    print(type(lista))

    lista = [x for x in range(1000)]
    print(type(lista))

    lista = (x for x in range(1000))
    print(sys.getsizeof(lista))
    print(type(lista))
    print(next(lista))




