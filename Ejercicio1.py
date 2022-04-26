num=[]
i=0
mayor=0
menor=0
m=int(input ("cuantos numeros va a ingresar?\n"))
print ("Ingrese los numeros:")
while i<m:
    val=float((input()))
    num.append(val)
    i+=1
prom=sum(num)//len(num)
mayor=max(num)
menor=min(num)
print(f"El numero mayor es {mayor} y el numero menor es {menor}")
print("El promedio es de ",prom)