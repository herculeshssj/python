if __name__ == '__main__':
    print('Iterando strings com while')

    frase = 'o rato roeu a roupa do rei de roma.'  # Valor iterável
    tamanho_frase = len(frase)
    contador = 0
    nova_string = ''
    print(f'Frase: {frase}')
    print(f'Tamanho: {tamanho_frase}')
    while contador < tamanho_frase:  # Iteraćão
        print(f'Letra: {frase[contador]} - índice: {contador}')
        contador += 1

    print()
    contador = 0
    while contador < tamanho_frase:
        print(f'Nova string: {nova_string}')
        nova_string += frase[contador]
        contador += 1
    print(f'Nova string: {nova_string}')

    print('*** Exercício ***')
    print(f'Frase: {frase}')
    input_do_usuario = input('Qual letra deseja colocar em maiúscula? ')
    contador = 0
    nova_string = ''
    while contador < tamanho_frase:
        letra = frase[contador]
        if letra == input_do_usuario:
            nova_string += input_do_usuario.upper()
        else:
            nova_string += letra
        contador += 1
    print(f'Nova frase: {nova_string}')
