"""
Módulos

Módulos padrão do Python:
Módulos são arquivos .py (que contém código Python) e servem para expandir as funcionalidades padrão da linguagem.
Veja todos os módulos padrão no Python em: https://docs.python.org/3/py-modindex.html
"""

# import sys # Importa tudo do módulo sys
# from sys import platform  # Importa somente a função do módulo
from sys import platform as so  # Usando alias
import random
from random import randrange, random  # importando mais de uma função

if __name__ == '__main__':
    print('Módulos')

    # print('Plataforma:', platform)
    # print('Plataforma:', sys.platform)
    print('Plataforma:', so)

    print(random.randint(0, 10))
