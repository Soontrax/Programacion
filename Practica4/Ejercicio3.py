z = input("Pon el primer numero:")
x = input("Pon el segundo numero mayor que %d:" %z)
d=0
for i in range(z,x+1):
    d = d+i
print "El resultado de los valores %d y %d es: %d" %(z,x,d)

