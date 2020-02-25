"""
Desafio 10

A partir desta string '01234567890123456789012345678901234567890123456789'
Gerar a seguinte lista:
lista = ['0123456789', '0123456789', '0123456789', '0123456789', '0123456789']

E após isso gerar a segunte string

'0123456789.0123456789.0123456789.0123456789.0123456789'

Deve-se usar somente list comprehension

"""

if __name__ == '__main__':
    print('Desafio 10 - List Comprehension')

    string = '01234567890123456789012345678901234567890123456789'
    string = string.replace('0', '"0').replace('9', '9",')
    print(string)
    lista = list(string)
    print(*lista, type(lista))

    # Não consegui realizar o desafio... no dia não estava concentrado :-/

    """
    Solução
    
    string = '01234567890123456789012345678901234567890123456789'
    n = 10
    lista = [string[i:i + n] for i in range(0, len(string), n)]
    print(lista)
    retorno = '.'.join(lista)
    print(retorno)
     
    """

