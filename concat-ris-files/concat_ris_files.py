import glob

arquivos_ris = glob.glob('/home/herculeshssj/Scholar/*.ris')
conteudo = []

for arquivo in arquivos_ris:
    with open(arquivo, 'r', encoding='utf-8') as f:
        conteudo.append(f.read())

with open('concatenado.ris', 'w', encoding='utf-8') as f:
    f.write('\n\n'.join(conteudo))

print('Arquivos concatenados com sucesso!')
