palabras=[]
print("Ingrese las palabras:")
while True:
    try:
        pal=str(input())
        palabras.append(pal)
        palabras.sort()
    except:
        print("solo letras")
    if pal == "salir":
        break

print (palabras)

