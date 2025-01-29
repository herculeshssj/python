import datetime


class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf


class Conta:
    def __init__(self, numero, titular, saldo, limite=1000):
        # print("Inicializando uma conta...")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite  # valor padrão: 1000.0
        self.historico = Historico()

    def __init__(self, numero, cliente, saldo, limite=1000):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite  # valor padrão: 1000.0
        self.historico = Historico()

    def __str__(self):
        return '< Instância de {}; endereço: {}'.format(self.__class__.__name__, id(self))

    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append("Depósito de {}".format(valor))

    def saca(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append("Saque de {}".format(valor))
            return True

    def extrato(self):
        print("Número: {} \nSaldo: {}".format(self.numero, self.saldo))
        self.historico.transacoes.append("Tirou extrato - saldo {}".format(self.saldo))

    def transfere_para(self, conta_destino, valor):
        retirou = self.saca(valor)
        if (retirou == True):
            conta_destino.deposita(valor)
            self.historico.transacoes.append("Transferência de {} para conta {}".format(valor, conta_destino.numero))
            return True
        else:
            return False

    def atualiza(self, taxa):
        self.saldo += self.saldo * taxa


class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print("Data de abertura: {}".format(self.data_abertura))
        print("Transações: ")
        for t in self.transacoes:
            print("-", t)


class ContaCorrente(Conta):
    def atualiza(self, taxa):
        self.saldo += self.saldo * taxa * 2

    def deposita(self, valor):
        self.saldo += valor - 0.10
        self.historico.transacoes.append("Depósito de {}".format(valor))


class ContaPoupanca(Conta):
    def atualiza(self, taxa):
        self.saldo += self.saldo * taxa * 3


class ContaInvestimento(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 5


class AtualizadorDeContas:

    def __init__(self, selic, saldo_total=0):
        self._selic = selic
        self._saldo_total = saldo_total

    @property
    def saldo_total(self):
        return self._saldo_total

    def roda(self, conta):
        # Imprime o saldo anterior, atualiza a conta e depois imprime o saldo final
        # Soma o saldo final ao atributo saldo_total
        print('Saldo anterior: {}'.format(conta.saldo))
        conta.atualiza(self._selic)
        print('Saldo atual: {}'.format(conta.saldo))
        self._saldo_total += conta.saldo
