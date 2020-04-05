from oo.cliente import Cliente
from oo.carrinho import CarrinhoDeCompras, ProdutoCarrinho
from oo.escritor import MaquinaDeEscrever
from oo.escritor import Caneta
from oo.escritor import Escritor
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

""" 
Associação de objetos
"""

escritor = Escritor('Joãozinho')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()

del escritor
print(caneta.marca)
maquina.escrever()

"""
Agregação de objetos
"""

carrinho = CarrinhoDeCompras()

p1 = ProdutoCarrinho('Camiseta', 50)
p2 = ProdutoCarrinho('iPhone', 10000)
p3 = ProdutoCarrinho('Caneca', 15)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)

carrinho.lista_produto()
print(carrinho.soma_total())

"""
Composição de objetos
"""

cliente1 = Cliente('Luiz', 32)
cliente1.insere_endereco('Belo Horizonte', 'MG')
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1
print()

cliente2 = Cliente('Maria', 55)
cliente2.insere_endereco('Salvador', 'BA')
cliente2.insere_endereco('Rio de Janeiro', 'RJ')
print(cliente2.nome)
cliente2.lista_enderecos()
del cliente2
print()

cliente3 = Cliente('João', 19)
cliente3.insere_endereco('São Paulo', 'SP')
print(cliente3.nome)
cliente3.lista_enderecos()
del cliente3
print()

print('#########################################################')

"""
Lembrete de OO:

Associação - Usa
Agregação - Tem
Composição - É dono
Herança - É
"""
