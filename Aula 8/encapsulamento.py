class ContaBancaria:
    def __init__(self, numero, titular, saldo, senha):
        self.numero = numero
        self.titular = titular
        self.__saldo = saldo
        self.__senha = senha

    def sacar(self, valor, senha):
        if self.__validar_senha(senha):
            if valor <= self.__saldo:
                self.__saldo -= valor
                print('Saque realizado com sucesso.')
            else:
                print('Erro. Saldo insuficiente')
    
    def depositar(self, valor, senha):
        if self.__validar_senha(senha):
            self.__saldo += valor
            print('Depósito realizado com sucesso.')

    def get_saldo(self, senha):
        if self.__validar_senha(senha):
            return self.__saldo

    def __validar_senha(self, senha):
        if senha == self.__senha:
            return True
        else:
            print('Erro. Senha incorreta')
            return False

conta = ContaBancaria(123, 'Paulo', 0, 123456)

while True:
    print('1 - Deposito')
    print('2 - Saque')
    print('3 - Saldo')
    print('4 - Encerrar')
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        valor = float(input('Informe o valor: '))
        senha = int(input('Informe a senha: '))
        conta.depositar(valor, senha)
    elif opcao == 2:
        valor = float(input('Informe o valor: '))
        senha = int(input('Informe a senha: '))
        conta.sacar(valor, senha)
    elif opcao == 3:
        senha = int(input('Informe a senha: '))
        print(f'Saldo: {conta.get_saldo(senha)}')
    elif opcao == 4:
        print('Programa finalizado.')
        break
    else:
        print('Erro. opção incorreta.')
