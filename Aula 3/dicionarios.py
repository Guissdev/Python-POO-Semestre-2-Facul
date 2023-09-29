# DICIONÁRIOS

# RA e o nome
alunos = {'123456': 'Paulo', 
          '456987': 'Ana', 
          '777888': 'João'}

print(alunos)

# consulta um item especifico
print(alunos['456987'])

# alterar o nome de um aluno
alunos['456987'] = 'Ana Maria'
print(alunos)

# inserir um novo aluno
alunos['111222'] = 'Fernando'
print(alunos)

# remover um aluno
alunos.pop('123456')
print(alunos)

# operado in (busca)
if '777888' in alunos:
    print(f"Aluno cadastrado: {alunos['777888']}")
else:
    print('Aluno não cadastrado')

# percorrer as chaves do dicionario
for chave in alunos.keys():
    print(chave)

# percorrer os valores do dicionario
for valor in alunos.values():
    print(valor)

for chave, valor in alunos.items():
    print(f'RA: {chave}  - Nome: {valor}')

# tamanho do dicionario (quantidade de itens)
print(len(alunos))

# preencher dicionario com input
alunos = {}
for i in range(5):  # cadastrar 5 alunos
    ra = input('Informe o RA: ')
    nome = input('Informe o nome: ')
    alunos[ra] = nome       # insere no dicionario
print(alunos)


# dicionario contendo listas
# armazenar RA e uma lista de notas
alunos = {'123456': [9, 8, 7], 
          '389777': [6, 5, 10], 
          '556666': [6, 8, 8]}
print(alunos['123456'][0])      # exibe a primeira nota
alunos['123456'][0] = 6         # altera a primeira nota
alunos['123456'].append(10)     # insere uma nota
print(alunos)

# dicionario contendo diconários
alunos = {'123456': {'nome': 'Paulo', 'idade':  25}, 
          '389777': {'nome': 'Ana', 'idade':  30}, 
          '556666': {'nome': 'João', 'idade':  20}
          }

print(alunos['123456']['nome'])
print(alunos['123456']['idade'])
alunos['123456']['nome'] = 'Paulo Vieira'
print(alunos)
