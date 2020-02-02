if __name__ == '__main__':
    nome = input('Qual é o seu nome? ')
    idade = input('Qual é a sua idade? ')
    ano_nascimento = 2020 - int(idade)

    print()  # Pular uma linha
    print(f'{nome} tem {idade}.\n\r'
          f'{nome} nasceu em {ano_nascimento}.')
