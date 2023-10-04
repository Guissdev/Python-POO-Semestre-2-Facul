class Pessoa:
    def __init__(self, nome, idade, rg, cpf):
        self.nome = nome
        self.idade = idade
        self.rg = rg
        self. cpf = cpf

    def exibir(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'RG: {self.rg}')
        print(f'CPF: {self.cpf}')

class Aluno(Pessoa):
    def __init__(self, nome, idade, rg, cpf, ra):
        super().__init__(nome, idade, rg, cpf)
        self.ra = ra

    def exibir(self):
        super().exibir()
        print(f'RA: {self.ra}')


class Professor(Pessoa):
    def __init__(self, nome, idade, rg, cpf, salario):
        super().__init__(nome, idade, rg, cpf)
        self.salario = salario

    def exibir(self):
        super().exibir()
        print(f'Salario: {self.salario}')


aluno1 = Aluno('João', 20, '23232323', '666666666', '12345')
aluno1.exibir()

prof1 = Professor('Joaquim', 50, '6565656', '9999999', 3000)
prof1.exibir()