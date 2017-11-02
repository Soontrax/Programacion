a = input("Escribe el límite:")
b = input("Escribe un valor:")
w = []
w.append(b)
resultado = 0+b
while resultado != a:
    b = input("Escribe otro valor:")
    resultado = resultado+b
    if resultado > a:
        resultado = resultado-b
        b = input("Este valor es muy grande pon otro valor menor que "+str(b)+": ")
    else:
        w.append(b)
print "El total de los numeros es de:" ,resultado, w
