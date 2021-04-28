"""
Placeholders
pass
... -> elipse

Servem para indicar que um código será escrito no local dos placeholders.
Muito útil para quando se escreve o código usando TDD.
"""
if __name__ == '__main__':
    print('Placeholders')

    valor = True
    var = False

    if valor:
        # Imprimir 'Oi' na tela
        pass
    else:
        print('Tchau')

    if var:
        # Imprimir 'Oi' na tela
        ...
    else:
        print('Tchau')