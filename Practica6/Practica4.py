numero = input("Dime cuantas palabras tiene una lista:")
w = []
for i in range (numero):
    a = raw_input("Dime la palabra %d: \n" %(i+1))
    w = w+[a]
print "La lista creada es de:"  ,w
c = raw_input("Dime la palabra:")

for s in range (numero):
    if c in w:
        w.remove(c)
print "La lista ahora es de:" ,w
