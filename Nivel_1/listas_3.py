asignaturas = ["DAW", "DWES", "DWEC", "DIW", "HLC"]

asignaturas_repetir= []

for asignatura in asignaturas:
    while True:
        try:
            nota = float(input("Introduce la nota de " + asignatura + ": "))
            if 0 <=nota <=10:
                break
            else:
                print("Por favor, introduce una nota válida")
        except ValueError:
            print("Por favor, introduce un número válido")
            
    if nota <5:
        asignaturas_repetir.append(asignatura)
        
if asignaturas_repetir:
    print ("Las asignaturas que debes repetir son: ")
    for asignatura in asignaturas_repetir:
        print (asignatura)
else:
    print("Felicidades!! No debes repetir ninguna asignatura")
    