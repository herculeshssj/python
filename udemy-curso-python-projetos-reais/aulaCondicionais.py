if __name__ == '__main__':
    print('Aula condicionais - IF, ELIF, ELSE')

    if True:
        print('Verdadeiro')
    else:
        print('Falso')

    if False:
        print('Verdadeiro')
    print('Falso')

    # Operadores lógicos
    # == igual
    # > maior
    # >= maior igual que
    # < menor
    # <= menor igual que
    # != diferente

    if 2 == '2':
        print('São iguais')
    else:
        print('São diferentes')

    nome = input('Qual é o seu nome? ')
    idade = int(input('Qual a sua idade? '))

    print(f'Seu nome é {nome}.\n\r')
    if idade >= 18:
        print(f'{nome} é maior de idade.')
    elif idade < 0:
        print(f'Idade não determinada!')
    else:
        print(f'{nome} é menor de idade.')
