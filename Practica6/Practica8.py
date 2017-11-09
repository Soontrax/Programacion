numero = input("Dime cuantas palabras tiene una lista:")
w = []
for i in range (numero):
    a = raw_input("Dime la palabra %d: \n" %(i+1))
    w = w+[a]
print "La lista creada es de:"  ,w
w.sort()
print "La lista ordenada es de:" ,w
