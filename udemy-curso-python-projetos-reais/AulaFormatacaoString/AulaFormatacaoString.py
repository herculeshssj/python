if __name__ == '__main__':
    print('Formataćão de strings')

    nome = 'José'
    idade = 30
    altura = 1.7
    e_maior = idade > 18
    data_atual = 2021
    peso = 80
    imc = peso / (altura ** 2)

    print(nome, 'tem', idade, 'e seu IMC é', imc)  # Sem F-Strings
    print(f'{nome} tem {idade} e seu IMC é {imc:.2f}')  # Com F-Strings
    print('{} tem {} anos de idades e seu IMC é {:.2f}'.format(nome, idade, imc))  # Funćão format()

    # Funćão format() usando parâmetros numéricos
    print('{0} tem {1} anos de idades e seu IMC é {2:.2f}'.format(nome, idade, imc))

    # Funćão format() usando parâmetros nomeados
    print('{n} tem {i} anos de idades e seu IMC é {im:.2f}'.format(n=nome, i=idade, im=imc))
