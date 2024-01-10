"""
Operadores

Adição (+)
Subtração (-)
Multiplicação (*)
Divisão (/)
Divisão inteira (//)
Potenciaćão (**)
Resto da divisão (%)

Os parênteses alteram a precedência dos operadores
"""

if __name__ == '__main__':
    print('Operadores aritméticos')

    print('Adição: 10 + 10 =', 10 + 10)
    print('Subtração: 10 - 10 =', 10 - 10)
    print('Multiplicação: 10 * 10 =', 10 * 10)
    print('Divisão: 10 / 2 =', 10 / 2)
    print('Divisão inteira: 10.5 // 2 =', 10.5 // 2)
    print('Potenciação: 10 ** 2 =', 10 ** 2)
    print('Resto da divisão: 10 % 3 =', 10 % 3)

    # Caso especial com o operador (*)
    print('Duplicação de string:', 10 * 'A')

    # Caso especial com o operador (+)
    print('Concatenação de string:', '5' + 'A')
    print('José' + ' tem ' + str(32) + ' anos')

    # Precedência
    print(5+2*10)
    print((5+2)*10)

"""
Precedência dos Operadores Aritméticos

Assim como aprendemos na matemática, operadores têm uma certa precedência que pode ser alterada usando os parênteses (como descrito na aula anterior).

Abaixo, segue uma lista mais precisa de quais operadores tem maior prioridade na hora de realizar contas mais complexas (de maior para menor precedência).

    ( n + n ) - Os parênteses têm a maior precedência, contas dentro deles são realizadas primeiro

    ** - Depois vem a exponenciação

    * / //  % - Na sequência multiplicação, divisão, divisão inteira e módulo

    +  - - Por fim, soma e subtração

Contas com operadores de mesma precedência são realizadas da esquerda para a direita.

Observação: existem muito mais operadores do que estes em Python e todos eles também têm precedência, você pode ver a lista completa em https://docs.python.org/3/reference/expressions.html#operator-precedence (sempre utilize a documentação oficial como reforço caso necessário).

Caso tenha dúvidas, faça testes com números. Por exemplo, olhe para essa conta e tente decifrar como chegar no resultado: 2 + 5 * 3 ** 2 - (23.5 + 23.5) (o resultado é 0.0). Para isso você precisa realizar as contas com maior precedência primeiro.
"""