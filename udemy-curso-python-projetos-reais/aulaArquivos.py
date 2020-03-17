"""
Arquivos

Modos de abertura dos arquivos
'r' - read
'w' - read
'x' - creation
'a' - append
'b' - binary mode
't' - text mode
'+' - open for updating

"""

import os

if __name__ == '__main__':
    print('Arquivos')

    # Criação do arquivo
    file = open('abc.txt', 'w+')  # Permite leitura e escrita. A cada abertura o conteúdo do arquivo é apagado

    # Grava as linhas no arquivo
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')

    file.seek(0, 0)  # Volta para o início do arquivo
    print('Lendo linhas...')
    print(file.read())
    print('#####################')

    file.seek(0, 0)
    # Lendo linha por linha
    print(file.readline(), end='')
    print(file.readline(), end='')
    print('#####################')

    file.seek(0,0)
    # Lendo todas as linhas do arquivo
    print(file.readlines())
    print('#####################')

    file.seek(0, 0)
    # Lendo todas as linhas do arquivo através de um for
    for linha in file.readlines(): # Também funciona mandar o arquivo direto, mas somente para arquivos modo texto
        print(linha, end='')
    print('#####################')

    file.close()  # Fecha o arquivo

    # Usando gerenciador de contexto
    with open('abc.txt', 'w+') as file:
        file.write('Linha 1\n')
        file.write('Linha 2\n')
        file.write('Linha 3\n')

        file.seek(0)
        print(file.readlines(), end='')

    print('#####################')

    # Modos de acesso do arquivo
    # Leitura do arquivo
    with open('abc.txt', 'r') as file:
        print(file.readlines(), end='')

    print('#####################')

    # Modo append
    with open('abc.txt', 'a+') as file:
        file.write('Linha 4\n')
        file.seek(0)
        print(file.readlines(), end='')

    print('#####################')

    # Apagar o arquivo do disco
    os.remove('abc.txt')

