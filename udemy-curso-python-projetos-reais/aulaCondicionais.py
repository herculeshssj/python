from libs.chk_numbers import is_number

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
    idadeStr = input('Qual a sua idade? ')
    idade = 0

    # Verifica se a idade é numérica
    if is_number(idadeStr):
        idade = int(idadeStr)

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
    else:
        print('Idade informada não é um número válido!')

    # Aproveitando a aula da função len()
    print(f'Total de caracteres: {len(nome)}')
    print(f'Total de caracteres (usando o __len__()): {nome.__len__()}')

    # Operador ternário
    senha = input('Informe a senha (123456): ')
    print('Usuário logado' if int(senha) == 123456 else 'Usuário não logado')
