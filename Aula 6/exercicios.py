# Exercício 01 - Classe Livro
# Atributos:
# - titulo
# - autor
# - quantidade_paginas

class Livro:
    def __init__(self, titulo, autor, quantidade_paginas):
        self.titulo = titulo
        self.autor = autor
        self.quantidade_paginas = quantidade_paginas


livro1 = Livro("Harry Potter e a Pedra Filosofal", "J. K. Rowling", 264)
print(livro1.titulo)
print(livro1.autor)
print(livro1.quantidade_paginas)



#Exercício 02 - Classe Triangulo
#Atributos:
# - lado_a
# - lado_b
# - lado_c
#Métodos:
# - calcular_perimetro: retorna o perímetro do triângulo (soma dos três lados).

class Triangulo:
    def __init__(self, lado_a, lado_b, lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c
    
    def calcular_perimetro(self):
        return self.lado_a + self.lado_b + self.lado_c
        
a = float(input('Primeiro lado: '))
b = float(input('Segundo lado: '))
c = float(input('Terceiro lado: '))
t = Triangulo(a, b, c)       # cria o objeto
print(t.calcular_perimetro())



# Exercício 03 - Classe Televisão
# Atributos:
# - canal (o canal da tv deve ser inicializado no construtor como None)
# - volume (o volume da tv deve ser inicializado no construtor como zero)
#Métodos:
# - aumentar_volume: aumenta o nível de volume em uma unidade.
# - diminuir_volume: diminui o nível de volume em uma unidade.
# - alterar_canal: recebe o número do canal que será sintonizado e altera o canal da tv.

class Televisao:
    def __init__(self):
        self.canal = None
        self.volume = 0

    def aumentar_volume(self):
        self.volume += 1

    def diminuir_volume(self):
        self.volume -= 1

    def alterar_canal(self, canal):
        self.canal = canal

tv = Televisao()
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
tv.diminuir_volume()
tv.alterar_canal(5)
print(f'A tv está no canal {tv.canal}')                 # A tv está no canal 5
print(f'A tv está no volume {tv.volume}')               # A tv está no volume 2



# Exercício 04 - Classe Funcionário
# Atributos:
# - nome
# - salario
# Métodos:
# - aumentar_salario: aumenta o salário do funcionário de acordo com o percentual recebido como parâmetro.

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentar_salario(self, percentual):
        aumento = self.salario * percentual / 100
        self.salario += aumento

# cadastrar funcionarios
lista = []
quantidade = int(input('Quantidade de Funcionarios: '))
for i in range(quantidade):
    nome = input('Nome: ')
    salario = float(input('Salario: '))
    func = Funcionario(nome, salario)   # cria objeto
    lista.append(func)                  # insere objeto na lista

percentual = float(input('Percentual de aumento: '))

# aumentar salario de todos os funcionarios
for func in lista:
    func.aumentar_salario(percentual)

# exibe nome e salario de todos os funcionario
for func in lista:
    print(func.nome, func.salario)
