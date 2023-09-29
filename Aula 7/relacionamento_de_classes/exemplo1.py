'''
|-------------------|           |-------------------|
| Pessoa            |           | Endereco          |
|-------------------|           |-------------------|
| nome              |           | rua               |
| idade             |-----------| numero            |
| endereco          |           | cep               |
|-------------------|           |                   |
|                   |           |-------------------|
|-------------------|           |                   |
                                |-------------------|
'''

class Endereco:
    def __init__(self, rua, numero, cep):
        self.rua = rua
        self.numero = numero
        self.cep = cep

    def exibir(self):
        print(self.rua)
        print(self.numero)
        print(self.cep)

class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

end1 = Endereco('Rua Silva', 123, '345678-000')
pessoa1 = Pessoa('Paulo', 30, end1)
pessoa1.endereco.exibir()
