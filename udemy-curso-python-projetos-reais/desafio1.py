'''
Desafio 1
* Criar variáveis para nome (str), idade(int), altura (float) e peso (float) de uma pessoa;
* Criar variável com o ano atual (int);
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual);
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa);
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves).


Saída no terminal:

Luiz tem 32 anos, 1.8 de altura e pesa 80kg.
O IMC de Luiz é 24.69.
Luiz nasceu em 1987.
'''

if __name__ == '__main__':
    nome = 'João da Silva'
    idade = 35
    altura = 1.73
    peso = 85
    ano_atual = 2020
    ano_nascimento = ano_atual - idade
    imc = peso / altura ** 2

    # Imprimindo os valores no console
    print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.')
    print(f'O IMC de {nome} é {imc:.2f}.')
    print(f'{nome} nasceu em {ano_nascimento}.')
