from funcionario import Gerente, Cliente, ControleDeBonificacoes, Secretario, Diretor
from autenticacao import Autenticavel
from conta import Conta, ContaCorrente, ContaPoupanca, AtualizadorDeContas

if __name__ == '__main__':
    funcionario = Secretario('João', '111.111.111-11', 2000)
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

    c = Conta('123-4', 'Joao', 1000.0)
    cc = ContaCorrente('123-5', 'Jose', 1000.0)
    cp = ContaPoupanca('123-6', 'Maria', 1000.0)

    c.atualiza(0.01)
    cc.atualiza(0.01)
    cp.atualiza(0.01)

    print(c.saldo)
    print(cc.saldo)
    print(cp.saldo)

    print(c)
    print(cc)
    print(cp)

    adc = AtualizadorDeContas(0.01)

    adc.roda(c)
    adc.roda(cc)
    adc.roda(cp)

    print('Saldo total: {}'.format(adc.saldo_total))

    Autenticavel.register(Diretor)
    d = Diretor('José', '22222222-22', 3000.0)
    # d.autentica('?')
    if isinstance(d, Autenticavel):
        d.autentica('?')
    else:
        print("Diretor não implementa a interface Autenticavel")
