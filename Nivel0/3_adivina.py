import random





# version A: 1 intento
def version_a():
    numero_secreto=random.randint(1,50)
    print("Solo tienes un intento para adivinar el número")
    intento = int(input("Introduce un número de 1 a 50: "))
    if intento == numero_secreto:
        print("¡Lo has acertado!")
    else:
        print("Lo siento, el número era " + str(numero_secreto))
        

# version B: 10 intentos
def version_b():
    print("Tienes 10 intentos para adivinar el número")
    numero_secreto=random.randint(1,50)
    for i in range(10):
        
        intento = int(input("Introduce un número de 1 a 50: "))
        if intento == numero_secreto:
            print("¡Lo has acertado!")
            break
        else:
            print("Intentos restantes: " + str(10-i-1))
    else:
            print(f"Has agotado tus intentos, el numero era el "+ str(numero_secreto))
            
            
# version C: Sin límite de intentos
def version_c():
    while True:
        numero_secreto=random.randint(1,50)
        intento = int(input("Introduce un número de 1 a 50: "))
        if intento == numero_secreto:
            print("¡Lo has acertado!")
            break
        else:
            print("No es ese el número, sigue intentándolo")
            

# ejecucion de las versiones

if __name__ == "__main__":
    print("¿Qué versión de juego quieres jugar?")
    print("A) 1 intento")
    print("B) 10 intentos")
    print("C) Sin límite de intentos")
    
    opcion = input("Introduce la opción: ").strip().upper()
    
if opcion == 'A':
    version_a()
elif opcion == 'B':
    version_b()
elif opcion == 'C':
    version_c()
else:
    print("Opción no válida")