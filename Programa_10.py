def main():
    while True:
        # Solicita los dos números al usuario
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        
        # Calcula la suma
        suma = num1 + num2
        
        # Muestra el resultado
        print(f"La suma de {num1} y {num2} es {suma}")
        
        # Pregunta al usuario si desea continuar
        continuar = input("¿Deseas realizar otra suma? (ingresa 'n' para detenerse, cualquier otra tecla para continuar): ")
        if continuar.lower() == 'n':
            break

if __name__ == "__main__":
    main()

    