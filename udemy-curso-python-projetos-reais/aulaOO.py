from oo.pessoa import Pessoa

p1 = Pessoa('Luiz', 32)
p2 = Pessoa('João', 30)

# p1.nome = 'Luiz'
# p2.nome = 'João'

# print(f'Pessoa 1 (p1): {p1.nome}')
# print(f'Pessoa 2 (p2): {p2.nome}')

p1.falar()
p1.comer('maçã')
p1.falar()
p1.parar_falar()
p1.comer('maçã')
p1.falar()

print(f'Ano atual: {p1.ano_atual}')
print(f'{p1.nome} nasceu em {p1.get_ano_nascimento()}')
print(f'{p2.nome} nasceu em {p2.get_ano_nascimento()}')