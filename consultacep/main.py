from csv import reader
import time
import brazilcep

if __name__ == '__main__':
    print('Hello :)')

    print('Lendo o arquivo CSV...')

    ### https://thispointer.com/write-to-a-csv-file-in-loop-in-python/

    with open('CEPs.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        if header != None:
            for row in csv_reader:
                print(row[0])
                address = brazilcep.get_address_from_cep(row[0])
                print(address)
                time.sleep(5)