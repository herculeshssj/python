print('******************************')
print('*    Jogo da adivinhação     *')
print('******************************')

numero_secreto = 42
numero_de_tentativas = 3
rodada = 1

while (rodada <= numero_de_tentativas):
    print('Tentativa {} de {}'.format(rodada, numero_de_tentativas))
    chute = int(input('Digite o seu número: '))
    print('Você digitou: ', chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print('Você acertou!')
        break
    elif(maior):
        print('Você errou! O seu chute foi maior que o número secreto')
    elif(menor):
        print('Você errou! O seu chute foi menor que o número secreto')

    rodada = rodada + 1

print('Fim de jogo!')