#Ejercicio 8
signos=["!","“","#","$","%","&",".","-"]
vocales=["a","e","i","o","u"]
cant=0

nombre=input('Ingresa su nombre y apellido:\n')
nombre.lower()
for i in vocales:
    for j in nombre:
        if i==j:
            cant+=1
if cant>3:
    print ("El nombre que ingresaste tiene",cant,"vocales.")
elif cant<3:
    print ("El nombre tiene menos de 3 vocales.")


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
for i in signos:
    for j in numero:
        if i==j:
            contra+=1
if contra<8 or contra>16:
    print("tu contraseña debe tener entre 8 a 16 caracteres y tener algun caracter especial")
elif contra>=8 and contra<=16:
    print("tu contraseña tiene esta cantidad de caracteres",contra)




