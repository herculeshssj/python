"""
https://rszalski.github.io/magicmethods/
"""


class A:
    # Construtor
    def __new__(cls, *args, **kwargs):
        print('Método mágico NEW')
        return super().__new__(cls)

    # Inicializador
    def __init__(self):
        print('Método mágico INIT')

    def __call__(self, *args, **kwargs):
        print('Método mágico CALL')
        print(args)
        print(kwargs)

    def __setattr__(self, name, value):
        print('Método mágico SETATTR')
        if name == 'idade':
            print('Você não pode setar a idade!')
        else:
            self.__dict__[name] = value

    def __del__(self):
        print('Método mágico DEL')
        print('Objeto coletado')

    def __str__(self):
        print('Método mágico STR')
        return 'Class <A>'

    def __len__(self):
        print('Método mágico LEN')
        return 55


if __name__ == '__main__':
    print('Métodos mágicos')

    a = A()
    a(1, 2, 3, 4, 5, nome='João')

    a.nome = 'João'
    print(a.nome)
    a.idade = 30
    # print(a.idade)
    print(a)
    print('Tamanho da classe:', len(a))
