# TUPLA
# Sequancia de itens

# tupla é delimitada por parenteses ( )
tupla = (3, 6, 8)

# tupla é heterogênea
tupla = (2, 3.6, 'abc')

# tupla não é mutável (imutável)
# a tupla não pode ser alterada
tupla = (3, 6, 8)

# tupla vazia
tupla = ()
print(tupla)

# tupla de 1 elemento
tupla = (10,)
print(tupla)

tupla = ([2, 3, 4], [30, 40, 50])
tupla[0][0] = 10
print(tupla)

tupla = (4, 1, 10)
print(tupla.count(4))

# operador in
if 10 in tupla:
    print('O valor está na tupla')
else:
    print('O valor nao está na tupla')

# concatenação
tupla1 = (3, 6)
tupla2 = (10, 20)
tupla3 = tupla1 + tupla2
print(tupla3)

# funções de conversão

# list - gera uma lista a partir de uma tupla
tupla = (4, 5, 6)
lista = list(tupla)
print(lista)

# tuple - gera uma tupla a partir de uma lista
lista = [3, 4, 5]
tupla = tuple(lista)
print(tupla)

# exemplo para ordenar uma tupla
tupla = (3, 10, 20, 2, 40, 1)
lista = list(tupla)
lista.sort()
tupla2 = tuple(lista)
print(tupla2)

# exemplo de aplicação de tupla
def funcao(a, b):
    soma = a + b
    subtracao = a - b
    return soma, subtracao   # gera uma tupla

retorno = funcao(10, 5)
print(retorno)
print(retorno[0])
print(retorno[1])