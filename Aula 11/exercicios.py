from abc import ABC, abstractmethod

# Exercicio 1

class Operacao(ABC):
    @abstractmethod
    def calcular(self, x, y):
        pass

class Soma(Operacao):
    def calcular(self, x, y):
        return x + y
    
class Subtracao(Operacao):
    def calcular(self, x, y):
        return x - y
    
class Multiplicacao(Operacao):
   def calcular(self, x, y):
        return x * y
    
class Divisao(Operacao):
    def calcular(self, x, y):
        return x / y
    
soma = Soma()
sub = Subtracao()
div = Divisao()
mult = Multiplicacao()

print(soma.calcular(10, 5))      # 15
print(sub.calcular(10, 5))       # 5
print(div.calcular(10, 5))       # 2.0
print(mult.calcular(10, 5))      # 50



# Exercicio 2

class Animal(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Cachorro(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def emitir_som(self):
        print('O cachorro latiu')


class Gato(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def emitir_som(self):
        print('O gato miou')


class Cavalo(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def emitir_som(self):
        print('O cavalo relinchou')


class Veterinario():
    def examinar(self, animal):
        animal.emitir_som()          # Aqui tem polimorfismo

dog = Cachorro("Rex", 3)
horse = Cavalo("Horse", 6)
cat = Gato("Tina", 1)

dog.emitir_som()          # exibe o som do cachorro
horse.emitir_som()        # exibe o som do cavalo
cat.emitir_som()          # exibe o som do gato

vet = Veterinario()
vet.examinar(dog)         # exibe o som do cachorro 
vet.examinar(horse)       # exibe o som do cavalo 
vet.examinar(cat)         # exibe o som do gato



# Exercicio 3

class Funcionario(ABC):
    def __init__(self, nome, matricula, salario_base):
        self.nome = nome
        self.matricula = matricula
        self.salario_base = salario_base

    @abstractmethod
    def calcular_salario(self):
        pass


class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario_base):
        super().__init__(nome, matricula, salario_base)

    def calcular_salario(self):
        return self.salario_base * 2

class Assistente(Funcionario):
    def __init__(self, nome, matricula, salario_base):
        super().__init__(nome, matricula, salario_base)

    def calcular_salario(self):
        return self.salario_base


class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario_base):
        super().__init__(nome, matricula, salario_base)

    def calcular_salario(self):
        return self.salario_base * 1.10
    

funcionarios = []

gerente = Gerente('Abner', '123456', 1000)
funcionarios.append(gerente)

assistente = Assistente('Jubileu', '987654', 1000)
funcionarios.append(assistente)

vendedor = Vendedor('Aguinaldo', '192837', 1000)
funcionarios.append(vendedor)

for f in funcionarios:
    print(f'{f.nome} - {type(f).__name__} - {f.calcular_salario()}')