'''
|------------|         |---------------------|        |-------------|
| Produto    |         | Carrinho            |        | Cliente     |
|------------|         |---------------------|        |-------------|
| descricao  |0..*    1| cliente             |1      1| nome        |
| valor      |---------| produtos            |--------|-------------|
|------------|         |---------------------|        |             |
|            |         | adicionar_produto() |        |-------------|
|------------|         | listar_produtos()   |
                       | calcular_total()    |
                       |---------------------|
'''

class Cliente:
    def __init__(self, nome):
        self.nome = nome

class Produto:
    def __init__(self, descricao, valor):
        self.descricao = descricao
        self.valor = valor

class Carrinho:
    def __init__(self, cliente):
        self.cliente = cliente
        self.produtos = []
    
    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for p in self.produtos:
            print(p.descricao, p.valor)

    def calcular_total(self):
        soma = 0
        for p in self.produtos:
            soma += p.valor
        print(f'Total: {soma}')

# programa principal
cliente1 = Cliente('Paulo')

prod1 = Produto('Caneta', 5.0)
prod2 = Produto('Caderno', 30.0)
prod3 = Produto('Pen Drive', 45.0)

carrinho = Carrinho(cliente1)
carrinho.adicionar_produto(prod1)
carrinho.adicionar_produto(prod3)
carrinho.adicionar_produto(prod3)

carrinho.listar_produtos()

carrinho.calcular_total()