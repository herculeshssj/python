# Referência: https://docs.python.org/3/library/json.html

"""
JavaScript Object Notation - JSON
JSON  é um formato de troca de dados entre sistemas e programas muito leve e de fácil utilização.
Muito utilizado por APIs.
"""

"""
DUMPS / Dump
#######################
Python          JSON
dict            object
list,tuple      array
str             string
int, float      number
True            true
False           false
None            null

LOADS / Load
#######################
JSON            Python
object          dict
array           list
string          str
number (int)    int
number (real)   float
true            True
false           False
null            None
"""

import json
from dados_json.dados import clientes_dicionario, clientes_json

if __name__ == '__main__':
    print('Aula Json')

    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    dados_json = json.dumps(lista)
    print(dados_json)
    print(type(dados_json))

    dados_json = json.dumps(clientes_dicionario, indent=4)
    print(dados_json)
    print(type(dados_json))

    print(clientes_json)
    dicionario = json.loads(clientes_json)
    for chave, valor in dicionario.items():
        print(chave)
        print(valor)

    with open('clientes.json', 'w') as arquivo:
        json.dump(clientes_dicionario, arquivo, indent=4)

    with open('clientes.json', 'r') as arquivo:
        data = json.load(arquivo)

    print(data)
    print()

    for chave, valor in data.items():
        print(chave)
        print(valor)
