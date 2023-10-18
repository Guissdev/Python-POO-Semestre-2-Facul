class Funcionario:
    def __init__(self, nome, rg, cpf):
        self.nome = nome
        self.rg = rg
        self.cpf = cpf


class Vendedor(Funcionario):
    def __init__(self, nome, rg, cpf, comissao):
        Funcionario.__init__(self, nome, rg, cpf)
        self.comissao = comissao

    def teste(self):
        print('Executou o metodo da classe vendedor')


class Gerente(Funcionario):
    def __init__(self, nome, rg, cpf, adicional):
        Funcionario.__init__(self, nome, rg, cpf)
        self.adicional = adicional

    def teste(self):
        print('Executou o metodo da classe Gerente')

    def salarioGerente(self):
        print(f'Adicional: {self.adicional}')


class GerenteVendas(Gerente, Vendedor):  # herança múltipla
    def __init__(self, nome, rg, cpf, comissao, adicional, area):
        Gerente.__init__(self, nome, rg, cpf, adicional)
        Vendedor.__init__(self, nome, rg, cpf, comissao)
        self.area = area


gv = GerenteVendas('João', '323232', '999999', 500, 150, 'vendas')
gv.teste()
gv.salarioGerente()