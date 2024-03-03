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
    sobrenome = 'Silva'

    print('Nome:', nome)
    print('Sobrenome', sobrenome)
    print('Idade:', idade)
    print('Altura:', altura)
    print('É maior de idade:', e_maior)

    # Exercício
    print(nome, sobrenome, 'tem', idade, 'e seu IMC é', peso / (altura ** 2), sep=" ")
    # Usando sep= para poder separar os valores com espaço.

    print()
    # Inversão de valores entre variáveis
    x = 10  # Luiz
    y = 'Luiz'  # 10
    """
    Troca de valores nas linguagens de programação
    z = x
    x = y
    y = z
    """
    # Troca de valores no Python
    print('Troca de valores de variáveis')
    print(f'Valor de X: {x}; Valor de Y: {y}')
    x, y = y, x
    print(f'Valor de X: {x}; Valor de Y: {y}')
    # Hiper fácil trocar valores de variáveis em Python XD

    # Identidade de uma variável
    v1 = 'a'
    v2 = 'a'
    print(id(v1))
    print(id(v2))