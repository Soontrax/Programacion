n = raw_input("Escribe una frase:")
def nombres (n):
    espacio = " "
    for i in range(len(n)):
        if n[i] == " ":
            espacio+= "*"
        else:
            espacio+= n[i]
    return espacio
print nombres (n)
