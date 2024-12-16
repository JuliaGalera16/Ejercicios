abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
abecedario_rest = [letra for i, letra in enumerate(abecedario) if (i + 1) % 3 != 0]


print ("Lista tras eliminar las letras en posiciones de múltiplos de 3: ")
print(abecedario_rest)