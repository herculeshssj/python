"""
Variáveis em Python iniciam com letra, pode conter números, separar com (_), letras minúsculas
Variáveis não podem iniciar com números
"""

if __name__ == '__main__':
    print('Variáveis em Python')
    nome = 'José'
    print(nome, type(nome))

    idade = 30
    altura = 1.7
    e_maior = idade > 18
    data_atual = 2021
    peso = 80

    print('Nome:', nome)
    print('Idade:', idade)
    print('Altura:', altura)
    print('É maior de idade:', e_maior)

    # Exercício
    print(nome, 'tem', idade, 'e seu IMC é', peso / (altura**2))


