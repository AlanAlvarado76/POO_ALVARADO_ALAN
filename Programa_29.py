def abstraccion():
    print("\nAbstracción:")
    print("La abstracción es el proceso de ocultar los detalles complejos de implementación y mostrar solo la funcionalidad esencial.")
    print("En Python, se puede lograr usando clases y métodos abstractos.\n")

def encapsulamiento():
    print("\nEncapsulamiento:")
    print("El encapsulamiento es el mecanismo que restringe el acceso directo a los atributos y métodos de una clase.")
    print("En Python, se puede implementar mediante variables y métodos privados utilizando un guion bajo (_).\n")

def herencia():
    print("\nHerencia:")
    print("La herencia permite que una clase derive o herede propiedades y comportamientos de otra clase.")
    print("En Python, se define una clase hija que hereda de una clase padre usando paréntesis. Ejemplo: class Hija(Padre):\n")

def polimorfismo():
    print("\nPolimorfismo:")
    print("El polimorfismo permite que un mismo método o función se comporte de diferentes maneras según el contexto.")
    print("En Python, se puede lograr mediante el uso de métodos con el mismo nombre en diferentes clases, o mediante la sobrecarga de operadores.\n")

def menu():
    while True:
        print("Menú:")
        print("1. Abstracción")
        print("2. Encapsulamiento")
        print("3. Herencia")
        print("4. Polimorfismo")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            abstraccion()
        elif opcion == '2':
            encapsulamiento()
        elif opcion == '3':
            herencia()
        elif opcion == '4':
            polimorfismo()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

menu()
