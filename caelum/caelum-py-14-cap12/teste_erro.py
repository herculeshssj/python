from conta import ContaCorrente


def metodo1():
    print('início do metodo1')
    metodo2()
    print('fim do metodo1')


def metodo2():
    print('início do metodo2')
    cc = ContaCorrente('123', 'José', 1000.0)
    try:
        for i in range(1, 15):
            cc.deposita(i + 1000)
            print(cc.saldo)
            if i == 5:
                cc = None
    except AttributeError:
        print('erro')

    print('fim do metodo2')


if __name__ == '__main__':
    print('início do main')
    metodo1()
    print('fim do main')
