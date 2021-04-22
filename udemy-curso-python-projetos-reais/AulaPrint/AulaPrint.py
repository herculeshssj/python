if __name__ == '__main__':
    print('Funcão print()')

    print('Hello World')
    print(123456)

    print('José', 'Silva') # Vai imprimir os dois argumentos separados por espaćo

    print('José', 'Silva', sep='-') # Uso de separador na funćão print()

    print('João', 'e', 'Maria', sep='-', end='') # parâmetro end informa o caracter de final de linha
    print('Bento')

    # parâmetro end informa o caracter de final de linha
    # usando um valor definido para separar as linhas
    print('João', 'e', 'Maria', sep='-', end=' - ')
    print('Bento')

    # Formatando um CPF
    # Número: 79650150994
    print('Formatando um CPF')
    print('796', '501', '509', sep='.', end='-')
    print('94')