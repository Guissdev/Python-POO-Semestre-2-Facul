# Exercicio 1

class Pessoa:
    def __init__(self, nome, idade, carro):
        self.nome = nome
        self.idade = idade
        self.carro = carro

class Carro:
    def __init__(self, marca, modelo, placa, ano):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.ano = ano

meucarro = Carro('Volkswagen', 'Gol', 'AAA-1111', 2015)
eu = Pessoa('João', 25, meucarro)
print('Nome: ', eu.nome)                                # João
print('Idade: ', eu.idade)                              # 25
print('Marca do carro: ', eu.carro.marca)               # Volkswagen
print('Modelo do carro: ', eu.carro.modelo)             # Gol
print('Placa do carro: ', eu.carro.placa)               # AAA-1111
print('Ano do carro: ', eu.carro.ano)                   # 2015



# Exercicio 2

class Medico:
    def __init__(self, nome, crm, especializacao):
        self.nome = nome
        self.crm = crm
        self.especializacao = especializacao

    def __str__(self):
        return f'\nNome: {self.nome}\nCRM: {self.crm}\nEspecialização: {self.especializacao}'

class Paciente:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

    def __str__(self):
        return f'\nNome: {self.nome}\nCPF: {self.cpf}\nIdade: {self.idade}'

class Exame:
    def __init__(self, medico, paciente, descricao, resultado):
        self.medico = medico
        self.paciente = paciente
        self.descricao = descricao
        self.resultado = resultado

    def imprimir_exame(self):
        print(self.medico)
        print(self.paciente)
        print(f'Descrição: {self.descricao}')
        print(f'Resultado: {self.resultado}')

paciente = Paciente('Marcelo Silva', '033444555-22', 26)
medico = Medico('Ana Beatriz', 333431, 'Clínico Geral')
exame01 = Exame(medico, paciente, 'COVID-19', 'Negativo')  
exame01.imprimir_exame()						
# Deve exibir relatório com os dados do exame (inclusive os do médico e do paciente)



# Exercicio 3

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

class Pedido:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
    
    def calcular_valor(self):
        soma = 0
        for p in self.produtos:
            soma += p.preco * p.quantidade
        return soma
    
    def __str__(self):
        s = ''
        for p in self.produtos:
            s += f'{p.nome} {p.preco} {p.quantidade}\n'
        return s
    
cafe = Produto('Café Solúvel', 5.50, 1)
arroz = Produto('Arroz Integral', 4.90, 2)
feijao = Produto('Feijão Preto', 2.80, 2)
meu_pedido = Pedido()
meu_pedido.adicionar_produto(cafe)
meu_pedido.adicionar_produto(arroz)
meu_pedido.adicionar_produto(feijao)
print(meu_pedido)
print('O valor total é: ', meu_pedido.calcular_valor())	    # imprime 20.90