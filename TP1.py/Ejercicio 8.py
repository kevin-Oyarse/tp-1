#Ejercicio 8
signos=["!","“","#","$","%","&",".","-"]
vocales=["a","e","i","o","u"]
cant=0

nombre=input('Ingresa su nombre y apellido:\n')
nombre.lower()
while nombre!=vocales:
    if nombre !=vocales:
        for i in vocales:
            for j in nombre:
                if i==j:
                    cant+=1
        break
    else:
        print("solo letras")
        nombre=input("ingresar un nombre:\n")
print("La cantidad de vocales es de ",cant)

año=input("ingresar año:\n")
while len(año)==len(año):
    if len(año)==4:
        break
    elif len(año)<4:
        print("ingrese año real")
        año=input("ingresar año:\n")
    elif len(año)>4:
        print("ingrese año real")
        año=input("ingresar año:\n")

numero=input("ingresar su contraseña:\n")
contra=0
while numero!=signos:
    if numero !=signos:
        for i in signos:
            for j in numero:
                if i==j:
                    contra+=1
        break
    else:
        print("solo letras")
        nombre=input("ingresar un nombre:\n")
print("tu contraseña tiene esta cantidad de caracteres",contra)




