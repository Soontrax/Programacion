a = input("Escribe un numero:")
b = input("Escribe un numero mayor que %d: \n" %a)
c = input("Escribe un numero mayor que %d: \n" %b)
d = input("Escribe un numero mayor que %d: \n" %c)
e = input("Escribe un numero mayor que %d: \n" %d)
while b<=a:
    b = input("Escribe un numero mayor que %d: \n" %a)
while c<=b:
    c = input("Escribe un numero mayor que %d: \n" %b)
while d<=c:
    d = input("Escribe un numero mayor que %d: \n" %c)
while e<=d:
    e = input("Escribe un numero mayor que %d: \n" %d)
else:
    print "Los numeros que has escrito son" ,a , "," ,b, "," ,c, "," ,d, "," ,e, 
