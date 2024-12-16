def ordena_positivos(lista):
    positivos = sorted([x for x in lista if x > 0])
    
    resultado = []
    indice_positivos = 0
        
    for num in lista:
        if num > 0:
            resultado.append(positivos[indice_positivos])
            indice_positivos += 1
        else:
            resultado.append(num)
        
    return resultado


lista = [8, -1, 3, -10, -3, 6, 4]
print(ordena_positivos(lista))