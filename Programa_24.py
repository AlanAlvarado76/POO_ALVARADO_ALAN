class Piloto:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        self.carros = []

    

    def acelerar(self):
        print("acelerando")

    def frenar(self):
        print("Frenando")
    
    def reabastecer(self):
        print("Reabasteciendose")

    def añadir_carro(self,carro):
        self.carros.append(carro)

    def llenar_lista(self):
        print(self.nombre, "tiene los siguientes: ")
        for carro in self.carros:
            Carro.encender()

class Carro:
    def __init__(self,marca, modelo, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.kilmetraje = kilometraje



    def encender(self):
        print("encendiendo")

    def apagar(self):
        print("apagando")


piloto1 = Piloto("Alan", "19")
piloto2 = Piloto("Checo", 29)
piloto3 = Piloto("Lewis", 25)

carro1 = Carro("Ford","Mustang",25000)
carro2 = Carro("Ferrari", "Laferrari", 30000)
carro3 = Carro("Mercedez","Clase G", 15000)

Piloto.llenar_lista()