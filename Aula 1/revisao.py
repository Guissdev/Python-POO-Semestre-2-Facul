# Revisão das estruturas básicas de python

# Exemplo de comentario de 1 linha

'''
Exemplo de 
comentario de 
multiplas 
linhas
'''


# tipos de dados
# int ( números inteiros)
a = 20
b = -30
c = 0
# float (números reais)
a = 20.5
b = -3.99
c = 1.0
# bool (valores lógicos/booleanos)
a = True
b = False
# str (string/texto)
a = 'Paulo'
b = "Exemplo de texto"
c = """1 - soma
2 - subtração
3 - multiplicação
"""

# operações de conversão de tipo
a = 1
a = float(a)        # converte para float
print(a)

a = 4.5
a = int(a)          # converte para int
print(a)

a = 3.55
a = str(a)          # converte para string
print(a)

# Operações de entrada (input)

nome = input('Informe seu nome: ')
idade = int(input('Informe a idade: '))
altura = float(input('Informe sua altura: '))


# operações de saída (print)
nome = 'Paulo'
idade = 30 
print(nome, idade)
print('O seu nome é', nome, 'e sua idade é de', idade, 'anos')
print('O seu nome é {} e sua idade é de {} anos'.format(nome, idade))
print(f'O seu nome é {nome} e sua idade é de {idade} anos')

# Operadores Aritmético
print(10 + 3)       # adição
print(10 - 3)       # subtração
print(10 * 3)       # multiplicação
print(10 / 3)       # divisão
print(10 // 3)      # divisão inteira
print(10 % 3)       # resto de divisão inteira (mod)
print(10 ** 3)      # potência

# Ordem de prioridade
# 1º: **
# 2º: * / // %
# 3º: + -

# Operadores Relacionais
print(10 > 3)       # maior
print(10 < 3)       # menor
print(10 == 3)      # igual
print(10 != 3)      # diferente
print(10 >= 3)      # maior ou igual
print(10 <= 3)      # menor ou igual

# Operadores Lógicos
print(10 < 3 and 10 == 10)      # E
print(10 < 3 or 10 == 10)       # OU
print(not 10 == 10)             # NÃO

# instruções condicionais (if elif else)
# verifica se o número é par ou ímpar

numero = int(input('Informe um numero: '))
if numero % 2 == 0:
    print('O numero é par')
else:
    print('O número é ímpar')

# verifica se o número é positivo, negativo ou zero
if numero > 0:
    print('Positivo')
elif numero < 0:
    print('Negativo')
else:
    print('Zero')


# estrutura de seleção (match case)
letra = (input('Informe uma letra: '))
match letra:
    case 'a' | 'A':
        print('Letra A')
    case 'b' | 'B':
        print('Letra B')
    case _:             # default
        print('A letra não é A e B')

float = 10
b = type(a) == int

match b:
    case True:
        print('inteiro')
    case False:
        print('float')


# estrutura de repetição while
# exibir os numeros inteiros de 1 a 10
cont = 1
while cont <= 10:
    print(cont)
    cont += 1

# Exemplo de Calculadora
opcao = 0
while opcao != 5:
    print('1 - soma')
    print('2 - subtração')
    print('3 - multiplicação')
    print('4 - divisão')
    print('5 - SAIR')
    opcao = int(input('Escolha uma opção: '))
    match opcao:
        case 1:
            a = float(input('Primeiro numero: '))
            b = float(input('Segundo numero: '))
            print(f'O resultado é {a + b}')
        case 2:
            a = float(input('Primeiro numero: '))
            b = float(input('Segundo numero: '))
            print(f'O resultado é {a - b}')
        case 3:
            a = float(input('Primeiro numero: '))
            b = float(input('Segundo numero: '))
            print(f'O resultado é {a * b}')
        case 4:
            a = float(input('Primeiro numero: '))
            b = float(input('Segundo numero: '))
            print(f'O resultado é {a / b}')
        case 5:
            break               # finaliza o loop
        case _:
            print('Opção inválida. Tente novamente.')

# estrutura de repetição for
# exibir os numeros inteiros de 1 a 10
for a in range(1, 11):
    print(a)

# exibir os numeros pares de 1 a 10
for a in range(2, 11, 2):
    print(a)


# Funções
# definir uma função para realizar a soma de dois números
def somar(numero1, numero2):
    c = numero1 + numero2
    return c

c = somar(4, 7)         # chamada da função
print(c)

print(somar(10, 50))    # chamada da função

a = int(input('Primeiro numero: '))
b = int(input('Segundo numero: '))
print(f'A soma de {a} e {b} é igual a {somar(a, b)}')