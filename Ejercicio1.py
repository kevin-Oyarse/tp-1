num=[]
val=""
print ("Ingrese los numeros:")
while True:
    try:
        val=float((input()))
        num.append(val)
    except:
        print ("solo numeros")
    if num == "salir":
        break
    if len(num)>0:
        prom=sum(num)//len(num)
        mayor=max(num)
        menor=min(num)
        print(f"El numero mayor es {mayor} y el numero menor es {menor}")
        print("El promedio es de ",prom)