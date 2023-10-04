# Exercicio 1

class Pessoa():
    def __init__(self, identificador, nome):
        self.identificador = identificador
        self.nome = nome

class PessoaJuridica(Pessoa):
    def __init__(self, identificador, nome, cnpj):
        super().__init__(identificador, nome)
        self.cnpj = cnpj

class PessoaFisica(Pessoa):
    def __init__(self, identificador, nome, rg, cpf):
        super().__init__(identificador, nome)
        self.rg = rg
        self.cpf = cpf

pessoa1 = Pessoa(1, "Ana")
p_juridica = PessoaJuridica(2, "Carlos", "1111111111")
p_fisica = PessoaFisica(3, "Clara", "222222222", "333333333")

print(pessoa1.identificador)        # 1
print(pessoa1.nome)                 # Nome da Pessoa

print(p_juridica.identificador)     # 2
print(p_juridica.nome)              # Nome da Pessoa Juridica
print(p_juridica.cnpj)              # 1111111111

print(p_fisica.identificador)       # 3
print(p_fisica.nome)                # Nome da Pessoa Fisica
print(p_fisica.rg)                  # 222222222
print(p_fisica.cpf)                 # 333333333



# Exercicio 2
print('---------------------------------------')

class Animal():
    def __init__(self, nome, cor, numero_patas):
        self.nome = nome
        self.cor = cor
        self.numero_patas = numero_patas

    def exibir_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Cor: {self.cor}')
        print(f'Quantidade de patas: {self.numero_patas}')


class Cachorro(Animal):
    def __init__(self, nome, cor, numero_patas, raca):
        super().__init__(nome, cor, numero_patas,)
        self.raca = raca

    def exibir_dados(self):
        super().exibir_dados()
        print(f'Raça: {self.raca}')

animal = Animal("Passarinho", "Azul", 2)
animal.exibir_dados()       # exibe os atributos do animal

dog = Cachorro("Rex", "Marrom", 4, "Vira lata")
dog.exibir_dados()          # exibe os atributos do cachorro



# Exercicio 3
print('---------------------------------------')

class Imovel():
    def __init__(self, endereco, preco):
        self.endereco = endereco
        self.preco = preco


class ImovelNovo(Imovel):
    def __init__(self, endereco, preco, adicional):
        super().__init__(endereco, preco)
        self.adicional = adicional

    def calcular_preco(self):
        return  self.preco + self.adicional
        
    
class ImovelVelho(Imovel):
    def __init__(self, endereco, preco, desconto):
        super().__init__(endereco, preco)
        self.desconto = desconto

    def calcular_preco(self):
        return self.preco - self.desconto
    
imovel = Imovel("Rua Silva, 123", 300000.0)
imovel_novo = ImovelNovo("Rua Joaquim, 999", 250000.0, 20000.0)
imovel_velho = ImovelVelho("Av. Brasil, 777", 500000.0, 35000.0)

print(imovel.endereco)                                      # Rua Silva, 123
print('Preço:', imovel.preco)                               # 300000.0

print(imovel_novo.endereco)                                 # Rua Joaquim, 999
print('Preço:', imovel_novo.preco)                          # 250000.0
print('Preço Atualizado:', imovel_novo.calcular_preco())    # 270000.0

print(imovel_velho.endereco)                                # Av. Brasil, 777
print('Preço:', imovel_velho.preco)                         # 500000.0
print('Preço Atualizado:', imovel_velho.calcular_preco())   # 465000.0



# Exercicio 4 
print('---------------------------------------')

class Motor():
    def __init__(self, cilindrada, potencia):
        self.cilindrada = cilindrada
        self.potencia = potencia

class Veiculo():
    def __init__(self, ano, preco, motor):
        self.ano = ano
        self.preco = preco
        self.motor = motor

    def exibir_dados(self):
        print(f'Motor - Cilindrada: {self.motor.cilindrada}, Potência: {self.motor.potencia}')
        print(f'Ano: {self.ano}')
        print(f'Preço: {self.preco}')

class Carro(Veiculo):
    def __init__(self, ano, preco, motor, cor, modelo):
        super().__init__(ano, preco, motor)
        self.cor = cor
        self.modelo = modelo

    def exibir_dados(self):
        super().exibir_dados()
        print(f'Cor: {self.cor}')
        print(f'Modelo: {self.modelo}')

class Caminhao(Veiculo):
    def __init__(self, ano, preco, motor, comprimento):
        super().__init__(ano, preco, motor)
        self.comprimento = comprimento

    def exibir_dados(self):
        super().exibir_dados()
        print(f'Comprimento: {self.comprimento}')

motor1 = Motor(1000, 500)
motor2 = Motor(8000, 900)
carro = Carro(2010, 20000, motor1, "branca", "gol")
caminhao = Caminhao(2015, 80000, motor2, 10)

carro.exibir_dados()           # imprime os valores de todos os atributos do carro
caminhao.exibir_dados()        # imprime os valores de todos os atributos do caminhão



# Exercicior 5
print('---------------------------------------')

class Pessoa():
    def __init__(self, nome, endereco, fone, cpf):
        self.nome = nome
        self.endereco = endereco
        self.fone = fone
        self.cpf = cpf

class Disciplina():
    def __init__(self, nome):
        self.nome = nome

class Aluno(Pessoa):
    def __init__(self, nome, endereco, fone, cpf,):
        super().__init__(nome, endereco, fone, cpf)
        self.disciplina = []

    def incluir_disciplina(self, disciplina):
        self.disciplina.append(disciplina)

class Funcionario(Pessoa):
    def __init__(self, nome, endereco, fone, cpf, salario):
        super().__init__(nome, endereco, fone, cpf)
        self.salario = salario

class Professor(Funcionario):
    def __init__(self, nome, endereco, fone, cpf, salario, titulacao):
        super().__init__(nome, endereco, fone, cpf, salario)
        self.titulacao = titulacao
        self.disciplina = []

    def incluir_disciplina(self, disciplina):
        self.disciplina.append(disciplina)

class Tecnico(Funcionario):
    def __init__(self, nome, endereco, fone, cpf, salario, cargo):
        super().__init__(nome, endereco, fone, cpf, salario)
        self.cargo = cargo

disciplina1 = Disciplina("Programação")
disciplina2 = Disciplina("Banco de Dados")
professor1 = Professor("Joao", "Rua Silva, 456", "(11)99999-9555", "9999999",
                       2000, "Mestrado")
aluno1 = Aluno("Maria", "Avenida São Francisco, 239",
               "(11)98888-8435", "555555")
tecnico1 = Tecnico("Pedro", "Rua Rocha, 77",
                   "(11)93333-3333", "8787887", 1500, "Tecnico")


aluno1.incluir_disciplina(disciplina1)
aluno1.incluir_disciplina(disciplina2)
professor1.incluir_disciplina(disciplina1)


print('Disciplinas associadas ao aluno:')
for d in aluno1.disciplina:
    print(d.nome)


print('Disciplinas associadas ao Professor:')
for d in professor1.disciplina:
    print(d.nome)