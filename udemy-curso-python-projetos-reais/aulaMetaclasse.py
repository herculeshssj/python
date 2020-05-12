"""
Aula metaclasse

Em Python tudo é um objeto: incluindo classes
Metaclasses são as "classes" que criam classes.
type é uma metaclasse
"""


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        print(name)

        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)

        print(namespace)

        if 'b_fala' not in namespace:
            print(f'Método "b_fala" não foi implementado em {name}!')
        else:
            if not callable(namespace['b_fala']):
                print(f'b_fala precisa ser um método em {name}!')

        if 'attr_classe' in namespace:
            print(f'{name} tentou sobrescrever o atributo')
            del namespace['attr_classe']

        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):

    attr_classe = 'Valor A'

    def fala(self):
        self.b_fala()


class B(A):

    attr_classe = 'Valor B'

    #b_fala = 'Woow'

    def sei_la(self):
        pass

    def b_fala(self):
        print('Oi')


class C(B):
    attr_classe = 'Valor C'


class Pai:
    nome = 'Teste'


if __name__ == '__main__':
    print('Metaclasses')

    b = B()
    b.fala()

    print(b.attr_classe)

    c = C()
    print(c.attr_classe)

    D = type('D',  # nome da classe
             (Pai, ),  # classes que 'D' herda
             {'attr': 'Olá mundo D'}  # atributos da classe
             )

    d = D()
    print(d.attr)
    print(type(d))
    print(d.nome)
