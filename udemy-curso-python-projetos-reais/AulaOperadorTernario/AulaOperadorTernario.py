"""
Operador ternário em Python
"""
if __name__ == '__main__':
    print('Operador ternário')
    logged_user = False

    if logged_user:
        print('Usuário logado.')
    else:
        print('Usuário não logado.')

    # Usando operador ternário
    answer = input('Deseja logar (S/N)? ')
    msg = 'Usuário logado.' if answer == 'S' else 'Usuário não logado'
    print(msg)