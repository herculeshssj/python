from oo.pessoa import Pessoa


class Aluno(Pessoa):

    def estudar(self):
        print('Aluno está estudando...')

class AlunoEstrangeiro(Aluno):

    def estudar(self):
        super().estudar()
        print('Aluno estrangeiro está estudando...')