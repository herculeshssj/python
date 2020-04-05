from oo.pessoa import Pessoa
from oo.produto import Produto
from oo.basededados import BaseDeDados

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

"""
Métodos de classe
"""
p3 = Pessoa.create_pessoa_por_ano_nascimento('Maria', 1985)
print(f'{p3.nome} tem {p3.idade} anos.')


"""
Métodos estáticos
"""
print(f'ID gerado: {Pessoa.gera_id()}')
print(f'ID gerado: {p3.gera_id()}')


""" 
Métodos Getters e Setters 
"""
produto1 = Produto('Galão de água', 12.5)
print(f'Produto: {produto1.nome}; preço: {produto1.preco}')
produto1.desconto(10)
print(f'Produto: {produto1.nome}; preço: {produto1.preco}')

produto2 = Produto('Camiseta', '50')
print(f'Produto: {produto2.nome}; preço: {produto2.preco}')
produto2.desconto(15)
print(f'Produto: {produto2.nome}; preço: {produto2.preco}')

"""
No Python não existe as palavras reservadas private, protected e public como 
em outras linguagens OO, por padrão todos os atributos e métodos da classe são
públicos.

Por convenção se usa underscore ( _ ) para indicar que o atributo ou método é
privado e não deve ser acessado pelo desenvolvedor.

_ -> faz com que o atributo ou método se comporte como protected
__ -> faz com que o atributo ou método se comporte como private
"""
bd = BaseDeDados()
bd.inserir_cliente(1, 'João')
bd.inserir_cliente(2, 'Miranda')
bd.inserir_cliente(3, 'Rose')
bd._dados = 'Outra coisa'
bd.lista_clientes()
print(bd._dados)
print(bd._BaseDeDados__dados)
