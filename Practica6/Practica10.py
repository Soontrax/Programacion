a = input("Dime un numero:")
w = []
for i in range(1,a+1):
    if a%i==0:
        w.append(i)

print a,"tiene",len(w), "divisores:" ,w
