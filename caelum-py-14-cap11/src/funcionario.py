import abc
from autenticacao import Autenticavel

class Funcionario(abc.ABC):

    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @abc.abstractmethod
    def get_bonificacao(self):
        pass


class Secretario(Funcionario):

    def __init__(self, nome, cpf, salario):
        super().__init__(nome, cpf, salario)

    def get_bonificacao(self):
        return self._salario * 0.10


class Diretor(Funcionario):

    def __init__(self, nome, cpf, salario):
        super().__init__(nome, cpf, salario)

    def get_bonificacao(self):
        return self._salario * 0.50


class Gerente(Funcionario):

    def __init__(self, nome, cpf, salario, senha, qtd_gerenciados):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_gerenciados = qtd_gerenciados

    def get_bonificacao(self):
        return (self._salario * 0.15) + 1000

    def autentica(self, senha):
        if self._senha == senha:
            print("Acesso permitido")
            return True
        else:
            print("Acesso negado")
            return False


class Cliente:
    def __init__(self, nome, cpf, senha):
        self._nome = nome
        self._cpf = cpf
        self._senha = senha


class ControleDeBonificacoes:
    def __init__(self, total_bonificacoes=0):
        self._total_bonificacoes = total_bonificacoes

    def registra(self, obj):
        if (hasattr(obj, 'get_bonificacao') or isinstance(obj, Funcionario)):
            self._total_bonificacoes += obj.get_bonificacao()
        else:
            print('Instância de {} não implementa o método get_bonificacao()'.format(obj.__class__.__name__))

    @property
    def total_bonificacoes(self):
        return self._total_bonificacoes


class SistemaInterno:

    def login(self, obj):
        if isinstance(obj, Autenticavel):
            obj.autentica(obj.senha)
            return True
        else:
            print("{} não é autenticável".format(self.__class__.__name__))
            return False
