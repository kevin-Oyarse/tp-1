num=[]
print ("Ingrese los numeros:")
while True:
    try:
        val=input()
        if val == "salir":
            break
        val=float((val))
        num.append(val)
    except:
        print ("solo numeros")
    if len(num)>0:
        prom=sum(num)//len(num)
        mayor=max(num)
        menor=min(num)
        print(f"El numero mayor es {mayor} y el numero menor es {menor}")
        print("El promedio es de ",prom)