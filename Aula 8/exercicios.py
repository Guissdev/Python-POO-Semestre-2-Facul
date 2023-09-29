# Exercicio 1

class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.__nome = nome
        self.__cpf = cpf
        self.__salario = salario

    def get_nome(self):
        return self.__nome
    
    def get_cpf(self):
        return self.__cpf
    
    def get_salario(self):
        return self.__salario

    def set_nome(self, nome):
        self.__nome = nome

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def set_salario(self, salario):
        self.__salario = salario

func1 = Funcionario("Pedro", "111222333-22", 1500.0)
func1.set_salario(2000.0)                 # Altera o salário
print("Nome:", func1.get_nome())          # Pedro
print("CPF:", func1.get_cpf())            # 111222333-22
print("Salário:", func1.get_salario())    # 2000.0



# Exercicio 2

class Filme:
    def __init__(self, titulo, genero):
        self.__titulo = titulo
        self.__genero = genero

    def get_titulo(self):
        return self.__titulo

    def get_genero(self):
        return self.__genero

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_genero(self, genero):
        self.__genero = genero

lista = []

for i in range(3):
    titulo = input('Titulo do filme: ')
    genero = input('Genero do filme: ')
    f = Filme(titulo, genero)       # cria o objeto
    lista.append(f)

for f in lista:
    print(f'Titulo: {f.get_titulo()}')
    print(f'Genero: {f.get_genero()}')



# Exercicio 3

class Cliente:
    def __init__(self, nome, cpf, senha):
        self.nome = nome
        self.__cpf = cpf
        self.__senha = senha

    def get_senha(self):
        return self.__senha

class ContaBancaria:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.__saldo = 0

    def depositar(self, valor, senha):
        if senha == self.cliente.get_senha():
            self.__saldo += valor
        else:
            print('Senha inválida')

    def sacar(self, valor, senha):
        if senha == self.cliente.get_senha():
            self.__saldo -= valor
        else:
            print('Senha inválida')
    
    def get_saldo(self):
        return self.__saldo

cliente1 = Cliente("João", "111111111", "123")
conta = ContaBancaria(1111, cliente1)

print(conta.get_saldo())            # Imprime 0
conta.depositar(200, "123")
print(conta.get_saldo())            # Imprime 200
conta.sacar(50, "123")
print(conta.get_saldo())            # Imprime 150

conta.depositar(100, "111")         # senha inválida
print(conta.get_saldo())            # Imprime 150
conta.sacar(50, "111")              # senha inválida
print(conta.get_saldo())            # Imprime 150