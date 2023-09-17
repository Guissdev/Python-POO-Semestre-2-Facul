# STRING
# Listas de caracteres

# acessar os caracteres pelos indices
texto = 'Exemplo de texto'
c = texto[0]
print(c)

for c in texto:
    print(c)

# len - retorna o tamanho da string
print(len(texto))

# upper - converte os caracteres para maiusculo
print(texto.upper())

# lower - converte os caracteres para minusculo
print(texto.lower())

# title - coloca a inicial de cada palavra em maiusculo
print(texto.title())

# capitalize - coloca apenas a primeira letra em maiusculo
print(texto.capitalize())

# replace - substitui uma substring por outra
texto = 'Exemplo de texto texto'
texto = texto.replace(' ', '')
print(texto)

# index - retorna o indice de uma substring
texto = 'Exemplo de texto texto texto'
print(texto.index('texto'))

# split - divide uma string de acordo com um separador
# retorna uma lista de strings
texto = 'banana, laranja, maça, melancia'
lista = texto.split(', ')
print(lista)

# concatenação de strings
texto1 = 'banana'
texto2 = 'laranja'
texto3 = texto1 + ', ' + texto2 + ', ' + texto1
print(texto3)