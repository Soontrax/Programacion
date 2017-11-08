numero = input("Dime cuantas palabras tiene una lista:")
w = []
for i in range (numero):
    a = raw_input("Dime la palabra %d: \n" %(i+1))
    w = w+[a]
print "La lista creada es de:"  ,w
b = raw_input("Sustituir la palabra:")
c = raw_input("Por la palabra:")

for s in range (numero):
    if b in w:
        indice = w.index(b)
        w.remove(b)
        w.insert(indice,c)
print "La lista ahora es de:" ,w
