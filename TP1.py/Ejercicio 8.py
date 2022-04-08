#Ejercicio 8
signos=["!","“","#","$","%","&",".","-"]
vocales=["a","e","i","o","u"]
cant=0
f=0
nombre=input('Ingresa su nombre y apellido:\n')
nombre.lower()
while f==0:
    f=0
    for i in vocales:
        for j in nombre:
            if i==j:
                cant+=1
    if cant>3:
        f=1
        print ("El nombre que ingresaste tiene",cant,"vocales.")
    elif cant<3:
        f=0
        print ("El nombre incorrecto.")
        nombre=input('Ingresa su nombre y apellido:\n')
        nombre.lower()


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

contra=0
fContra=0
numero=input("ingresar su contraseña:\n")
while fContra==0:
    for i in signos:
        for j in numero:
            if i==j:
                contra+=1
    if contra<3 and len(numero)<8 and len(numero)<16:
        print("tu contraseña debe tener entre 8 a 16 caracteres y tener algun caracter especial")
        numero=input("ingresar su contraseña:\n")
        fContra=0
    elif contra>=3 and len(numero)>=8 and len(numero)<=16:
        print("tu contraseña es correcta")
        fContra=1





