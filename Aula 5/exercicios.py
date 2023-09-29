# Exercicio 1

while True:
    try:
        a = int(input('Numero: '))
        b = int(input('Numero: '))
        if a < 0 or b < 0:
            raise TypeError
        c = a / b
        print(c)
    except ValueError:
        print('Erro. O numero deve ser inteiro')
    except ZeroDivisionError:
        print('Erro de divisão')
    except TypeError:
        print('Erro. O numero deve ser positivo')
    except Exception:
        print('Erro inesperado')
    else:
        print('Operação realizada com sucesso')
        break

print('programa continua.....')



# Exercicio 2

def funcao_1():
    print('Início da função')
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    try:
        for i in range(15):
            print(lista[i])
    except IndexError:
        print('Erro. Indice inexistente')
    print('Fim da função')


print('Início do programa')
funcao_1()
print('Fim do programa')



# Exercicio 3

alunos = {}
while True:
    try:
        ra = input('RA (digite 0 para sair): ')
        if ra == '0':
            break
        nome = input('Nome: ')
        if len(ra) != 7 or not ra.isdigit():
            raise ValueError
        if ra in alunos:
            raise TypeError
        alunos[ra] = nome       # insere no dicionario
    except ValueError:
        print('RA invalido')
    except TypeError:
        print('Ra ja cadastrado')
    except Exception:
        print('Erro inesperado')

print(alunos)
