a = raw_input("Pon tu nombre:")
b = raw_input("Pon un caracter:")
def persona (a,b): 
    for i in range(len(a)):
        if (a[i] == b):
            return "El caracter que has puesto esta en tu nombre"
    return "El caracter que has puesto NO esta en tu nombre" 
print persona(a,b)
