'''
Faça um programa que pergunte a hora do usuário e, baseando-se no horário descrito, exiba a saudação apropriada. Ex.:
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
'''

if __name__ == '__main__':

    entrada = input('Oi :), que horas são (0 - 23)? ')

    hora = 0

    if entrada.isnumeric():

        hora = int(entrada)
        if hora >= 0 and hora <= 23:
            if hora >= 0 and hora <= 11:
                print('Oi, Bom dia :)')
            elif hora >= 12 and hora <= 17:
                print('Oi, Boa tarde :)')
            else:
                print('Oi, Boa noite :)')
        else:
            print('Desculpe, hora fora do intervalo :(')

    else:
        print('Desculpe, hora inválida :(')
