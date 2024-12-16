palabra = input("Introduce una palabra: ")

palabra_normalizada = palabra.replace(" ", "").lower()


if palabra_normalizada == palabra_normalizada[::-1]:
    print(f"{palabra} es un palíndromo")
    
else:
    print(f"{palabra} no es un palíndromo")