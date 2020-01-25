from collections import UserDict, defaultdict, Counter, deque, namedtuple
from collections.abc import MutableSequence
import csv


class Funcionario:
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    @property
    def salario(self):
        return self._salario

    def get_bonificacao(self):
        return float(self._salario) * 0.10


class Funcionarios(MutableSequence):

    _dados = []

    def __len__(self):
        return len(self._dados)

    def __getitem__(self, posicao):
        return self._dados[posicao]

    def __setitem__(self, posicao, valor):
        if isinstance(valor, Funcionario):
            self._dados[posicao] = valor
        else:
            raise ValueError('Valor atribuído não é um Funcionario')

    def __delitem__(self, posicao):
        del self._dados[posicao]

    def insert(self, posicao, valor):
        if isinstance(valor, Funcionario):
            return self._dados.insert(posicao, valor)
        else:
            raise ValueError('Valor atribuído não é um Funcionario')


class Pins(UserDict):

    def __contains__(self, key):
        return str(key) in self.keys()

    def __setitem__(self, key, value):
        self.data[str(key)] = value


if __name__ == '__main__':
    print('Collections in Python')

    pins = Pins(one=1)
    print(pins)
    pins[3] = 1
    print(pins)
    lista = [1, 2, 3]
    pins.__setitem__(lista, 2)
    print(pins)

    cores = [('1', 'azul'), ('2', 'amarelo'), ('3', 'vermelho'), ('1', 'branco'), ('3', 'verde')]
    cores_favoritas = defaultdict(list)
    for chave, valor in cores:
        cores_favoritas[chave].append(valor)
    print(cores_favoritas)

    cores1 = ['amarelo', 'azul', 'azul', 'vermelho', 'azul', 'verde', 'vermelho']
    contador = Counter(cores1)
    print(contador)

    fila = deque()
    fila.append('1')
    fila.append('2')
    fila.append('3')

    print(len(fila))  # saída: 3

    fila.pop()  # exclui elemento da direita
    fila.append('3')  # adiciona elemento na direita
    fila.popleft()  # exclui elemento da esquerda
    fila.appendleft('1')  # adiciona elemento na esquerda
    print(fila)

    Conta = namedtuple('Conta', 'numero titular saldo limite')
    conta = Conta('123-4', 'João', 1000.0, 1000.0)
    print(conta)  # saída: Conta(numero='123-4', titular='João', saldo=1000.0, limite=1000.0)
    print(conta.titular)  # saída: João
    print(conta[0])

    arquivo = None
    funcionarios = Funcionarios()
    try:
        arquivo = open('funcionarios.txt', 'r')
        leitor = csv.reader(arquivo)
        for linha in leitor:
            funcionario = Funcionario(linha[0], linha[1], linha[2])
            funcionarios.append(funcionario)

    except IOError:
        print('Arquivo não existe')
    finally:
        if arquivo is not None:
            arquivo.close()

    print('Salário - Bonificação')
    for f in funcionarios:
        print('{} - {}'.format(f.salario, f.get_bonificacao()))
