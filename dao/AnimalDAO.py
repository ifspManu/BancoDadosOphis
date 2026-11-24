class AnimalDAO:

    def __init__(self, mydb):
        self.mydb = mydb

    #Cadastrar animal
    def inserir(self, dados):
        cursor = self.mydb.cursor()

        query = """
        INSERT INTO animal
        (nomeCientifico, nome, habitat, nivelPerigo,
        descricao, caracterFisic, sobre)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(query, dados)
        self.mydb.commit()
        cursor.close()

    #Excluir animal
    def excluir(self, nomeCientifico):
        cursor = self.mydb.cursor()

        query = """
        DELETE FROM animal
        WHERE nomeCientifico = %s
        """

        cursor.execute(query, (nomeCientifico,))
        self.mydb.commit()

        resultado = cursor.rowcount
        cursor.close()

        return resultado

    #Consultar animal
    def consultar(self, nomeCientifico):
        cursor = self.mydb.cursor()

        query = """
        SELECT * FROM animal
        WHERE nomeCientifico = %s
        """

        cursor.execute(query, (nomeCientifico,))
        animal = cursor.fetchone()

        cursor.close()
        return animal

    #Listar todos os animais
    def listar(self):
        cursor = self.mydb.cursor()

        cursor.execute("SELECT * FROM animal")
        animais = cursor.fetchall()

        cursor.close()
        return animais

    #Atualizar animal
    def atualizar(self, dados):
        cursor = self.mydb.cursor()

        query = """
        UPDATE animal
        SET nome = %s,
            habitat = %s,
            nivelPerigo = %s,
            descricao = %s,
            caracterFisic = %s,
            sobre = %s
        WHERE nomeCientifico = %s
        """

        cursor.execute(query, dados)
        self.mydb.commit()

        resultado = cursor.rowcount
        cursor.close()

        return resultado