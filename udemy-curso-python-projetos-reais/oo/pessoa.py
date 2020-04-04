from datetime import datetime


class Pessoa:

    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        # print('Objeto instanciado!')

    def falar(self):
        if self.falando:
            print(f'{self.nome} já está falando...')
        elif self.comendo:
            print(f'{self.nome} está comendo...')
        else:
            self.falando = True
            print(f'{self.nome} está falando...')

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo...')
        elif self.falando:
            print(f'{self.nome} não pode comer agora, ele está falando...')
        else:
            self.comendo = True
            print(f'{self.nome} está comendo {alimento}...')

    def parar_falar(self):
        if self.falando:
            self.falando = False
            print(f'{self.nome} parou de falar...')
        elif self.comendo:
            print(f'{self.nome} está comendo...')
        else:
            print(f'{self.nome} não está falando...')

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
