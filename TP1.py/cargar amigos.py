amigos=[]
a=input("¿Queres cargar los nombres de tus amigos?\n")
while a==a:
    if a=="si":
        amigos.append(input("Ingresar nombre de tu amigo:\n"))
        a=input("para volver a cargar poner si, para salir poner exit.\n")
    elif a=="exit":
        print (amigos)
        break
    elif a=="no":
        a=input("si no quieres cargar ningun amigo pon exit para salir, sino si para cargar alguno.\n")
    elif a!="si" or a!="no":
        a=input("Debes poner si,no o exit.\n") 