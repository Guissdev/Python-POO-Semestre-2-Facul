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

# 5 - Escreva um programa que receba uma frase como entrada e retorne uma lista das palavras presentes na frase.

# 6 - Implemente uma função que conte quantas palavras existem em uma string.

# 7 - Escreva uma função que remova todos os espaços em branco de uma string.

# 8 - Preencha uma lista com 10 números inteiros digitados pelo usuário e exiba:
#  (a) o maior número da lista
#  (b) o menor número da lista
#  (c) a média dos números contidos na lista

# 9 - Preencha uma lista com 10 números inteiros digitados pelo usuário e exiba:
#  (a) a quantidade de números pares contidos na lista
#  (b) o somatório de todos os números ímpares contidos na lista.

# 10 - Preencha uma lista com 10 números digitados pelo usuário. A partir desta lista, gere uma lista com os números pares e outra com os números ímpares. 
# Exemplo: 
# Suponha que a lista digitada seja: [1, 4, 7, 9, 5, 3, 7, 9, 8, 8]. 
# Para esta lista, o programa deve gerar as seguintes listas:
#  [4, 8, 8]
#  [1, 7, 9, 5, 3, 7, 9]

# 11 - Solicite 10 números inteiro e armazene-os em uma tupla. 
# Dica: primeiro crie uma lista, e então, converta a lista em tupla utilizando a função tuple.