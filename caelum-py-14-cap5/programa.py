def velocidade(espaco, tempo):
    v = espaco / tempo
    print('velocidade: {} m/s'.format(v))
    return v

# velocidade(100,20)
aceleracao = velocidade(100,20) / 20
print('aceleracao: {}'.format(aceleracao))

def diz_oi():
    print('oi')

diz_oi()

def dados(nome, idade = None):
    print('nome: {}'.format(nome))
    if (idade is not None):
        print('idade: {}'.format(idade))
    else:
        print('idade não informada')

dados('João', 20)
dados('João')

def calculadora(x,y):
    return x+y, x-y, x*y, x/y

print(calculadora(10,20))


def teste(arg, *args):
    print('primeiro argumento normal: {}'.format(arg))
    for arg in args:
        print('outro argumento: {}'.format(arg))


teste('python', 'é', 'muito', 'legal')
lista = ["é", "muito", "legal"]
teste('python', *lista)
tupla = ("é", "muito", "legal")
teste('python', *tupla)

def minha_funcao(**kwargs):
    for key, value in kwargs.items():
        print('{0} = {1}'.format(key, value))

minha_funcao(nome='caelum')

dicionario = {'nome': 'joao', 'idade': 25}
minha_funcao(**dicionario)