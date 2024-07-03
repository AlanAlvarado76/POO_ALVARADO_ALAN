class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")


class Pasajero(Persona):
    def __init__(self, nombre, edad, pasaporte):
        super().__init__(nombre, edad)
        self.pasaporte = pasaporte

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Pasaporte: {self.pasaporte}")


class Empleado(Persona):
    def __init__(self, nombre, edad, id_empleado):
        super().__init__(nombre, edad)
        self.id_empleado = id_empleado

    def mostrar_info(self):
        super().mostrar_info()
        print(f"ID Empleado: {self.id_empleado}")


class Vuelo:
    def __init__(self, numero_vuelo, destino):
        self.numero_vuelo = numero_vuelo
        self.destino = destino
        self.pasajeros = []
        self.empleados = []

    def agregar_pasajero(self, pasajero):
        self.pasajeros.append(pasajero)

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def mostrar_info(self):
        print(f"Vuelo {self.numero_vuelo} con destino a {self.destino}")
        print("Pasajeros:")
        for pasajero in self.pasajeros:
            pasajero.mostrar_info()
        print("Empleados:")
        for empleado in self.empleados:
            empleado.mostrar_info()


class Avion:
    def __init__(self, modelo):
        self.modelo = modelo
        self.vuelos = []

    def agregar_vuelo(self, vuelo):
        self.vuelos.append(vuelo)

    def mostrar_info(self):
        print(f"Modelo de avión: {self.modelo}")
        for vuelo in self.vuelos:
            vuelo.mostrar_info()


class Aeropuerto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.aviones = []

    def agregar_avion(self, avion):
        self.aviones.append(avion)

    def mostrar_info(self):
        print(f"Aeropuerto: {self.nombre}")
        for avion in self.aviones:
            avion.mostrar_info()


class Terminal:
    def __init__(self, numero, aeropuerto):
        self.numero = numero
        self.aeropuerto = aeropuerto

    def mostrar_info(self):
        print(f"Terminal {self.numero} en el aeropuerto {self.aeropuerto.nombre}")


class Itinerario:
    def __init__(self, pasajero, vuelo):
        self.pasajero = pasajero
        self.vuelo = vuelo

    def mostrar_info(self):
        print("Itinerario:")
        self.pasajero.mostrar_info()
        self.vuelo.mostrar_info()


# Creación de objetos
pasajero1 = Pasajero("Juan", 30, "A123456")
pasajero2 = Pasajero("Maria", 25, "B654321")
empleado1 = Empleado("Carlos", 40, "E001")
empleado2 = Empleado("Ana", 35, "E002")
vuelo1 = Vuelo("V001", "New York")
vuelo2 = Vuelo("V002", "Paris")
avion1 = Avion("Boeing 737")
avion2 = Avion("Airbus A320")
aeropuerto = Aeropuerto("Aeropuerto Internacional")
terminal1 = Terminal(1, aeropuerto)
terminal2 = Terminal(2, aeropuerto)
itinerario1 = Itinerario(pasajero1, vuelo1)
itinerario2 = Itinerario(pasajero2, vuelo2)

# Agregar relaciones
vuelo1.agregar_pasajero(pasajero1)
vuelo1.agregar_empleado(empleado1)
vuelo2.agregar_pasajero(pasajero2)
vuelo2.agregar_empleado(empleado2)
avion1.agregar_vuelo(vuelo1)
avion2.agregar_vuelo(vuelo2)
aeropuerto.agregar_avion(avion1)
aeropuerto.agregar_avion(avion2)


def clear_screen():
    print("\033c", end="")

# Menú interactivo
def mostrar_menu():
    print("\nMenu:")
    print("1. Mostrar información del aeropuerto")
    print("2. Mostrar información de un avión")
    print("3. Mostrar información de un vuelo")
    print("4. Mostrar información de un pasajero")
    print("5. Mostrar información de un empleado")
    print("6. Mostrar itinerario de un pasajero")
    print("7. Salir")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
         clear_screen()
         aeropuerto.mostrar_info()
    elif opcion == "2":
        clear_screen()
        avion_num = input("Ingrese el número del avión (1 o 2): ")
        if avion_num == "1":
            clear_screen()
            avion1.mostrar_info()
        elif avion_num == "2":
            clear_screen()
            avion2.mostrar_info()
        else:
            clear_screen()
            print("Opción no válida.")
            
    elif opcion == "3":
        clear_screen()
        vuelo_num = input("Ingrese el número del vuelo (V001 o V002): ")
        
        if vuelo_num == "V001":
            clear_screen()
            vuelo1.mostrar_info()
            
        elif vuelo_num == "V002":
            clear_screen()
            vuelo2.mostrar_info()
            
        else:
            clear_screen()
            print("Opción no válida.")
            
    elif opcion == "4":
        clear_screen()
        pasajero_nombre = input("Ingrese el nombre del pasajero (Juan o Maria): ")
        
        if pasajero_nombre == "Juan":
            clear_screen()
            pasajero1.mostrar_info()
            
        elif pasajero_nombre == "Maria":
            clear_screen()
            pasajero2.mostrar_info()
            
        else:
            clear_screen()
            print("Opción no válida.")
            
    elif opcion == "5":
        clear_screen()
        empleado_nombre = input("Ingrese el nombre del empleado (Carlos o Ana): ")
        
        if empleado_nombre == "Carlos":
            clear_screen()
            empleado1.mostrar_info()
            
        elif empleado_nombre == "Ana":
            clear_screen()
            empleado2.mostrar_info()
            
        else:
            clear_screen()
            print("Opción no válida.")
            
    elif opcion == "6":
        clear_screen()
        itinerario_nombre = input("Ingrese el nombre del pasajero (Juan o Maria): ")
        
        if itinerario_nombre == "Juan":
            clear_screen()
            itinerario1.mostrar_info()
            
        elif itinerario_nombre == "Maria":
            clear_screen()
            itinerario2.mostrar_info()
            
        else:
            clear_screen()
            print("Opción no válida.")
        
    elif opcion == "7":
        clear_screen()
        print("Saliendo...")
        break
    else:
        print("Opción no válida.")