a = input("Escribe un numero:")
b = input("Escribe un numero mayor que %d: \n" %a)
w = []
while b<=a:
    b = input("Escribe un numero mayor que %d: \n" %a)
c = input("Escribe un numero entre" + str(a) + "y" + str(b) + ":")
while a<= c <=b:
    w.append(c)
    c = input("Escribe otro entre" + str(a) + "y" + str(b) + ":")
print w
