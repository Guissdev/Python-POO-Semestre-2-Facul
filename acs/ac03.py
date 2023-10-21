class SuperPoder:
    def __init__(self, nome, categoria):
        self.__nome = nome
        self.__categoria = categoria

    def get_nome(self):
        return self.__nome
    
    def get_categoria(self):
        return self.__categoria
    
class Personagem:
    def __init__(self, nome, nome_vida_real):
        self.__nome = nome
        self.__nome_vida_real = nome_vida_real
        self.__poderes = []

    def adicionar_super_poder(self, superpoder):
        self.__poderes.append(superpoder)

    def get_poder_total(self):
        poder_total = 0
        for p in self.__poderes:
            poder_total += p.get_categoria()
        return poder_total
    
class SuperHeroi(Personagem):
    def __init__(self, nome, nome_vida_real):
        super().__init__(nome, nome_vida_real)

    def get_poder_total(self):
        return super().get_poder_total() * 1.10
    
class Vilao(Personagem):
    def __init__(self, nome, nome_vida_real, tempo_de_prisao):
        super().__init__(nome, nome_vida_real)
        self.tempo_de_prisao = tempo_de_prisao

class Confronto:
    pass

    def lutar(self, superheroi, vilao):
        poder_total_heroi = superheroi.get_poder_total()
        poder_total_vilao = vilao.get_poder_total()

        if poder_total_heroi == poder_total_vilao:
            return 0
        elif poder_total_heroi > poder_total_vilao:
            return 1
        else:
            return 2
        
lista_de_super_herois = []
lista_de_viloes = []
        
while True:
    print("1 - Criar um heroi")
    print("2 - Criar um vilão")
    print("3 - Adicionar poderes a um heroi")
    print("4 - Adicionar poderes a um vilão")
    print("5 - Ver todos os herois")
    print("6 - Ver todos os vilões")
    print("7 - Realizar um confronto")
    print("0 - Finalizar")

    try:
        opcao = int(input('Escolha a opção que deseja:'))
    except ValueError:
        print('Opção inválida. Por favor, digite um número válido.')
        continue

    if opcao == 1:
        nome = input('Digite o nome do super-heroi: ')
        nome_real = input('Digite o nome na vida real do heroi: ')
        personagem = Personagem(nome, nome_real)
        heroi = SuperHeroi(personagem)
        lista_de_super_herois.append(heroi)
        print(f'{nome} foi criado como super-heroi.')

    elif opcao == 2:
        nome = input('Digite o nome do vilão: ')
        nome_real = input('Digite o nome na vida real do vilão: ')
        while True:
            try:
                tempo_de_prisao = int(input('Digite o tempo de prisão do vilão (em anos): '))
                break
            except ValueError:
                print('Entrada inválida. Por favor, digite um número válido.')
        personagem = Personagem(nome, nome_real)
        vilao = Vilao(personagem, tempo_de_prisao)
        lista_de_viloes.append(vilao)
        print(f'{nome} foi criado como vilão.')
    
    elif opcao == 3:
        if not lista_de_super_herois:
            print("Nenhum herói foi criado ainda, crie um heroi primeiro")
            continue

        print("Herois disponíveis: ")
        for idx, heroi in enumerate(lista_de_super_herois, start=1):
            print(f"{idx}. {heroi.nome}")

        escolha = int(input("Selecione o heroi que deseja adicionar um poder: ")) - 1

        if 0 <= escolha < len(lista_de_super_herois):
            heroi_selecionado = lista_de_super_herois[escolha]

            nome_superpoder = input("Digite o nome do novo super poder: ")
            categoria_superpoder = int(input("Digite a categoria do SuperPoder (entre 1 e 5): "))

            if 1 <= categoria_superpoder <= 5:
                novo_superpoder = SuperPoder(nome_superpoder, categoria_superpoder)
                heroi_selecionado.adicionar_super_poder(novo_superpoder)
                print(f"O SuperPoder '{nome_superpoder}' foi adicionado ao heroi '{heroi_selecionado.nome}'.")
            else:
                print("A categoria do super poder deve estar entre 1 e 5.")
        else:
            print("Opção inválida. Selecione um heroi existente.")

    elif opcao == 4:
        if not lista_de_viloes:
            print("Nenhum vilão foi criado ainda, crie um vilão primeiro")
            continue

        print("Vilões disponíveis: ")
        for idx, vilao in enumerate(lista_de_viloes, start=1):
            print(f"{idx}. {vilao.nome}")

        escolha = int(input("Selecione o vilão que deseja adicionar um poder: ")) - 1

        if 0 <= escolha < len(lista_de_viloes):
            vilao_selecionado = lista_de_viloes[escolha]

            nome_superpoder = input("Digite o nome do novo super poder: ")
            categoria_superpoder = int(input("Digite a categoria do SuperPoder (entre 1 e 5): "))

            if 1 <= categoria_superpoder <= 5:
                novo_superpoder = SuperPoder(nome_superpoder, categoria_superpoder)
                vilao_selecionado.adicionar_super_poder(novo_superpoder)
                print(f"O SuperPoder '{nome_superpoder}' foi adicionado ao vilao '{vilao_selecionado.nome}'.")
            else:
                print("A categoria do super poder deve estar entre 1 e 5.")
        else:
            print("Opção inválida. Selecione um vilao existente.")
    
    elif opcao == 5:
        if not lista_de_super_herois:
            print("Nenhum heroi foi criado ainda.")
        else:
            print("Todos os herois:")
        for idx, heroi in enumerate(lista_de_super_herois, start=1):
            print(f"{idx}. Nome: {heroi.nome}")

    elif opcao == 6:
        if not lista_de_viloes:
            print("Nenhum vilao foi criado ainda.")
        else:
            print("Todos os vilões:")
        for idx, vilao in enumerate(lista_de_viloes, start=1):
            print(f"{idx}. Nome: {vilao.nome}")

    elif opcao == 7:
        if not lista_de_super_herois or not lista_de_viloes:
            print("É necessário criar pelo menos um heroi e um vilão para realizar um confronto.")
            continue

        print("Heróis disponíveis: ")
        for idx, heroi in enumerate(lista_de_super_herois, start=1):
            print(f"{idx}. {heroi.nome}")

        escolha_heroi = int(input("Selecione o heroi para o confronto: ")) - 1

        if 0 <= escolha_heroi < len(lista_de_super_herois):
            heroi_selecionado = lista_de_super_herois[escolha_heroi]
        else:
            print("Opção inválida. Selecione um heroi existente.")
            continue

        print("Vilões disponíveis: ")
        for idx, vilao in enumerate(lista_de_viloes, start=1):
            print(f"{idx}. {vilao.nome}")

        escolha_vilao = int(input("Selecione o vilão para o confronto: ")) - 1

        if 0 <= escolha_vilao < len(lista_de_viloes):
            vilao_selecionado = lista_de_viloes[escolha_vilao]
        else:
            print("Opção inválida. Selecione um vilao existente.")
            continue

        confronto = Confronto()
        resultado = confronto.lutar(heroi_selecionado, vilao_selecionado)

        if resultado == 0:
            print("O confronto terminou em empate!")
        elif resultado == 1:
            print(f"{heroi_selecionado.nome} venceu o confronto!")
        else:
            print(f"{vilao_selecionado.nome} venceu o confronto!")

    elif opcao == 0:
        print('Programa Finalizado !')
        break

    else:
        print('Opção inválida tente novamente')