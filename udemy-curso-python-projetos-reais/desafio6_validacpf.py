"""
Desafio 6 - Valida CPF
"""

if __name__ == '__main__':

    # Declaração das variáveis globais
    nome = ''
    cpf = ''

    # Loop while que pede o nome e o CPF do usuário
    while True:
        # Solicita o nome do usuário
        nome = input('Informe seu nome: ')

        # Solicita o CPF do usuário
        cpf = input('Informe seu CPF (formato: 999.999.999-99): ')

        # Verifica se o usuário informou o nome e o CPF
        if not nome:
            print('Nome não infomado!')
            continue
        elif not cpf:
            print('CPF não informado!')
            continue

        # Faz a limpeza do CPF
        cpf = cpf.replace('.', '').replace('-', '')

        # Verifica se nenhum outro caractere foi digitado no CPF
        if not cpf.isnumeric():
            print('CPF deve conter somente números!')
            continue
        elif len(cpf) != 11:
            print('CPF deve conter 11 números!')
            continue
        else:
            # CPF prontro para validar
            break

    # Guardando os nove primeiros números do CPF informado
    cpf_validado = cpf[0:9]

    # Variável que guardará a soma dos valores do CPF
    soma_numeros_cpf = 0

    # Índice
    indice = 10

    # Itera o CPF para realizar a primeira parte do cálculo
    for numero in cpf_validado:
        soma_numeros_cpf += int(numero) * indice
        indice -= 1

    # Calcula o primeiro dígito verificador
    dv1 = 11 - (soma_numeros_cpf % 11)
    if dv1 > 9:
        cpf_validado += '0'
    else:
        cpf_validado += str(dv1)

    # Zera as variáveis auxiliares
    soma_numeros_cpf = 0
    indice = 11

    # Itera o CPF validado para realizar a segunda parte do cálculo
    for numero in cpf_validado:
        soma_numeros_cpf += int(numero) * indice
        indice -= 1

    # Calcula o segundo dígito verificador
    dv2 = 11 - (soma_numeros_cpf % 11)
    if dv2 > 9:
        cpf_validado += '0'
    else:
        cpf_validado += str(dv2)

    # Verifica se o CPF gerado é idêntico ao CPF informado
    if cpf == cpf_validado:
        print('O CPF informado é válido!')
    else:
        print('O CPF informado não é válido!')
