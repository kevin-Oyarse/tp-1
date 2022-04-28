palabras=[]
print("Ingrese las palabras:")
while True:
    pal=input ("")
    try:
        pal=int(pal)
        print("solo letras")
    except:
        if pal=="salir":
            break
        palabras.append(pal)
        palabras.sort()

print (palabras)

