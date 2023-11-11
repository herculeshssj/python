from csv import reader
import time
import brazilcep
import sqlite3

if __name__ == '__main__':
    
    # Conectando na base SQLite...
    connection = sqlite3.connect("ceps.db")
    cursor = connection.cursor()

    ### Descomente caso seja a primeira vez que o script está sendo executado
    # cursor.execute("create table logradouro (district TEXT, cep TEXT, city TEXT, street TEXT, uf TEXT, complement TEXT)")
    # connection.commit()

    with open('CEPs.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        if header != None:
            for csv_row in csv_reader:
                cep = "{}-{}".format(csv_row[0][:5], csv_row[0][5:])
                print(cep)
                rows = cursor.execute("select cep from logradouro where cep = ?", (cep,)).fetchall()
                if len(rows) == 0:
                    
                    address = None
                    try:
                        address = brazilcep.get_address_from_cep(csv_row[0])

                        print(address)
                        sql_tuple = (
                            address['district'],
                            address['cep'],
                            address['city'],
                            address['street'],
                            address['uf'],
                            address['complement']
                        )

                        cursor.execute("insert into logradouro (district, cep, city, street, uf, complement) values (?,?,?,?,?,?)", sql_tuple)
                        connection.commit()
                    except brazilcep.exceptions.CEPNotFound as e:
                        # Registra o CEP na base para que o mesmo não seja consultado novamente
                        sql_tuple = ('-', cep, '-', '-', '-', '-')
                        cursor.execute("insert into logradouro (district, cep, city, street, uf, complement) values (?,?,?,?,?,?)", sql_tuple)
                        connection.commit()

                        print('CEP ', csv_row[0], ' não encontrado, continuando...')

                else:
                    print('CEP ',csv_row[0], ' já existe, continuando...')
                    continue

                time.sleep(15)
                
    # Fechando os recursos
    cursor.close()
    connection.close()