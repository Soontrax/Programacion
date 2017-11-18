a = raw_input("Dime una frase:")
def nombres (a):
    contador = 0
    vocales = ["a","e","i","o","u"]
    for i in range(len(a)):
        if a[i] in vocales:
            contador = contador+1
    return contador
print nombres (a)
