def contar_letras_sem_espacos(string):
    contador = 0
    for caracter in string:
        if caracter != ' ':
            contador += 1
    return contador

class Endereco:
    def __init__(self, rua, numero, complemento, bairro, cidade, uf, cep):
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.cep = cep

class Cliente:
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco

class Pedido:
    def __init__(self, cliente, altura, largura, frase, cor_placa, cor_letra, valor_total = 0, valor_fixo_material=147.00, valor_fixo_letra=0.35):
        self.cliente = cliente
        self.altura = altura
        self.largura = largura
        self.frase = frase
        self.cor_placa = cor_placa
        self.cor_letra = cor_letra
        self.__valor_fixo_material = valor_fixo_material
        self.__valor_fixo_letra = valor_fixo_letra
        self.__valor_total = valor_total

    def get_valor_total(self):
        area = self.altura * self.largura
        custo_material = area * self.__valor_fixo_material
        custo_desenho = contar_letras_sem_espacos(self.frase) * self.__valor_fixo_letra
        valor_placa = custo_material + custo_desenho
        return valor_placa
    
class Historico:
    def __init__(self):
        self.__pedidos = []

    def inserir_pedido(self, pedido):
        if isinstance(pedido, Pedido):
            self.__pedidos.append(pedido)
        else:
            print("O objeto inserido não é um Pedido.")

    def calcular_faturamento(self):
        faturamento_total = 0
        for pedido in self.__pedidos:
            faturamento_total += pedido.get_valor_total()
        return faturamento_total


endereco1 = Endereco('Rua Padre Vicente de Araujo', '531', 'Casa', 'JD. Quisisana', 'São Paulo','SP', '08150580')
endereco2 = Endereco('Rua Padre Vicente', '53', 'Casa', 'JD. Quisisana', 'São Paulo','SP', '08150580')
cliente1 = Cliente('Guilherme', '11932196473', endereco1)
cliente2 = Cliente('Clara', '11932196473', endereco2)
pedido1 = Pedido(cliente1, 5, 6, 'Hello World', 'Branca', 'Preta')
pedido2 = Pedido(cliente2, 7, 8, 'Hello World', 'Branca', 'Preta')
print(pedido1.get_valor_total())
print(pedido2.get_valor_total())
historico = Historico()
historico.inserir_pedido(pedido1)
historico.inserir_pedido(pedido2)

faturamento = historico.calcular_faturamento()
print(f"Faturamento total: R${faturamento:.2f}")

lista_de_clientes = []



while True:
    print('1 - Cadastrar cliente')
    print('2 - Adicionar pedido')
    print('3 - Ver o valor total de um pedido')
    print('4 - Calcular faturamento de todos pedidos')
    print('5 - Finalizar programa')

    opcao = int(input('Escolha a opção que deseja:'))

    if opcao == 1:
        while True:
            nome = input('Digite o nome do cliente: ')
            try:
                telefone = int(input('Digite o telefone do cliente: '))
                if telefone <= 0:
                    raise ValueError
                if telefone >= 0:
                    break
            except Exception:
                print('Algum erro ocorreu')
        rua = input('Qual a rua do cliente: ')
        try:
            numero = int(input('Digite o numero da residência: '))
            if numero <= 0:
                raise ValueError
        except Exception:
            print('Algum erro ocorreu')
        complemento = input('Complemento: ')
        try:
            cep = int(input('Digite o cep: '))
            if cep <= 0:
                raise ValueError
        except Exception:
            print('Algum erro ocorreu')
        bairro = input('Bairro: ')
        cidade = input('Cidade: ')
        uf = input('Estado: ')
        
        endereco = Endereco(rua, numero, complemento, bairro, cidade, uf, cep)
        cliente = Cliente(nome, telefone, endereco)
        lista_de_clientes.append(cliente)
        print(f'Cliente {cliente.nome}, cadastrado(a) com sucesso !')

    elif opcao == 2:
        if not lista_de_clientes:
            print("Nenhum cliente cadastrado. Por favor, cadastre um cliente primeiro.")
            continue

        print('Clientes Disponiveis: ')
        for idx, cliente in enumerate(lista_de_clientes, start=1):
            print(f"{idx}. {cliente.nome}")

        escolha = int(input("Selecione o número do cliente para criar um pedido: ")) - 1

        if 0 <= escolha < len(lista_de_clientes):
            cliente_selecionado = lista_de_clientes[escolha]
            altura = float(input("Digite a altura: "))
            largura = float(input("Digite a largura: "))
            frase = input("Digite a frase: ")
            cor_placa = input("Digite a cor da placa: ")
            cor_letra = input("Digite a cor da letra: ")
            valor_total = 0
            pedido = Pedido(cliente_selecionado, altura, largura, frase, cor_placa, cor_letra, valor_total)
            historico.inserir_pedido(pedido)
            print('Pedido cadastrado com sucesso')

    elif opcao == 3:
        if not historico._Historico__pedidos:
            print("Nenhum pedido cadastrado. Por favor, cadastre um pedido primeiro.")
            continue

        print('Pedidos Disponíveis: ')
        for idx, pedido in enumerate(historico._Historico__pedidos, start=1):
            print(f"{idx}. Pedido do(a) cliente: {pedido.cliente.nome}")

        escolha = int(input("Selecione o número do pedido para ver o valor total: ")) - 1

        if 0 <= escolha < len(historico._Historico__pedidos):
            pedido_selecionado = historico._Historico__pedidos[escolha]
            valor_total_pedido = pedido_selecionado.get_valor_total()
            print(f'Valor total do pedido para cliente {pedido_selecionado.cliente.nome}: R${valor_total_pedido:.2f}')

    elif opcao == 4:
        if not historico._Historico__pedidos:
            print("Nenhum pedido cadastrado. Por favor, cadastre um pedido primeiro.")
            continue
        faturamento_total = historico.calcular_faturamento()
        print(f'Faturamento total de todos os pedidos: R${faturamento_total:.2f}')

    elif opcao == 5:
        print('Programa finalizado.')
        break

    else:
        print('Erro. opção incorreta.')
