from funcionario import Funcionario, Gerente, Cliente, ControleDeBonificacoes

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
