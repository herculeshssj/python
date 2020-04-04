from datetime import datetime


class Pessoa:

    # Atributo de classe
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    # Construtor da classe
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        # print('Objeto instanciado!')

    # Método de instância
    def falar(self):
        if self.falando:
            print(f'{self.nome} já está falando...')
        elif self.comendo:
            print(f'{self.nome} está comendo...')
        else:
            self.falando = True
            print(f'{self.nome} está falando...')

    # Método de instância
    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo...')
        elif self.falando:
            print(f'{self.nome} não pode comer agora, ele está falando...')
        else:
            self.comendo = True
            print(f'{self.nome} está comendo {alimento}...')

    # Método de instância
    def parar_falar(self):
        if self.falando:
            self.falando = False
            print(f'{self.nome} parou de falar...')
        elif self.comendo:
            print(f'{self.nome} está comendo...')
        else:
            print(f'{self.nome} não está falando...')

    # Método de instância
    def get_ano_nascimento(self):
        return self.ano_atual - self.idade

    """
    Método de classe

    Abaixo exemplo de factory method
    """
    @classmethod
    def create_pessoa_por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
