from datetime import datetime, timedelta

if __name__ == '__main__':
    print('Trabalhando com data e hora no Python')

    # hoje = datetime()
    # print(hoje)

    data_atual = datetime(2020, 6, 27)
    print(data_atual)

    data_hora_atual = datetime(2020, 6, 27, 10, 40, 0)
    print(data_hora_atual)

    print('Data formatada:', data_hora_atual.strftime('%d/%m/%Y %H:%M:%S'))

    print('String to Datetime')
    data_str = datetime.strptime('30/06/2020', '%d/%m/%Y')
    print(data_str)
    print('Timestamp: ', data_str.timestamp())
    print('From timestamp:', data_str.fromtimestamp(1593486000.0))

    inicio = datetime(2020, 6, 1)
    fim = datetime(2020, 6, 30)

    print('Soma 5 dias a data')
    inicio = inicio + timedelta(days=5, seconds=59)
    print(inicio)

    print('Cálculo com data')
    inicio = inicio + timedelta(seconds=2*60*60)
    print(inicio)

    print('Diferença entre as datas')
    dif = fim - inicio
    print(dif)

    print('Somente os segundos da data final', dif.seconds)
    print('Segundos totais: ', dif.total_seconds())
    print('Somente os dias', dif.days)

    print('Mostrando somente a data: ', inicio.date())
    print('Mostrando somente a hora: ', inicio.time())

    print('Comparação de datas')
    print(inicio > fim)
    print(inicio == fim)
    print(inicio < fim)

    print('Imprimir data em português Brasil')
    # Sexta, 13 de junho de 2019
    dt = datetime.now()
    formatacao = dt.strftime('%A, %d de %B de %Y')
    print(formatacao)

    from locale import setlocale, LC_ALL
    setlocale(LC_ALL, 'pt_BR.utf-8')
    dt = datetime.now()
    formatacao = dt.strftime('%A, %d de %B de %Y')
    print(formatacao)

    print('Último dia do mês')
    from calendar import mdays
    mes_atual = int(dt.strftime("%m"))
    print('Último dia do mês: ', mes_atual, mdays[mes_atual])
    print(mdays)

    """
    Último dia do mês em ano bissexto
    Na aula anterior, você viu como utilizar mdays de calendar 
    (que pega a quantidade de dias do mês) para pegar o último dia do mês. 
    Isso pode não funcionar como esperado em ano bissexto.

    Você também pode utilizar a função monthrange de calendar para pegar o 
    número do dia na semana (entre 0-6) e último dia do mês (entre 28-31), 
    exemplo:
    """

    from calendar import monthrange

    # Retorna uma tupla contendo o número do dia na semana (0-6)
    # e último dia de fevereiro de 2020
    print(monthrange(2020, 2))

    # Saída - (5, 29)
    # O 5 significa que é um sábado
    # O 29 significa que este é o último dia do mês
    # O número do dia na semana vai de 0 a 6 (segunda é 0, domingo é 6).

    # Caso queira retornar apenas um valor, você pode fazer o desempacotamento, assim:

    from calendar import monthrange
    dia_semana, ultimo_dia = monthrange(2020, 2)
    print(ultimo_dia)  # Saída: 29 (último dia de fevereiro de 2020)
    # Você também pode criar uma lista, assim como mdays, contendo todos os últimos dias de meses do ano atual:

    from datetime import datetime
    from calendar import monthrange

    ultimos_dias_de_meses_do_ano_atual = [
        monthrange(datetime.now().year, mes)[1] for mes in range(1, 13)
    ]
    print(ultimos_dias_de_meses_do_ano_atual)
    # Saída: [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Observação: meu ano atual é 2020 neste momento
    # Isso deve solucionar os problemas do ano bissexto.
