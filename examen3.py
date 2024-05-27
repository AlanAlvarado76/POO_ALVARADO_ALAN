lista_edades = [6,5,11,18,22,28,16,7,15,11,34,23,45]

infancia = []
adolescentes = []
jovenes = []
adultos = []

for edad in lista_edades:
    if edad < 11:
        infancia.append(edad)
    elif edad > 12 and edad < 17:
        adolescentes.append(edad)
    elif edad > 18 and edad < 26:
        jovenes.append(edad)
    elif edad > 27:
        adultos.append(edad)

print(infancia, adolescentes, jovenes, adultos)