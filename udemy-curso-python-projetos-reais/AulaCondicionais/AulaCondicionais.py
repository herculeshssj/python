if __name__ == '__main__':
    print('Condicionais - IF, ELIF, ELSE, operadores relacionais e operadores lógicos')

    if False:
        print('Verdadeiro')
    elif True:
        print('Agora é verdadeiro')
    elif False:
        print('Mais uma verdadeira')
    else:
        print('Falso')

    """
    Operadores relacionais
    == > >= < <= !=
    """
    # Igualdade
    print(f'Igualdade: 2 == 2 -> {2 == 2}')

    # Maior que
    print(f'Maior que: 2 > 2 -> {2 > 2}')

    # Maior ou igual que
    print(f'Maior ou igual que: 2 >= 2 -> {2 >= 2}')

    # Menor que
    print(f'Menor que: 2 < 2 -> {2 < 2}')

    # Menor ou igual que
    print(f'Menor ou igual que: 2 <= 2 -> {2 <= 2}')

    # Diferenća
    print(f'Diferenća: 2 != 2 -> {2 != 2}')

    print()
    print('***** Exercício *****')
    nome = input('Qual é seu nome? ')
    idade = input('Qual a sua idade? ')

    # Cast
    idade = int(idade)

    # Limite para pegar empréstimo
    idade_limite = 18

    if idade >= idade_limite:
        print(f'{nome} pode pegar o empréstimo.')
    else:
        print(f'{nome} não pode pegar o empréstimo.')
