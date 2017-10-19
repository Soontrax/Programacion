a = input("Escribe el primer numero:")
b = input("Pon el segundo numero mayor que: %d \n" % a)
for z in range(a,b+1):
    if z%2==0:
        print "El numero" ,z , "es par"
    else:
        print "El numero" ,z , "es impar"
