num=[]
mayor=0
menor=0

print ("Ingrese los numeros:")
while True:
    try:
        val=float((input()))
        num.append(val)
    except:
        if num!="salir":
            break
        print ("solo numeros")
    prom=sum(num)//len(num)
    mayor=max(num)
    menor=min(num)
    print(f"El numero mayor es {mayor} y el numero menor es {menor}")
    print("El promedio es de ",prom)