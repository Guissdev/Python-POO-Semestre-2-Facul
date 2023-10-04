
class Veiculo:
    def __init__(self, marca, modelo, placa):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa

    def exibir(self):
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Placa: {self.placa}')

class Carro(Veiculo):               # Carro herda do Veiculo
    def __init__(self, marca, modelo, placa, portas):
        super().__init__(marca, modelo, placa)
        self.portas = portas

    def exibir(self):
        super().exibir()
        print(f'Qtd de portas: {self.portas}')

class Moto(Veiculo):                # Moto herda do Veiculo
    def __init__(self, marca, modelo, placa, bagageiro):
        super().__init__(marca, modelo, placa)
        self.bagageiro = bagageiro

    def exibir(self):
        super().exibir()
        print(f'Bagageiro : {self.bagageiro}')


carro1 = Carro('Ford', 'Ka', 'ABC-1234', 4)
carro1.exibir()

moto1 = Moto('Honda', 'CG', 'DFG-3456', True)
moto1.exibir()