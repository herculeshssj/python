if __name__ == '__main__':
    print('Aula condicionais - IF, ELIF, ELSE')

    if True:
        print('Verdadeiro')
    else:
        print('Falso')

    if False:
        print('Verdadeiro')
    print('Falso')

    # Operadores de comparação
    # == igual
    # > maior
    # >= maior igual que
    # < menor
    # <= menor igual que
    # != diferente

    # Operadores lógicos
    # and
    # or
    # not
    # in

    if 2 == '2':
        print('São iguais')
    else:
        print('São diferentes')

    a = ''
    b = 0
    if not a:
        print('Por favor informe um valor para a')

    if not b:
        print('Por favor informe um valor para b')

    nome = input('Qual é o seu nome? ')
    idade = int(input('Qual a sua idade? '))

    print(f'Seu nome é {nome}.\n\r')
    if idade >= 18:
        print(f'{nome} é maior de idade.')
    elif idade < 0:
        print(f'Idade não determinada!')
    else:
        print(f'{nome} é menor de idade.')

    idade_minima = 20
    idade_maxima = 30

    if idade >= idade_minima and idade <= idade_maxima:
        print(f'{nome} pode pegar o empréstimo.')
    else:
        print(f'{nome} não pode pegar o empréstimo.')

    if 'a' in nome or 'e' in nome or 'i' in nome or 'o' in nome or 'u' in nome:
        print(f'{nome}, seu nome possui vogais.')
    else:
        print(f'{nome}, seu nome não possui vogais.')
