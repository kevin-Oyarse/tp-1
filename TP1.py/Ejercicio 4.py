#Ejercicio 5
n1=int(input("ingrese un número:\n"))
n2=int(input("ingrese otro número:\n"))
resultado=n1%n2
if resultado==0:
    print("los números ",n1,",",n2," son divisibles")
else:
    print("los números ",n1,",",n2," no son divisibles")