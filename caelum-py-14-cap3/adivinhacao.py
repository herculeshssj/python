intNumero = 42
intChute = int(input('Digite um número: '))

#if (intNumero == intChute):
#    print('Você acertou')
#elif (intChute > intNumero):
#    print('Você errou! O seu chute é maior que o número secreto!')
#elif (intChute < intNumero):
#    print('Você errou! O seu chute é menor que o número secreto!')

# Segundo implementação do if
boolAcertou = intChute == intNumero
boolMaior = intChute > intNumero
boolMenor = intChute < intNumero
if (boolAcertou):
    print('Você acertou!')
elif (boolMaior):
    print('Você errou! O seu chute foi maior que o número secreto')
elif (boolMenor):
    print('Você errou! O seu chute foi menor que o número secreto')