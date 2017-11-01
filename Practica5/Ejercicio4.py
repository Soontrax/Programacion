a = input("Escribe un numero:")
b = input("Escribe un numero mayor que %d: \n" %a)
while b<=a:
    b = input("Escribe un numero mayor que %d: \n" %a)
else:
    print "Los numeros que has escrito son" ,a , "y" ,b, 
