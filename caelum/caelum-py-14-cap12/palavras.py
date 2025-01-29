# Popula o arquivo 'palavras.txt' para ser usado pelo programa 'forca.py'

if __name__ == '__main__':
    arquivo = open('palavras.txt', 'w')
    arquivo.write('banana\n')
    arquivo.write('melancia\n')
    arquivo.write('morango\n')
    arquivo.write('manga\n')
    arquivo.close()
