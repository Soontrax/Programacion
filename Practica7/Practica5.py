a = raw_input("Dime una frase:")
b = raw_input("Dime una vocal:")
def nombres (a,b):
    vocales = ["a","e","i","o","u"]
    espacio = " "
    for i in range(len(a)):
        if a[i] in vocales:
            espacio+= b
        else:
            espacio+= a[i]
    return espacio
print nombres (a,b)
