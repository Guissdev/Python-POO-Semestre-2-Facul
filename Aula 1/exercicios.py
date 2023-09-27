#Exercício 01
#Implemente a função somar que recebe dois números e retorna o resultado da soma desses dois números.
#Lembre-se que para retornar um resultado a função deve utilizar a instrução return.

a = 40
b = 32
c = 27

def somar(a, b):
    soma = a + b
    return soma

resultado = somar(a, b)
print(resultado)

#Exercício 02
#Implemente a função quadrado que recebe um número e retorna o resultado desse número ao quadrado

def quadrado(a):
    quadrado = a ** 2
    return quadrado

resultado = quadrado(a)
print(resultado)

#Exercício 03
#Implemente a função soma_dos_quadrados que receba dois numeros e devolve a soma dos seus quadrados.
#Você pode tentar reutilizar a função quadrado definida anteriormente para facilitar a implementação.

def soma_dos_quadrados(a, b):
    valor1 = quadrado(a)
    valor2 = quadrado(b)
    resultado = valor1 + valor2
    return resultado

resultado = soma_dos_quadrados(a, b)
print(resultado)

#Exercício 04
#Implemente a função media, que recebe três valores numéricos e retorna a média aritmética dos valores.

def media(a, b, c):
    media = a + b + c
    media = media / 3
    return media

resultado = media(a, b, c)
print(resultado)

#Exercício 05
#Implemente a função calcular_salario, que recebe o salário atual de um funcionário e retorna o salário com um reajuste de aumento, sendo que:
#Caso o salário seja maior que R$ 2.000,00, o funcionário receberá 7% de aumento.
#Caso contrário, o funcionário receberá 15% de aumento.

def calcular_salario(salario_atual):
    if salario_atual > 2000:
        aumento = salario_atual * 0.07
        salario_reajustado = salario_atual + aumento
        return salario_reajustado
    else:
        aumento = salario_atual * 0.15
        salario_reajustado = salario_atual + aumento
        return salario_reajustado

salario_atual = 1800
novo_salario = calcular_salario(salario_atual)
print(novo_salario)

#Exercício 06
#Implemente a função soma_divisores, que recebe como parâmetro de entrada um número positivo e retorna a soma de todos os divisores desse número.

#Por exemplo:
#caso o número seja 15, o retorno deve ser 24 (1 + 3 + 5 + 15).
#caso o número seja 30, o retorno deve ser 72 (1 + 2 + 3 + 5 + 6 + 10 + 15 + 30)

def soma_divisores(numero):
    soma = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            soma += i
    return soma

numero1 = 15
resultado1 = soma_divisores(numero1)
print(resultado1)
