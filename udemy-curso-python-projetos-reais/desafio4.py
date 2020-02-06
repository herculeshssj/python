'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto";
se tiver 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreve "Seu nome é muito grande".
'''

if __name__ == '__main__':

    nome = input('Informe seu nome: ')

    if len(nome) <= 4:
        print('Seu nome é curto XD')
    elif len(nome) > 4 and len(nome) <= 6:
        print('Seu nome é normal :)')
    else:
        print('Seu nome é muito grande :O')
