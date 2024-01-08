"""
Tipos de dados primitivos

str - string
int - inteiro
float - real/ponto flutuante
bool - booleano
"""
if __name__ == '__main__':
    print('Tipos de dados primitivos', end='\r\n\r\n')

    print('Isto aqui é uma string', type('Isto aqui é uma string'))  # str
    print('Isto aqui é um número inteiro:', 123456, type(123456))  # int
    print('Isto aqui é um número real:', 123456.789, type(123456.789))  # float
    print('Isto aqui é um booleano:', 10 == 10, type(10 == 10))  # bool

    # Para strings, posso utilizar tanto aspas simples quanto aspas duplas
    print('José')
    print("José")

    # Caracter de escape
    print('José Sant\'Ana')

    # r
    print(r'José Sant\'Ana')

    print('Posso usar "aspas" na string, para deixar o código mais limpo')

    # o 'r' é usado mais para expressões regulares

    # String vazia, valor zero retorna falso ou dicionários vazios
    print(bool(''), bool(0))

    # Type casting
    print('jose', type('jose'), bool('jose'))
    print('10', type('10'), type(int('10')))
    print('10', type('10'), type(float('10')))

    # Exercício
    print('#### Exercício ####')
    # Nome
    print('José', type('José'))
    # Idade
    print(30, type(30))
    # Altura
    print(1.7, type(1.7))
    # É maior de idade
    print(30 > 18, type(30 > 18))
