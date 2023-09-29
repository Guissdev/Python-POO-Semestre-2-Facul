# Classe Pessoa
# atributos:
    # nome
    # idade
    # cpf
# métodos:
    # falar
    # comer
    # dormir

class Pessoa:
    def __init__(self, nome, idade, cpf):  # construtor
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
    
    def falar(self):
        print(f'A pessoa {self.nome} falou...')

    def comer(self):
        print(f'A pessoa {self.nome} comeu...')
    
    def dormir(self):
        print(f'{self.nome} ZZZzzzzzz')
    
    def exibir_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'CPF: {self.cpf}')


pessoa1 = Pessoa('João', 23, '123.546.769-28')
pessoa2 = Pessoa('Maria', 20, '333.555.666-98')
pessoa1.nome = 'João Pedro'
pessoa1.idade = 25

pessoa1.falar()
pessoa2.falar()
pessoa1.comer()

pessoa1.exibir_dados()
pessoa2.exibir_dados()