"""
Funćões built-in: https://docs.python.org/3/library/stdtypes.html
"""

"""
import re
 
def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True
 
    return False
 
def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True
 
    return False
 
def is_number(val):
    return is_int(val) or is_float(val)
 
###########
#  USAGE  #
###########
 
# Float
print(is_float('-101.0112'))  # True
# Int
print(is_int('-1010112'))  # True
# Numbers in general (float ou int)
print(is_number('-1010.112'))  # True
 
# False
print(is_number('123a'))  # False
"""

import re


def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False


def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False


def is_number(val):
    return is_int(val) or is_float(val)


if __name__ == '__main__':
    print('Documentaćão e funćões built-in')

    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')

    # num1 = int(num1)
    # num2 = int(num2)
    # String methods: isnumeric(), isdigit(), isdecimal()
    # Verifica se a string possui somente números, não funciona quando coloco sinal negativo
    # ou ponto decimal
    if num1.isdecimal() and num2.isdecimal():
        num1 = int(num1)
        num2 = int(num2)
        print(num1 + num2)
    else:
        print('Não pude converter os números para realizar contas')

    """
    Solućões:
    - uso das funćões criadas pelo professor
    - bloco try...except
    """
    print('Usando as funćões criadas pelo professor')
    if is_number(num1) and is_number(num2):
        num1 = int(num1)
        num2 = int(num2)
        print(num1 + num2)
    else:
        print('ERROR!')
