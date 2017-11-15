def nombres (primer):
    return primer
n = raw_input("Escribe una frase:")
for i in range (len(n)):
    nombre = nombres(n)
    print nombre[i]
