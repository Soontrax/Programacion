a = input("Escribe el límite:")
b = input("Escribe un valor:")
w = []
resultado = 0+b
while resultado < a:
    b = input("Escribe otro valor:")
    w.append(b)
    resultado = resultado+b
print "El límite a superar es de:" ,a , w
