promedio1 = (input("Ingrese su primer promedio"))
promedio2 = (input("Ingrese su segundo promedio"))
promedio3 = (input("Ingrese su tercer promedio"))

if promedio1 > promedio2 and promedio3:
    print("el primer promedio es el mas alto ", promedio1)
elif promedio2 > promedio1 and promedio3:
    print("El segundo promedio ingresado es el mas alto", promedio2)
elif promedio3 > promedio1 and promedio2:
    print("El tercer promedio ingresado es el mas alto", promedio3)