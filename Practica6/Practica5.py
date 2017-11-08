numero = input("Dime cuantas palabras tiene una lista:")
w = []
for i in range (numero):
    a = raw_input("Dime la palabra %d: \n" %(i+1))
    w = w+[a]
print "La lista creada es de:"  ,w

lista = input("Dime cuantas palabras tiene la lista de palabras a eliminar:")
z = []
for s in range (lista):
    b = raw_input("Dime la palabra %d: \n" %(s+1))
    z = z+[b]
print "La lista creada es de:"  ,z

for m in range (lista):
    if z[m] in w: 
        w.remove(z[m])
print "La lista es ahora:" ,w 
