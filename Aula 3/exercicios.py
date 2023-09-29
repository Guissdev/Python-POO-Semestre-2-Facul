#Exercício 01
#Preencha um dicionário com as informações de 5 pessoas.
# - Utilize o cpf da passoa como chave e o nome como valor. 
# - Solicite os dados ao usuário.

pessoas = {}
for i in range (5):
    cpf = input('DIgite o CPF:')
    nome = input('Digite o nome:')
    pessoas[cpf] = nome
print(pessoas)



#Exercício 02
# - Preencha um dicionário com as informações de 5 produtos.
# - Utilize o nome do produto como chave e o preço como valor. 
# - Solicite os dados ao usuário.
# - Percorra o dicionário e exiba o nome dos produtos com preço superior a R$ 50.00

produto = {}
for i in range(5):      # preenche o dicionario
    nome = input('Nome do produto: ')
    preco = float(input('Preço do produto: '))
    produto[nome] = preco
print(produto)

# percorre os itens do dicionario
for nome, preco in produto.items():
    if preco > 50:
        print(f'Nome: {nome} - Preço: {preco}')



#Exercício 03
# - Preencha um dicionário com os dados de 5 alunos.
# - Utilize o ra do aluno como chave e uma lista de três notas como valor.
# - Solicite os dados ao usuário.
# - Percorra o dicionário e exiba a média de cada aluno.

alunos = {}
for i in range(3):
    ra = input('RA: ')
    n1 = float(input('Primeira nota: '))
    n2 = float(input('Segunda nota: '))
    n3 = float(input('Terceira nota: '))
    alunos[ra] = [n1, n2, n3]
print(alunos)

for ra, notas in alunos.items():
    media = sum(notas) / len(notas)
    print(ra, media)



#Exercício 04
# - Conte a quantidade de vogais em um texto e armazena tal quantidade em um dicionário, onde 
# - a chave é a vogal e o valor é a quantidade de vezes que essa vogal aparece no texto.

quantidade = {}
vogais = 'aeiou'

texto = input('Digite um texto: ').lower()

for letra in texto:         # percorre a string
    if letra in vogais:     # verifica se é uma vogal
        if letra not in quantidade:
            quantidade[letra] = 1   # insere pela primeira vez
        else:
            quantidade[letra] += 1  # incrementa se ja existir
print(quantidade)
