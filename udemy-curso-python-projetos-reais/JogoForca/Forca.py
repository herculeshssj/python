if __name__ == '__main__':
    print('*******************************')
    print('* J O G O    D E    F O R C A *')
    print('*******************************')

    secreto = 'perfume'
    digitadas = []
    chances = 3

    while True:
        if chances <= 0:
            print('Você perdeu!')
            break

        letra = input('Digite uma letra: ')

        if len(letra) > 1:
            print('Ahhh isso não vale, digite apenas uma letra')
            continue

        digitadas.append(letra)

        if letra in secreto:
            print(f'UHUUUU, a letra "{letra}" existe na palavra secreta.')
        else:
            print(f'Aaaahhhhh, a letra "{letra}" NÃO EXISTE na palavra secreta.')
            digitadas.pop()

        secreto_temporatio = ''
        for letra_secreta in secreto:
            if letra_secreta in digitadas:
                secreto_temporatio += letra_secreta
            else:
                secreto_temporatio += '*'

        if secreto_temporatio == secreto:
            print(f'Que legal, VOCÊ GANHOU!!! A palavra era "{secreto_temporatio}"')
            break
        else:
            print(f'A palavra secreta está assim: {secreto_temporatio}')

        if letra not in secreto:
            chances -= 1

        print(f'Você ainda tem {chances} chances.')
        print()