from database.conexao import conectar
from dao.AnimalDAO import AnimalDAO
from model.AnimalModel import AnimalModel
from view.AnimalView import AnimalView
from controller.AnimalController import AnimalController

mydb = conectar()

dao = AnimalDAO(mydb)
model = AnimalModel(dao)
view = AnimalView()

controller = AnimalController(model, view)

controller.iniciar()

mydb.close()