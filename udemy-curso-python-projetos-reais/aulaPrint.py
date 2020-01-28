if __name__ == '__main__':
    print('Olá', 'mundo')

    # Parâmetro 'sep' define um separador entre os argumentos passados para a função print()
    print('Olá', 'mundo', sep='-')

    # Parâmetro 'end' define um caractere de fim de linha
    print('Olá', 'mundo', end='#')
    print('')

    # Imprimindo um CPF formatado
    print('307', '367', '385', sep='.', end='-')  # Número principal
    print('76')  # Dígito verificador

    # Caracter de escape
    print('Uso de caracteres de \'escape\'')

    # Quebra de linha
    print('Este é um exemplo \n para quebra de linha')

    # Texto em formato raw
    print(r'Este texto está em formato \'row\'')
