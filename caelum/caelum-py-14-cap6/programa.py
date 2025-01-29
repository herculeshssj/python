# r - read
# w - write
# a - append
# b - modo binário

arquivo = open('palavras.txt', 'w')
arquivo.write('banana')
arquivo.write('melancia')
arquivo.close()

arquivo = open('palavras.txt', 'a')
arquivo.write('morango\n')
arquivo.write('manga\n')
arquivo.close()

arquivo = open('palavras.txt', 'r')
print(arquivo.read())
arquivo.close()

arquivo = open('palavras.txt', 'r')
for linha in arquivo:
    print(linha)
arquivo.close()

arquivo = open('palavras.txt', 'r')
linha = arquivo.readline().strip()
print(linha)
arquivo.close()