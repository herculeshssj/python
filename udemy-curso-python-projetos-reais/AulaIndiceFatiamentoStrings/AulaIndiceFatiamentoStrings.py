"""
Manipulando strings
* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funćões built-in len, abs, type, print, etc...
Essas funćões podem ser usadas diretamente em cada tipo.

Você pode conferir tudo isso em:
https://docs.python.org/3/library/functions.html
https://docs.python.org/3/library/stdtypes.html
"""

if __name__ == '__main__':
    print('Índices e fatiamento de strings em Python')

    texto = 'Python_s2'
    # Acessando índices positivos [012345678]
    print(f'Acessando o índice 2 da string: {texto[2]}') # Mostrando o caractere no índice 2 da string
    # Acessando índices negativos -[987654321]
    print(f'Acessando o índice -2 da string: {texto[-2]}')  # Mostrando o caractere no índice -2 da string

    # Fatiamento de strings
    nova_string = texto[2:6] # De 2 até 6
    print(f'String da posićão 2 até a posićão 6: {nova_string}')
    nova_string = texto[:6]  # Todos os caracteres até a posićão 6
    print(f'Todos os caracteres até a posićão 6: {nova_string}')
    nova_string = texto[7:]  # Todos os caracteres a partir da posićão 7
    print(f'Todos os caracteres a partir da posićão 7: {nova_string}')
    # Funciona com os índices negativos também

    # Usando passo no fatiamento de string
    nova_string = texto[0:6:2]  # Comeća do índice 0 até o 6, a cada 2 passos
    print(f'Comeća do índice 0 até o 6, a cada 2 passos: {nova_string}')
    nova_string = texto[0::3]  # Comeća do índice 0 até o fim da string, a cada 2 passos
    print(f'Comeća do índice 0 até o fim da string, a cada 2 passos: {nova_string}')


