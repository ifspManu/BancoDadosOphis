import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ifsp",
        database="Animais"
    )

    cursor = mydb.cursor()

    # Cadastrar Onça-pintada
    nomeCientifico = 'Panthera onca'
    nome = 'Onça-pintada'
    habitat = 'Florestas tropicais e pantanal'
    nivelPerigo = 'Alto'
    descricao = 'Maior felino das Américas, com pelagem amarelada e rosetas.'
    caracterFisic = 'Corpo robusto e mandíbula extremamente forte.'
    sobre = 'Excelente nadadora e caçadora no topo da cadeia alimentar.'

    queryInserir = """INSERT INTO animal (nomeCientifico, nome, habitat, nivelPerigo, descricao, caracterFisic, sobre) VALUES (%s, %s, %s, %s, %s, %s, %s)"""

    dadosAnimais = (nomeCientifico, nome, habitat, nivelPerigo, descricao, caracterFisic, sobre)

    cursor.execute("SELECT * FROM animal WHERE nomeCientifico = %s", ('Panthera onca',))

    animal = cursor.fetchone()

    if (bool(animal) == True):
        print("Onça-pintada já está cadastrada")
    else:
        cursor.execute(queryInserir, dadosAnimais)
        mydb.commit()
        print("Onça-pintada cadastrada")

    #Mostrar animais
    print("--- Animais cadastrados no banco ---")
    cursor.execute("SELECT * FROM animal")
    results = cursor.fetchall()


    for animal in results:
        print(animal)

    i = 0
    while (i == 0):
        #escolhe oq fazer
        escolha = int(input("1-inserir\n2-excluir\n3-consultar\n4-atualização\n5-fechar\nO que deseja fazer:"))

        #Inserir animal
        if (escolha == 1):

            nomeCientifico = input("Nome científico: ")
            nome = input("Nome popular: ")
            habitat = input("Habitat: ")
            nivelPerigo = input("Nível de perigo: ")
            descricao = input("Descrição: ")
            caracterFisic = input("Características físicas: ")
            sobre = input("Sobre o animal: ")

            queryInserir = """INSERT INTO animal (nomeCientifico, nome, habitat, nivelPerigo,descricao, caracterFisic, sobre) VALUES (%s, %s, %s, %s, %s, %s, %s)"""

            dadosAnimais = (nomeCientifico, nome, habitat, nivelPerigo, descricao, caracterFisic, sobre)

            cursor.execute(queryInserir, dadosAnimais)
            mydb.commit()

            print("\nNovo animal inserido corretamente!")

        #Excluir animal
        elif (escolha == 2):

            nomeCientifico = input("Digite o nome científico do animal que deseja excluir: ")

            queryDelete = """DELETE FROM animal WHERE nomeCientifico = %s"""

            cursor.execute(queryDelete, (nomeCientifico,))
            mydb.commit()

            if cursor.rowcount > 0:
                print("\nRegistro excluído com sucesso!")
            else:
                print("\nAnimal não encontrado!")

        #Consultar animal
        elif (escolha == 3):

            nomeCientifico = input("Digite o nome científico do animal que deseja consultar: ")

            querySelect = """SELECT * FROM animal WHERE nomeCientifico = %s"""

            cursor.execute(querySelect, (nomeCientifico,))
            results = cursor.fetchall()

            if (bool(results) == True):
                print("\n--- Animal encontrado ---")

                for animal in results:
                    print("Nome científico:", animal[0])
                    print("Nome:", animal[1])
                    print("Habitat:", animal[2])
                    print("Nível de perigo:", animal[3])
                    print("Descrição:", animal[4])
                    print("Características físicas:", animal[5])
                    print("Sobre:", animal[6])
            else:
                print("\nAnimal não encontrado!")

        #Atualizar animal
        elif (escolha == 4):

            nomeCientifico = input("Digite o nome científico do animal que deseja atualizar: ")

            cursor.execute("SELECT * FROM animal WHERE nomeCientifico = %s", (nomeCientifico,))

            animal = cursor.fetchone()

            if (bool(animal) == True):

                print("\nDigite os novos dados do animal:")

                nome = input("Novo nome popular: ")
                habitat = input("Novo habitat: ")
                nivelPerigo = input("Novo nível de perigo: ")
                descricao = input("Nova descrição: ")
                caracterFisic = input("Novas características físicas: ")
                sobre = input("Novas informações: ")

                queryUpdate = """
                UPDATE animal
                SET nome = %s, habitat = %s, nivelPerigo = %s, descricao = %s, caracterFisic = %s, sobre = %s 
                WHERE nomeCientifico = %s"""

                dadosAtualizados = (nome, habitat, nivelPerigo, descricao, caracterFisic, sobre, nomeCientifico)

                cursor.execute(queryUpdate, dadosAtualizados)
                mydb.commit()

                print("\nAnimal atualizado com sucesso!")

            else:
                print("\nAnimal não encontrado!")

        #Fechar
        else:
            i = 1

except Exception as err:
    print("Ocorreu um erro ao conectar ou manipular o banco de dados:")
    print(err)

finally:
    if 'mydb' in locals() and mydb.is_connected():
        cursor.close()
        mydb.close()
        print("Conexão fechada!")