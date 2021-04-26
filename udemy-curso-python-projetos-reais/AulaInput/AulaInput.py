if __name__ == '__main__':
    print('Input - entrada de dados')

    nome = input('Qual é o seu nome? ')
    print('Seu nome é', nome)
    print(f'O tipo de variável é {type(nome)}')
    print()

    # Input sempre retorna string (str)
    # Precisa colocar um espaćo na mensagem do input para não ficar colado com texto digitado

    nome = input('Qual o seu nome? ')
    idade = input('Qual sua idade? ')
    ano_nascimento = 2021 - int(idade)  # cast
    print()
    print(f'{nome} tem {idade} anos.')
    print(f'{nome} tem {idade} anos e nasceu em {ano_nascimento}.')
    print()

    # Calculadora de soma
    print('##### Calculadora de soma #####')
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    print(f'A soma de {numero_1} com {numero_2} dá {numero_1 + numero_2}.')
    print(f'A soma de {numero_1} com {numero_2} dá {int(numero_1) + int(numero_2)}.')  # Fazendo cast de valores
