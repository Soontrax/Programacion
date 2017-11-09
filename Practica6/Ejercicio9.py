numero = input("Dime cuantas palabras tiene una lista:")
w = []
no_repetidas = []
for i in range (numero):
    a = raw_input("Dime la palabra %d: \n" %(i+1))
    w = w+[a]
print "La lista creada es de:"  ,w

for j in range (len(w)):
    if w[j] not in no_repetidas:
        no_repetidas.append(w[j])
print "La lista sin repeticiones es de:" ,no_repetidas
