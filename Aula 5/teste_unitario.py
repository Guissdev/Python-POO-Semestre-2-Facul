import modulo 

try:
    # Executa a função
    c = modulo.somar(10, 20)
    # Verifica se o valor de retorno é igual ao esperado
    assert c == 30  # Instrução assert comapara os valores e gera uma AssertionError se forem diferentes
    print('Correto')
except AssertionError:
    # Caso o valor de retorno não seja igual ao esperado
    print('Erro')
