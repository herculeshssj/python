print('Hello World')
print(2)
print(type('Hello World'))  # tipo string
print(type(2))  # tipo inteiro
print(type(3.2))  # tipo float
print(type('2'))  # string que representa o algarismo 2
print(type('3.2'))  # string que representa o número real 3.2

# Números complexos. A parte imaginário é indicada pela letra 'j'
print(type(2 + 3j))  # número complexo

# Atribuição de variável
mensagem = 'Oi Python'
print(mensagem)
numero = 5
print(numero)
pi = 3.14
print('Número PI: ', pi)

# Sou desenvolvedor Java, portanto seguirei adotando o camelCase para nomes de classes, métodos, atributos e variáveis.

intX = 10
intY = 5
print('Soma: ', intX + intY)
print('Subtração: ', intX - intY)
print('Multiplicação: ', intX * intY)
print('Divisão: ', intX / intY)
print('Potenciação: ', intX ** intY)
intY += 1
print('Divisão inteira: ', intX // intY)
print('Resto (módulo): ', intX % intY)

# Concatena strings
strTexto1 = 'oi'
strTexto2 = 'python'
print(strTexto1 + strTexto2)

# Duplica string multiplicando seu conteúdo pelo valor informado
print(strTexto2 * 3)

# Tudo em maiúsculo
print(strTexto2.upper())

# Primeira letra em maiúsculo
print(strTexto2.capitalize())

# Tipo None
print(type(None))

# No interpretador CPython o sinal '=' compara valores, enquanto o 'is' compara referências
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)

# While
x = 5
while (x >= 1):
    print(x)
    x = x - 1

print('')

#For
for rodada in range(1,11):
    print(rodada)