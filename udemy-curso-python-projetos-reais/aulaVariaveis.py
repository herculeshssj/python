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

    # Aproveitando para incluir a função len()
    quantCaracteres = len(nome)
    print(f'{nome} tem {quantCaracteres} caracteres.')

    # Inverter valores entre variáveis
    x = 10
    y = 'João'
    print(f'Valor de x: {x}; Valor de y: {y}')

    # Modo clássico
    z = x
    x = y
    y = z
    print(f'Valor de x: {x}; Valor de y: {y}')

    # Modo Python de inversão de valores entre variáveis
    y, x = x, y
    print('Inversão de valores - modo Python')
    print(f'Valor de x: {x}; Valor de y: {y}')
