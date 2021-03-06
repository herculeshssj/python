"""
Módulos

Módulos padrão do Python:
Módulos são arquivos .py (que contém código Python) e servem para expandir as funcionalidades padrão da linguagem.
Veja todos os módulos padrão no Python em: https://docs.python.org/3/py-modindex.html
"""

# import sys # Importa tudo do módulo sys
# from sys import platform  # Importa somente a função do módulo
from sys import platform as so  # Usando alias
from random import randint
from random import randrange, random  # importando mais de uma função

import libs
from libs.lib1Modulo import dobra_lista, multiplica, PI

# Importando pacotes
import package1Modulo.calculaPreco # pacote.modulo

if __name__ == '__main__':
    print('Módulos')

    # print('Plataforma:', platform)
    # print('Plataforma:', sys.platform)
    print('Plataforma:', so)

    print(randint(0, 10))

    lista = [1, 2, 3, 4, 5]
    print(dobra_lista(lista))
    print(multiplica(lista))
    print(PI)

    # Pacotes
    preco = 49.90
    preco_com_aumento = package1Modulo.calculaPreco.aumento(preco, 10)
    print(preco_com_aumento)

    preco_com_reducao = package1Modulo.calculaPreco.reducao(preco, 10)
    print(preco_com_reducao)

    preco_com_aumento = package1Modulo.calculaPreco.aumento(preco, 15, formata=True)
    print(preco_com_aumento)

    preco_com_reducao = package1Modulo.calculaPreco.reducao(preco, 15, formata=True)
    print(preco_com_reducao)
