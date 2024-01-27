"""
Interpolação básica de strings

s- string
d e i - int
f - float
x e X - Hexadecimal (0123456789ABCDEF)
"""

if __name__ == '__main__':
    print('Interpolação de strings')

    nome = 'Luiz'
    preco = 1000.3823923898293
    variavel = '%s, o preço é R$ %.2f' % (nome, preco)
    print(variavel)

    # Valores hexadecimal
    print('O hexadecimal de %d é %04x' % (15,15))