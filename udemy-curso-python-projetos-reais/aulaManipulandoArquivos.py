"""
Manipulando arquivos e diretórios
"""
import os
import shutil


def formata_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5
    exa = base ** 6

    texto = ''

    if tamanho < mega:
        tamanho /= kilo
        texto = 'Kilobytes'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'Megabytes'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'Gigabytes'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'Terabytes'
    elif tamanho < exa:
        tamanho /= peta
        texto = 'Exabytes'
    else:
        texto = 'bytes'

    tamanho = round(tamanho, 2)
    return f'{tamanho} {texto}'


if __name__ == '__main__':
    print('Manipulando arquivos e diretórios')

    # caminho_procura = 'C:\\Users\\hercu\\OneDrive\\Documentos\\Gnucash'
    caminho_procura = input('Digite um caminho: ')
    termo_procura = input('Digite um termo: ')
    contador = 0

    for raiz, diretorios, arquivos in os.walk(caminho_procura):
        for arquivo in arquivos:
            #caminho_completo = os.path.join(raiz, arquivo)
            # print(caminho_completo)
            #nome_arquivo, extensao_arquivo = os.path.splitext(caminho_completo)
            #print('Arquivo:', nome_arquivo, '; Extensão: ', extensao_arquivo)
            #tamanho_arquivo = os.path.getsize(caminho_completo)
            #print('Tamanho', tamanho_arquivo)

            try:

                if termo_procura in arquivo:

                    contador += 1

                    caminho_completo = os.path.join(raiz, arquivo)
                    # print(caminho_completo)
                    nome_arquivo, extensao_arquivo = os.path.splitext(
                        caminho_completo)
                    print('Arquivo:', nome_arquivo,
                          '; Extensão: ', extensao_arquivo)
                    tamanho_arquivo = os.path.getsize(caminho_completo)
                    print('Tamanho', formata_tamanho(tamanho_arquivo))

            except PermissionError as pe:
                print('Sem permissão de acesso!')
            except FileNotFoundError as fnfe:
                print('Arquivo não encontrado!')
            except Exception as e:
                print('Erro desconhecido!', e)

    print()
    print(f'{contador} arquivo(S) encontrado(s).')
    print()

    caminho_original = r'C:\Users\hercu\OneDrive\Documentos\Gnucash'
    caminho_novo = r'C:\Users\hercu\OneDrive\Documentos\Gnucash\novo'

    try:
        os.mkdir(caminho_novo)
    except FileExistsError as fee:
        print(f'Pasta {caminho_novo} já existe.')

    for root, dirs, files in os.walk(caminho_novo):
        for file in files:
            file_path = os.path.join(caminho_novo, file)
            if '.log' in file:
                os.remove(file_path)

    for root, dirs, files in os.walk(caminho_original):
        for file in files:
            old_file_path = os.path.join(root, file)
            new_file_path = os.path.join(caminho_novo, file)
            # shutil.move(old_file_path, new_file_path)  # move e/ou renomeia
            # print(f'Arquivo {file} movido com sucesso!')

            if '.log' in file:
                shutil.copy(old_file_path, new_file_path)
                print(f'Arquivo {file} copiado com sucesso!')
