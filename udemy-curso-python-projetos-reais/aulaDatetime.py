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
