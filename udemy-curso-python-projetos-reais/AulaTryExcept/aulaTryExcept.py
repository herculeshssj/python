"""
Introdução ao try/except

try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

if __name__ == '__main__':
    print('Aula try..except')

    print(123)
    print(456)
    # int('a')

    numero = input('Vou dobrar o número que você digitar: ')

    print(numero.isdigit()) # Verifica se o usuário informou somente números

    numero_float = float(numero)
    print(f'O dobro de {numero} é {numero_float * 2:.0f}')

    try:
        pass
    except:
        pass