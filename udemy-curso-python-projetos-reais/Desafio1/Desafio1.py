"""
Criar variáveis para nome (str), idade (int), altura (float) e peso (float) de uma pessoa.
Criar variável com o ano atual (int)
Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
Obter o IMC da pessoa com 2 casas decimais (peso e na altura pessoa)
Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)

Resultado para mostrar no console:
Luiz tem 32 anos, 1.8 de altura e pesa 80kg.
O IMC de Luiz é 24.69.
Luiz nasceu em 1987.
"""
if __name__ == '__main__':
    print('***** Desafio 1 *****')

    nome = 'José'
    idade = 30
    altura = 1.7
    peso = 70.69
    ano_atual = 2021
    ano_nascimento = 2021 - 30
    imc = peso / altura ** 2

    print(f'{nome} tem {idade} anos, {altura}m de altura e pesa {peso}kg.')
    print(f'O IMC de {nome} é {imc:.2f}.')
    print(f'{nome} nasceu em {ano_nascimento}.')
