while True:
    eleccion = int(input("¿De que figura desea obtener el area: 1. cuadrado, 2. trangulo  3.rectangulo 4. para salir del programa?"))
    if eleccion == 1:
        lado_cuadrado = float(input("Ingrese el lado del cuadrado"))
        area_cuadrado = lado_cuadrado * lado_cuadrado
        print("El area del cuadrado es: ", area_cuadrado)
    elif eleccion == 2:
        base_triangulo = float(input("Ingrese la base del triangulo"))
        altura_triangulo = float(input("Ingrese la altura del triangulo"))
        area_triangulo = base_triangulo * altura_triangulo / 2
        print("el area del triangulo es: ", area_triangulo)
    elif eleccion == 3:
        base_rectangulo = float(input("Ingrese el area del reectangulo"))
        altura_rectangulo = float(input("Ingrese la altura del rectangulo"))
        area_rectangulo = base_rectangulo * altura_rectangulo
        print ("El area del rectangulo es la siguiente: ", area_rectangulo)
    else:
        print("saliendo  del programa")
        break
    
