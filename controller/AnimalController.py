class AnimalController:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def iniciar(self):

        # Cadastrar Onça-pintada caso não exista
        animal = self.model.get_animal("Panthera onca")

        if animal:
            self.view.mensagem(
                "Onça-pintada já está cadastrada"
            )
        else:
            self.model.add_animal(
                "Panthera onca",
                "Onça-pintada",
                "Florestas tropicais e pantanal",
                "Alto",
                "Maior felino das Américas, com pelagem amarelada e rosetas.",
                "Corpo robusto e mandíbula extremamente forte.",
                "Excelente nadadora e caçadora no topo da cadeia alimentar."
            )

            self.view.mensagem("Onça-pintada cadastrada!")

        # Mostrar animais cadastrados
        animais = self.model.get_animais()
        self.view.display_animais(animais)

        # Menu principal
        i=0
        while (i==0):

            escolha = self.view.menu()

            # Inserir
            if escolha == 1:

                dados = self.view.inserir_animal()

                self.model.add_animal(*dados)

                self.view.mensagem(
                    "Novo animal inserido corretamente!"
                )

            # Excluir
            elif escolha == 2:

                nomeCientifico = self.view.nome_para_busca()

                resultado = self.model.delete_animal(
                    nomeCientifico
                )

                if resultado > 0:
                    self.view.mensagem(
                        "Registro excluído com sucesso!"
                    )
                else:
                    self.view.mensagem(
                        "Animal não encontrado!"
                    )

            # Consultar
            elif escolha == 3:

                nomeCientifico = self.view.nome_para_busca()

                animal = self.model.get_animal(
                    nomeCientifico
                )

                if animal:
                    self.view.display_animal(animal)
                else:
                    self.view.mensagem(
                        "Animal não encontrado!"
                    )

            # Atualizar
            elif escolha == 4:

                nomeCientifico = self.view.nome_para_busca()

                animal = self.model.get_animal(
                    nomeCientifico
                )

                if animal:

                    dados = self.view.atualizar_animal()

                    self.model.update_animal(
                        nomeCientifico, *dados
                    )

                    self.view.mensagem(
                        "Animal atualizado com sucesso!"
                    )

                else:
                    self.view.mensagem(
                        "Animal não encontrado!"
                    )

            # Listar todos os animais cadastrados
            elif escolha == 5:

                animais = self.model.get_animais()

                if animais:
                    self.view.display_animais(animais)
                else:
                    self.view.mensagem(
                        "Nenhum animal cadastrado!"
                    )

            # Fechar
            elif escolha == 6:
                self.view.mensagem(
                    "Programa encerrado!"
                )
                i+=1

            else:
                self.view.mensagem(
                    "Opção inválida!"
                )