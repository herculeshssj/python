class MinhaExcecaoError(Exception):
    pass


def testar():
    raise MinhaExcecaoError('Tá errado! >:(')


if __name__ == '__main__':

    try:
        testar()
    except MinhaExcecaoError as error:
        print(f'Erro: {error}')
