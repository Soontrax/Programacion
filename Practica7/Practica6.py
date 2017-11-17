a = raw_input("Pon tu nombre:")
b = raw_input("Pon un caracter:")
def persona (a,b): 
    for i in range (a,b):
        if a[i] in b:
            print "El caracter que has puesto esta en tu nombre" ,a
        else:
            print "Error tu caracter no esta"
            
    
