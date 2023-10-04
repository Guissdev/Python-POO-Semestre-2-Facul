# Atividade continua para a nota 2 

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

historico = Historico()
lista_de_clientes = []
cores_placa = ['branca', 'cinza']
cores_frase = ['azul', 'vermelha', 'amarelo', 'preto', 'verde']
estados = [
    "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA",
    "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN",
    "RS", "RO", "RR", "SC", "SP", "SE", "TO"
]

while True:
    print('1 - Cadastrar cliente')
    print('2 - Cadastrar pedido')
    print('3 - Ver o valor total de um pedido')
    print('4 - Calcular faturamento de todos pedidos')
    print('5 - Ver todos os clientes cadastrados')
    print('6 - ver todos os pedidos')
    print('7 - Excluir um cliente')
    print('8 - Excluir um pedido')
    print('0 - Sair do programa')

    try:
        opcao = int(input('Escolha a opção que deseja:'))
    except ValueError:
        print('Opção inválida. Por favor, digite um número válido.')
        continue

    if opcao == 1:
        nome = input('Digite o nome do cliente: ')
        while True:
            telefone = input('Digite o telefone do cliente (11 dígitos): ')
            if len(telefone) == 11 and telefone.isdigit():
                break
            else:
                print('Telefone inválido. Certifique-se de que possui exatamente 11 dígitos e contém apenas números.')

        rua = input('Qual a rua do cliente: ')
        while True:
            numero = input('Digite o numero da residência: ')
            if numero.isdigit():
                break
            else:
                print('Número inválido. Certifique-se de que contenha apenas números')
        complemento = input('Complemento: ')
        while True:
            cep = input('Digite o cep: ')
            if len(cep) == 8 and cep.isdigit():
                break
            else:
                print('Cep inválido. Certifique-se de que possui exatamente 8 dígitos e contém apenas números.')
        bairro = input('Bairro: ')
        cidade = input('Cidade: ')
        while True:
            uf = input('Estado (sigla): ')
            if uf.upper() in estados:
                break
            else:
                print('UF inválida. Por favor, digite a sigla do estado brasileiro.')
        
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
            while True:
                try:
                    altura = float(input("Digite a altura: "))
                    if altura > 0:
                        break
                except ValueError:
                    print("Altura inválida. Digite um número válido.")
            while True:
                try:
                    largura = float(input("Digite a largura: "))
                    if largura > 0:
                        break
                except ValueError:
                    print("Largura inválida. Digite um número válido.")
            frase = input("Digite a frase: ")
            while True:
                cor_placa = input("Digite a cor da placa (branca ou cinza): ").lower()
                if cor_placa in cores_placa:
                    break
                else:
                    print("Cor da placa inválida. Digite 'branca' ou 'cinza'.")
            while True:
                cor_frase = input("Digite a cor da letra (azul, vermelha, amarelo, preto ou verde): ").lower()
                if cor_frase in cores_frase:
                    break
                else:
                     print("Cor da letra inválida. Escolha entre azul, vermelha, amarelo, preto ou verde.")
            valor_total = 0
            pedido = Pedido(cliente_selecionado, altura, largura, frase, cor_placa, cor_frase, valor_total)
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
        if not lista_de_clientes:
            print("Nenhum cliente cadastrado ainda.")
        else:
            print("Clientes Cadastrados:")
        for idx, cliente in enumerate(lista_de_clientes, start=1):
            print(f"{idx}. Nome: {cliente.nome}, Telefone: {cliente.telefone}")

    elif opcao == 6:
        if not historico._Historico__pedidos:
            print("Nenhum pedido cadastrado ainda.")
        else:
            print("Pedidos Cadastrados:")
        for idx, pedido in enumerate(historico._Historico__pedidos, start=1):
            print(f"{idx}. Cliente: {pedido.cliente.nome}, Altura: {pedido.altura}, Largura: {pedido.largura}, Cor Placa: {pedido.cor_placa}, Cor Letra: {pedido.cor_letra}")

    elif opcao == 7:
        if not lista_de_clientes:
            print("Nenhum cliente cadastrado. Não há clientes para excluir.")
        else:
            print("Clientes Cadastrados:")
            for idx, cliente in enumerate(lista_de_clientes, start=1):
                print(f"{idx}. Nome: {cliente.nome}")

            escolha = int(input("Selecione o número do cliente que deseja excluir: ")) - 1

            if 0 <= escolha < len(lista_de_clientes):
                cliente_a_excluir = lista_de_clientes[escolha]
                num_pedidos_cliente = sum(1 for pedido in historico._Historico__pedidos if pedido.cliente == cliente_a_excluir)

                print(f'O cliente {cliente_a_excluir.nome} possui {num_pedidos_cliente} pedidos.')

                while True:
                    confirmacao = input(f'Tem certeza que deseja excluir o cliente {cliente_a_excluir.nome} que tem {num_pedidos_cliente} pedidos? (Sim/Não/S/N): ').lower()
                    if confirmacao in ['sim', 'não', 's', 'n']:
                        break
                    else:
                        print('Resposta inválida. Digite "Sim", "Não", "S" ou "N".')

                if confirmacao in ['sim', 's']:
                    lista_de_clientes.pop(escolha)
                    print(f'Cliente {cliente_a_excluir.nome} excluído com sucesso.')

                    historico._Historico__pedidos = [pedido for pedido in historico._Historico__pedidos if pedido.cliente != cliente_a_excluir]
                    print(f'Todos os pedidos do cliente {cliente_a_excluir.nome} também foram excluídos.')
                else:
                    print('Exclusão cancelada.')

    elif opcao == 8:
        if not historico._Historico__pedidos:
            print("Nenhum pedido cadastrado. Não há pedidos para excluir.")
        else:
            print("Pedidos Cadastrados:")
            for idx, pedido in enumerate(historico._Historico__pedidos, start=1):
                print(f"{idx}. Cliente: {pedido.cliente.nome}, Altura: {pedido.altura}, Largura: {pedido.largura}, Cor Placa: {pedido.cor_placa}, Cor Letra: {pedido.cor_letra}")

            escolha = int(input("Selecione o número do pedido que deseja excluir: ")) - 1
            if 0 <= escolha < len(historico._Historico__pedidos):
                pedido_a_excluir = historico._Historico__pedidos.pop(escolha)
                print('Pedido excluído com sucesso.')

    elif opcao == 0:
        print('Programa Finalizado !')
        break

    else:
        print('Opção inválida tente novamente')