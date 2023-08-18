# LISTA
# Sequencia de itens

# itens são separados com vírgula e delimitados por []
lista = [4, 3, 10, 20]

# listas são heterogêneas: pode armazenar diferentes tipos de dados
lista = [3, 'abc', 3.5, 5, 'dfdfd']

# listas são mutáveis: podem ser modificadas
lista[0] = 100
print(lista)

# Acesso pode ser feito pelos índices
print(lista[0])
print(lista[1])

# índices negativos (a partir do ultimo item)
print(lista[-1])
print(lista[-2])

# len - tamanho da lista
print(len(lista))

# append - insere um item no final da lista
lista = [10, 30, 5, 40]
lista.append(300)
print(lista)

# insert(indice, item) - insere o item no indice específico
lista.insert(1, 2)
print(lista)

# count - conta quantas vezes um item aparece na lista
lista = [2, 4, 5, 2, 3, 8, 2]
print(lista.count(2))

# index - retorna o indice de um item
lista = [2, 4, 5, 2, 4, 8, 2, 4]
print(lista.index(8))

# operador in (realiza uma busca)
lista = [2, 4, 5, 2, 4, 8, 2, 4]
if 4 in lista:
    print('Existe na lista')
else:
    print('Não existe na lista')

# pop() - remove o último item
lista = [1, 2, 3, 4, 5]
lista.pop()
print(lista)

# pop(indice) - remove o item de um índice específico
lista = [1, 2, 3, 4, 5]
lista.pop(0)
print(lista)

# remove - remove a primeira ocorrência de um item da lista
lista = [10, 20, 30, 40, 20, 20, 20, 20]
lista.remove(20)
print(lista)

# remove todas as ocorrências de um item
while 20 in lista:
    lista.remove(20)
print(lista)

# sort - ordena de forma crescente
lista = [3, 50, 1, 30, 25]
lista.sort()
print(lista)

lista = ['Paulo', 'ana', 'joão', 'Ana']
lista.sort()
print(lista)

# sort(reverse=True) - ordena de forma decrescente
lista = [3, 50, 8, 30, 25]
lista.sort(reverse=True)
print(lista)

# max - maior item
lista = [3, 50, 8, 30, 25]
print(max(lista))

# min = menor item
lista = [3, 50, 8, 30, 25]
print(min(lista))

# sum - somatorio dos itens
lista = [3, 50, 8, 30, 25]
print(sum(lista))

# concatenação de listas
lista1 = [3, 50, 8, 30, 25]
lista2 = [100, 200]
lista3 = lista2 + lista1 + lista2
print(lista3)

# percorrer os itens da lista
cont = 0
lista = [3, 50, 8, 30, 25]
for a in lista:
    if a % 2 == 0:
        cont += 1
print(f'Quantidade de pares: {cont}')

# percorrer os indices da lista
lista = [3, 50, 8, 30, 25]
for a in range(len(lista)):
    if lista[a] % 2 == 0:   # substituir os numeros pares por zero
        lista[a] = 0
print(lista)

# range(fim)
for a in range(10):      # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    print(a)

# range(inicio, fim)
for a in range(5, 10):      # 5, 6, 7, 8, 9
    print(a)

# range(inicio, fim, passo)
for a in range(3, 15, 2):      # 3, 5, 7, 9, 11, 13
    print(a)

# preencher lista

lista = []
for a in range(5):
    n = int(input('Digite um Numero Inteiro: '))
    lista.append(n)
print(f'Lista: {lista}')


# cópia de lista
lista = [3, 5, 7, 9]
lista2 = lista          # as duas variaveis fazem referencia a mesma lista
lista2[0] = 200
print(lista, lista2)

# cópia de lista
lista = [3, 5, 7, 9]
lista2 = lista.copy()   # gera uma nova lista
lista2[0] = 200
print(lista, lista2)