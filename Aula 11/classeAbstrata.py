from abc import ABC, abstractmethod

class Conta(ABC):               # classe abstrata
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    @abstractmethod
    def sacar(self, valor):     # método abstrato
        pass

class ContaCorrente(Conta):
    def __init__(self, numero, titular, saldo, limite):
        super().__init__(numero, titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
        else:
            print("Saldo e limite insuficientes")

class ContaPoupanca(Conta):
    def __init__(self, numero, titular, saldo, juros):
        super().__init__(numero, titular, saldo)
        self.juros = juros

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

'''
ERRO: não é possível criar objetos de classe abstrata
c = Conta(123, 'Paulo', 100)
'''

cc = ContaCorrente(123, 'Paulo', 100, 50)
cc.sacar(100)
cc.depositar(50)
print(f"Saldo: {cc.saldo}")

cp = ContaPoupanca(123, 'Paulo', 100, 0.02)
cp.sacar(200)
cp.depositar(50)
print(f"Saldo: {cp.saldo}")
