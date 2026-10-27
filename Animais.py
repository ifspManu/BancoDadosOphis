import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ifsp", 
        database="Animais"  
    )

    cursor = mydb.cursor()

    print("--- Animais cadastrados no banco ---")
    cursor.execute("SELECT * FROM animal")
    results = cursor.fetchall()

    
    nomeCientifico = 'Panthera onca'
    nome = 'Onça-pintada'
    habitat = 'Florestas tropicais e pantanal'
    nivelPerigo = 'Alto'
    descricao = 'Maior felino das Américas, com pelagem amarelada e rosetas.'
    caracterFisic = 'Corpo robusto e mandíbula extremamente forte.'
    sobre = 'Excelente nadadora e caçadora no topo da cadeia alimentar.'


    #Escolher oq fazer
    escolha = int(input("1-inserir\n2-excluir\n3-consultar\n4-atualização\n5-fechar\nO que deseja fazer:"))

    #Inserir animal
    if(escolha==1):
        queryInserir = """INSERT INTO animal (nomeCientifico, nome, habitat, nivelPerigo, descricao, caracterFisic, sobre) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s)""" 
        dadosAnimais = (nomeCientifico, nome, habitat, nivelPerigo, descricao, caracterFisic, sobre)

        cursor.execute(queryInserir, dadosAnimais)
        mydb.commit()

        print('\nNovo animal inserido corretamente!')
        
    #Excluir animal
    elif(escolha==2):
        queryDelete = "DELETE FROM animal WHERE nomeCientifico=%s"
            
        cursor.execute(queryDelete, ('Panthera onca',))
        mydb.commit()
            
        print('\nRegistro excluído')

    #Consultar(não esta funcionando)
    elif(escolha==3):
        querySelect = "Select * FROM animal WHERE nomeCientifico=%s"

        cursor.execute(querySelect, ('Panthera onca',))
        mydb.commit()

    #Atualização(não esta dando certo)[nem sei oq é pra fazer aqui]
    else:
        print("ainda nao feito")

except Exception as err:
    print('Ocorreu um erro ao conectar ou manipular o banco de dados:')
    print(err)

finally:
    if 'mydb' in locals() and mydb.is_connected():
        cursor.close()
        mydb.close()
        print('Conexão fechada!')