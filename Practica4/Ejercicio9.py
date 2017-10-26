a = input("Dame la anchura del rectangulo:")
b = input("Dame la altura del rectangulo:")
for i in range(a):
    for j in range(b):
        if i==0 or i==a-1:
            print "*",
        else:
            if j==0 or j==b-1:
                print "*",
            else:
                print " ",
    print ""
