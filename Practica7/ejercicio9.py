a = raw_input("Dime una palabra:")
b = raw_input("Dime una palabra:")
def rima (a,b):
    if a[-2] == b[-2]:
        return "Las palabras" ,a, "y" ,b, "riman un poco."
    elif a[-3] == b[-3]:
        return "Las palabras" ,a, "y" ,b, "riman."
    else:
        return "Las palabras" ,a, "y" ,b, "no riman."
    return rima (a,b)
print rima (a,b)
