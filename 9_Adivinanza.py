import random

num_secreto = random.randint(1, 10)
intentos = 0
adivinado = False
print("¡Adivina el número secreto entre 1 y 100!")
print (num_secreto)
while not adivinado:
   try:
       num = int(input("Ingresa un número: "))
       intentos += 1

       if num == num_secreto:
           adivinado = True
           break
       elif num < num_secreto:
           print("El número es mayor. Intenta de nuevo.")
       else:
           print("El número es menor. Intenta de nuevo.")
   except ValueError:
       print("Por favor, ingresa un número válido.")

print(f"¡Bien! Adivinaste el número:{num_secreto} en {intentos} intentos.")