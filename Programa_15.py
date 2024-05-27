lista_edades = [12, 14, 15, 18, 20, 13, 22, 34]

mayores_edad = []
menores_edad = []

for edad in lista_edades:
    if edad < 18:
        menores_edad.append(edad)
    else:
        mayores_edad.append(edad)

print (mayores_edad)
print (menores_edad)

