palabras=[]
m=int(input ("cuantos palabras va a ingresar?\n"))
print("Ingrese las palabras:")
i=0
while i<m:
    palabras.append(input())
    palabras.sort()
    i+=1
print (palabras)

