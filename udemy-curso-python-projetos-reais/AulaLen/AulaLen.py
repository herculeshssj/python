if __name__ == '__main__':
    print('len() - quantidade de caracteres')

    usuario = input('Digite seu usuário: ')
    quant_caracteres = len(usuario)
    print(usuario, quant_caracteres, type(quant_caracteres))

    if quant_caracteres < 6:
        print('Você precisa digitar pelo menos 6 caracteres.')
    else:
        print('Você foi cadastrado no sistema.')

    print()
    string1 = input('Digite alguma coisa: ')
    string2 = input('Digite outra coisa: ')
    print(f'Quantidade total de caracteres digitados: {len(string1) + len(string2)}')
