"""
Groupby - Agrupando valores
"""
from itertools import groupby

if __name__ == '__main__':
    print('Agrupando valores')

    alunos = [
        {'nome': 'Luiz', 'nota': 'A'},
        {'nome': 'Maria', 'nota': 'B'},
        {'nome': 'João', 'nota': 'C'},
        {'nome': 'Gustavo', 'nota': 'B'},
        {'nome': 'Henrique', 'nota': 'A'},
        {'nome': 'Débora', 'nota': 'B'},
        {'nome': 'Marília', 'nota': 'C'},
        {'nome': 'Marta', 'nota': 'B'},
        {'nome': 'Sérgio', 'nota': 'B'},
        {'nome': 'Cintia', 'nota': 'A'},
        {'nome': 'Souza', 'nota': 'D'}
    ]

    ordena = lambda item: item['nota']
    alunos.sort(key=ordena)
    for aluno in alunos:
        print(aluno)

    print()

    alunos_agrupados = groupby(alunos, ordena)
    for agrupamento, valores in alunos_agrupados:
        lista_alunos = list(valores)
        print(f'Agrupamento: {agrupamento}, Quant. de alunos: {len(lista_alunos)}')

        for aluno in lista_alunos:
            print(aluno)

        print()
