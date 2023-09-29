# Tratando exceções

try:
    a = int(input('Informe um número: '))
    b = int(input('Informe outro número: '))
    c = a/b
except ZeroDivisionError:
    print('Erro: divisão por zero')
except Exception:
    print('Algum erro ocorreu')
else:
    print(c)
finally:
    print('Final do programa')



# Gerando exceções

try:
    a = int(input('Informe um número positivo: '))
    if a <= 0:
        raise ValueError
except ValueError:
    print('Erro: O número deve ser positivo')
except Exception:
    print('Algum erro ocorreu')