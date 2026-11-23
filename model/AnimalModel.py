class AnimalModel:

    def __init__(self, dao):
        self.dao = dao

    def add_animal(self, nomeCientifico, nome, habitat,
                   nivelPerigo, descricao, caracterFisic, sobre):

        dados = (
            nomeCientifico, nome, habitat, nivelPerigo,
            descricao, caracterFisic, sobre
        )

        self.dao.inserir(dados)

    def delete_animal(self, nomeCientifico):
        return self.dao.excluir(nomeCientifico)

    def get_animal(self, nomeCientifico):
        return self.dao.consultar(nomeCientifico)

    def get_animais(self):
        return self.dao.listar()

    def update_animal(self, nomeCientifico, nome, habitat,
                      nivelPerigo, descricao, caracterFisic, sobre):

        dados = (
            nome, habitat, nivelPerigo,
            descricao, caracterFisic, sobre,
            nomeCientifico
        )

        return self.dao.atualizar(dados)