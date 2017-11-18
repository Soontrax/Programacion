palabra = raw_input("Dime una frase:")
def parametro (palabra):
    espacio = " "
    for i in range(len(palabra)):
        if palabra[i] != " ":
            espacio = espacio+palabra[i]
    return espacio
print parametro(palabra)
