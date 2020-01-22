class Funcionario:

    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    def get_bonificacao(self):
        return self._salario * 0.10


class Gerente(Funcionario):

    def __init__(self, nome, cpf, salario, senha, qtd_gerenciados):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_gerenciados = qtd_gerenciados

    def get_bonificacao(self):
        # return self._salario * 0.15
        return super().get_bonificacao() + 1000

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
    def __init__(self, total_bonificacoes = 0):
        self._total_bonificacoes = total_bonificacoes

    def registra(self, obj):
        if (hasattr(obj, 'get_bonificacao') or isinstance(obj, Funcionario)):
            self._total_bonificacoes +=funcionario.get_bonificacao()
        else:
            print('Instância de {} não implementa o método get_bonificacao()'.format(obj.__class__.__name__))

    @property
    def total_bonificacoes(self):
        return self._total_bonificacoes


class MinhaClasse:
    def __str__(self):
        return '< Instância de {}; endereço: {}'.format(self.__class__.__name__, id(self))


class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __repr__(self):
        return 'Ponto ({}, {})'.format(self.x + 1, self.y + 1)


if __name__ == '__main__':
    funcionario = Funcionario('João', '111.111.111-11', 2000)
    print('Funcionário: {}'.format(funcionario.nome))
    print('Bonificação: {}'.format(funcionario.get_bonificacao()))

    gerente = Gerente('Marcos', '222.222.222-22', 5000, 'abc123', 1)
    print('Gerente: {}'.format(gerente.nome))
    print('Bonificação: {}'.format(gerente.get_bonificacao()))

    cliente = Cliente('Joana', '333.333.333-33', '123456')

    controle = ControleDeBonificacoes()
    controle.registra(funcionario)
    controle.registra(gerente)
    controle.registra(cliente)
    print("Total de bonificações: {}".format(controle.total_bonificacoes))

    mc = MinhaClasse()
    print(mc)

    p1 = Ponto(1, 2)
    p2 = eval(repr(p1))
    print(p1)
    print(p2)
