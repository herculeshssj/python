"""
Jogo de perguntas e respostas
"""

if __name__ == '__main__':
    perguntas = {
        'Pergunta 1': {
            'pergunta': 'Quando é 2+2? ',
            'respostas': {'a': '1', 'b': '4', 'c': '5'},
            'resposta_certa': 'b',
        },
        'Pergunta 2': {
            'pergunta': 'Quando é 2+2? ',
            'respostas': {'a': '1', 'b': '4', 'c': '5'},
            'resposta_certa': 'b',
        },
        'Pergunta 3': {
            'pergunta': 'Quando é 2+2? ',
            'respostas': {'a': '1', 'b': '4', 'c': '5'},
            'resposta_certa': 'b',
        },
        'Pergunta 4': {
            'pergunta': 'Quando é 2+2? ',
            'respostas': {'a': '1', 'b': '4', 'c': '5'},
            'resposta_certa': 'b',
        },
        'Pergunta 5': {
            'pergunta': 'Quando é 2+2? ',
            'respostas': {'a': '1', 'b': '4', 'c': '5'},
            'resposta_certa': 'b',
        },
    }

    respostas_certas = 0
    for pk, pv in perguntas.items():
        print(f'{pk}: {pv["pergunta"]}')
        print('Respostas: ')
        for rk, rv in pv['respostas'].items():
            print(f'[{rk}]: {rv}')
        resposta_usuario = input('Sua resposta: ')

        if resposta_usuario == pv['resposta_certa']:
            print('EHHHHHHH!!!!! Você acertou!!!!')
            respostas_certas += 1
        else:
            print('IXIIIIIII!!! Você errou!!!!')

    qtd_perguntas = len(perguntas)
    porcentagem_acerto = respostas_certas / qtd_perguntas * 100

    print(f'Você acertou {respostas_certas} respostas.')
    print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%.')
