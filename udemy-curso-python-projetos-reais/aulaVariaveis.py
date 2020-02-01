'''
Uso de variáveis. Calculando o Índice de Massa Corpórea (IMC)
'''

if __name__ == '__main__':
    nome = 'João'
    idade = 30
    altura = 1.75
    peso = 70
    e_maior_idade = idade > 18
    imc = peso / altura ** 2

    print(nome, 'tem', idade, 'anos e seu IMC é', imc)
