# Exercicios

# 1 - Escreva uma função que receba uma string e retorne o número de caracteres nela.

def conta_caracteres(texto):
    return len(texto)

texto = input('Digite uma string: ')
print( conta_caracteres(texto) )

# 2 - Crie uma função que receba uma string e retorne a mesma string com todas as letras em maiúsculas.

def converte_maiusculo(texto):
    return texto.upper()

texto = input("Informe um texto: ")
print(converte_maiusculo(texto))

# 3 - Implemente uma função que substitua todas as ocorrências de uma substring por outra em uma string dada.

def troca_string(texto, textoantigo, textonovo):
    return texto.replace(textoantigo, textonovo)

texto = input('Digite um texto: ')
textoantigo = input('Digite o valor que será substuido: ')
textonovo = input('Digite o valor que será inserido: ')

print(troca_string(texto, textoantigo, textonovo))

# 4 - Crie uma função que conte quantas vogais (a, e, i, o, u) existem em uma string.

def conta_vogais(frase):
    frase = frase.lower()
    quantidade = frase.count('a')
    quantidade += frase.count('e')
    quantidade += frase.count('i')
    quantidade += frase.count('o')
    quantidade += frase.count('u')
    return quantidade

def conta_vogais2(frase):
    frase = frase.lower()
    quantidade = 0
    for caracter in frase:      # percorre os caracteres da string
        if caracter in 'aeiou':
            quantidade += 1
    return quantidade

frase = input('Digite uma frase: ')
print(conta_vogais(frase))
print(conta_vogais2(frase))

# 5 - Escreva um programa que receba uma frase como entrada e retorne uma lista das palavras presentes na frase.

def lista_palavras(frase):
    lista = frase.split(' ')
    return lista

# 6 - Implemente uma função que conte quantas palavras existem em uma string.

def conta_palavras(frase):
    lista = frase.split(' ')
    return len(lista)       # tamanho da lista

frase = input('Frase: ')
print(lista_palavras(frase))
print(conta_palavras(frase))

# 7 - Escreva uma função que remova todos os espaços em branco de uma string.

def remove_espacos(frase):
    frase = frase.replace(' ', '')
    return frase

frase = input('Frase: ')
print(remove_espacos(frase))

# 8 - Preencha uma lista com 10 números inteiros digitados pelo usuário e exiba:
#  (a) o maior número da lista
#  (b) o menor número da lista
#  (c) a média dos números contidos na lista

lista = []
for i in range(10):    # 0,1,2,3,...,9      # preenche a lista
    numero = int(input('Numero: '))
    lista.append(numero)
print(lista)

maior = max(lista)
menor = min(lista)
media = sum(lista) / len(lista)

print(f'Maior: {maior}')
print(f'Menor: {menor}')
print(f'Média: {media}')

# 9 - Preencha uma lista com 10 números inteiros digitados pelo usuário e exiba:
#  (a) a quantidade de números pares contidos na lista
#  (b) o somatório de todos os números ímpares contidos na lista.

lista = []
for i in range(10):    # 0,1,2,3,...,9      # preenche a lista
    numero = int(input('Numero: '))
    lista.append(numero)
print(lista)

cont = 0            # contador
soma = 0            # somador

for item in lista:
    if item % 2 == 0:
        cont += 1           # cont = cont + 1
    else:
        soma += item        # soma = soma + item

print(f'Quantidade de números pares: {cont}')
print(f'Somatório dos números ímpares: {soma}')

# 10 - Preencha uma lista com 10 números digitados pelo usuário. A partir desta lista, gere uma lista com os números pares e outra com os números ímpares. 
# Exemplo: 
# Suponha que a lista digitada seja: [1, 4, 7, 9, 5, 3, 7, 9, 8, 8]. 
# Para esta lista, o programa deve gerar as seguintes listas:
#  [4, 8, 8]
#  [1, 7, 9, 5, 3, 7, 9]

pares = []
impares = []

for i in range(10):
    numero = int(input('Numero: '))
    if numero % 2 == 0:
        pares.append(numero)    # insere na lista de pares
    else:
        impares.append(numero)  # insere na lista de impares

print(pares)
print(impares)

# 11 - Solicite 10 números inteiro e armazene-os em uma tupla. 
# Dica: primeiro crie uma lista, e então, converta a lista em tupla utilizando a função tuple.

lista = []
for i in range(10):
    numero = int(input('Numero: '))
    lista.append(numero)
print(lista)

tupla = tuple(lista)        # copia os itens da lista para uma tupla
print(tupla)