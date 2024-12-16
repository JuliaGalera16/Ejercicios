numeros = []

for i in range(6):
    while True:
        try:
            numero = int(input(f"Introduce el numero ganador {i+1}: "))
            if 1 <= numero <= 49:
                numeros.append(numero)
                break
            else:
                print("Por favor, introduce un número entre el 1 y el 49")
        except ValueError:
            print("Por favor, introduce un número válido")
            
numeros.sort()


print("Los numeros ganadores son: ")
print(numeros)
                