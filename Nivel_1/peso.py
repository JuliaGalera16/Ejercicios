
peso= float(input("Introduce tu peso: "))

unidad = input("¿(K)gs o (L)bs? " ).strip().lower()

if unidad == "k":
    peso_libras = peso /0.45
    print(f"Tu peso en libras es {peso_libras:.2f} lbs")
elif unidad == "l":
    peso_kilos = peso * 0.45
    print(f"Tu peso en kilos es {peso_kilos:.2f} kg")
else:
    print("Opcion no válida. Por favor, elige (K)gs o (L)bs")