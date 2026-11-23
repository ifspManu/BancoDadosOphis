class AnimalView:

    def menu(self):
        print("\n1 - Inserir")
        print("2 - Excluir")
        print("3 - Consultar")
        print("4 - Atualizar")
        print("5 - Fechar")

        return int(input("O que deseja fazer: "))

    def inserir_animal(self):
        nomeCientifico = input("Nome científico: ")
        nome = input("Nome popular: ")
        habitat = input("Habitat: ")
        nivelPerigo = input("Nível de perigo: ")
        descricao = input("Descrição: ")
        caracterFisic = input("Características físicas: ")
        sobre = input("Sobre o animal: ")

        return (
            nomeCientifico, nome, habitat, nivelPerigo,
            descricao, caracterFisic, sobre
        )

    def nome_para_busca(self):
        return input(
            "Digite o nome científico do animal: "
        )

    def atualizar_animal(self):
        nome = input("Novo nome popular: ")
        habitat = input("Novo habitat: ")
        nivelPerigo = input("Novo nível de perigo: ")
        descricao = input("Nova descrição: ")
        caracterFisic = input("Novas características físicas: ")
        sobre = input("Novas informações: ")

        return (
            nome, habitat, nivelPerigo,
            descricao, caracterFisic, sobre
        )

    def display_animais(self, animais):
        print("\n--- Animais cadastrados ---")

        for animal in animais:
            print(animal)

    def display_animal(self, animal):
        print("\n--- Animal encontrado ---")
        print("Nome científico:", animal[0])
        print("Nome:", animal[1])
        print("Habitat:", animal[2])
        print("Nível de perigo:", animal[3])
        print("Descrição:", animal[4])
        print("Características físicas:", animal[5])
        print("Sobre:", animal[6])

    def mensagem(self, texto):
        print(texto)