numero = input("Dime cuantas palabras tiene una lista:")
w = []
for i in range (numero):
    a = raw_input("Dime la palabra %d: \n" %(i+1))
    w = w+[a]
print "La lista creada es de:"  ,w
b = raw_input("Dime la palabra:")
z = 0
for s in range (numero):
    if b in w:
        w.remove(b)
        z = z+1
    else:
        z = z
print "La palabra" ,b, "aparece" ,z, "vez/es en la lista."
