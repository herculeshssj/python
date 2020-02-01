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

    # Formatando a saída com F-String
    print("Usando F-String...")
    print(f'{nome} tem {idade} anos e seu IMC é {imc:.2f}')
    print("Usando a função 'format()'")
    print('{0} tem {1} anos e seu IMC é {2}'.format(nome, idade, imc))  # Pode usar índice nas chaves
    print('{a} tem {b} anos e seu IMC é {c}'.format(a=nome, b=idade, c=imc))  # Pode usar parâmetros nomeados

