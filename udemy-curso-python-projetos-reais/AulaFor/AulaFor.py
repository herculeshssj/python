"""
For in em Python
Iterando strings com for
Funćão range(start=0, stop, step=1)
"""
if __name__ == '__main__':
    print('Aula - For in e For/Else')
    texto = 'Python'
    for letra in texto:
        print(letra)
    print()
    # Funćão built-in range()
    for numero in range(1, 11, 1):
        print(numero)
    print()
    # Iterando o range() de trás para frente
    for numero in range(20, 9, -1):
        print(numero)
    print()
    # Imprimindo números múltiplos de 3
    for numero in range(0, 100, 3):
        print(numero)

    # For aceita break e continue, e funcionam da mesma forma que o while

    print()

    print('***** Exercício *****')
    frase = 'o rato roeu a roupa do rei de roma.'  # Valor iterável
    print(f'Frase: {frase}')
    input_do_usuario = input('Qual letra deseja colocar em maiúscula? ')
    nova_string = ''
    for letra in frase:
        if letra.upper() == input_do_usuario.upper(): # Padronizando os caracteres para facilitar na comparaćão
            nova_string += input_do_usuario.upper()
        else:
            nova_string += letra

    print(f'Nova frase: {nova_string}')
    print()

    print('*** For / Else ***')
    variavel = ['Huguinho', 'Zezinho', 'Luizinho']
    for valor in variavel:
        if valor.lower().startswith('z'):
            print(f'{valor} comeća com "z"')
    else:
        print('Não foi encontrado mais nomes que comećam com "z"')