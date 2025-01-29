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


class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print("Data de abertura: {}".format(self.data_abertura))
        print("Transações: ")
        for t in self.transacoes:
            print("-", t)
