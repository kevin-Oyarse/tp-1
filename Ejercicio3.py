import random

jugando=True
while jugando:
    pj= input("opciones= piedra, papel o tijera \n")
    pc=random.choice(["piedra","tijera","papel"])

    if pj=="piedra":
        if pc=="piedra":
            print ("empate de piedra ")
        elif pc=="papel":
            print ("la pc eligio papel")
        else:
            print("La buena piedra nada le gana")
    elif pj=="tijera":
        if pc=="tijera":
            print ("empate de tijeras ")
        elif pc=="papel":
            print ("la pc eligio piedra")
        else:
            print("Ganaste con un buen par de tijeras")
    elif pj=="papel":
        if pc=="papel":
            print ("empate con papel")
        elif pc=="papel":
            print ("la pc eligio tijera")
        else:
            print("Anotate una victoria capo")
    else:
        print ("escribi bien inutil")
    seguir=""
    while seguir !="no" or seguir !="si":
        seguir=input ("Queres seguir jugando si/no\n")
        if seguir =="no":
            print ("gracias por jugar")
            jugando=False
            break
        elif seguir =="si":
            break
        else:
            print ("no te cuesta nada escribir bien capo")



