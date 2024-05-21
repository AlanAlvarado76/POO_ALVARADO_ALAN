peso = float(input("Ingrese el peso de su paquete: "))

if peso < 1:
    precio = 50
elif peso > 1 < 5: 
    precio = 100
elif peso > 5 < 10: 
    precio = 200
elif peso > 10: 
    precio = 500

print("El precio por el traslado de su paquete es: ", precio)