class Piloto:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        self.carros = []
        self.neumatico = None
        
    def acelerar(self):
        print("acelerando")

    def frenar(self):
        print("Frenando")
    
    def reabastecer(self):
        print("Reabasteciendose")

    def añadir_carro(self,carro):
        self.carros.append(carro)

    def llenar_lista_carros(self):
        print(self.nombre, "tiene los siguientes: ")
        for carro in self.carros:
            print(self.carros)

    def describir(self, neumatico):
        print("Me llamo ", self.nombre,"Manejo", self.carros,"Y mi edad es:", self.edad)
        if self.neumatico:
            print("lleva puesto un neumatico de marca: ", self.marca)
        
        

class Carro:
    def __init__(self,marca, modelo, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.kilometraje = kilometraje
    def encender(self):
        print("encendiendo")
        
    def apagar(self):
        print("apagando")

    def describir(self, neumatico):
        print("Es un carro", self.marca,"modelo", self.modelo,"Y mi kilometraje es de:", self.kilometraje)
        if self.neumatico:
            print("lleva puesto un neumatico de marca: ", self.marca)



class Mecanico:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        self.carros = []

    def reparar(self):
        print("reparando")

    def añadir_carro(self, carro):
        self.carros.append(carro)

    def lista_carro_reparados(self):
        print(self.nombre,"Ha reparado los siguientes autos:")
        for carro in self.carros:
            print(self.carros)

class Neumaticos:
    def __init__(self, marca):
        self.marca = marca
     
        


        


piloto1 = Piloto("Alan", 19)
piloto2 = Piloto("Checo", 29)
piloto3 = Piloto("Lewis", 25)

carro1 = Carro("Ford","Mustang",25000)
carro2 = Carro("Ferrari", "Laferrari", 30000)
carro3 = Carro("Mercedez","Clase G", 15000)

mecanico1 = Mecanico("Franco", 35)
mecanico2 = Mecanico("Roberto", 24)
mecanico3 = Mecanico("Lucas", 45)

neumatico1 = Neumaticos("Michelin")
neumatico2 = Neumaticos("Toyotires")
neumatico3 = Neumaticos("Bridgestone", "liso")
