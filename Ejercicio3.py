import random

jugando=0
while jugando!=3:
    pj= input("opciones= piedra, papel o tijera \n")
    pc=random.choice(["piedra","tijera","papel"])

    if pj=="piedra" or pj=="p":
        if pc=="piedra":
            print ("empate de piedra ")
        elif pc=="papel":
            print ("la pc eligio papel")
        else:
            print("La buena piedra nada le gana")
            jugando+=1
    elif pj=="tijera" or pj=="t":
        if pc=="tijera":
            print ("empate de tijeras ")
        elif pc=="papel":
            print ("Perdiste ante la buena piedra")
        else:
            print("Ganaste con un buen par de tijeras")
            jugando+=1
    elif pj=="papel" or pj=="p":
        if pc=="papel":
            print ("empate con papel")
        elif pc=="papel":
            print ("la pc eligio tijera")
        else:
            print("Anotate una victoria capo")
            jugando+=1
    else:
        print ("Escribi bien inutil")
    seguir=""
if jugando==3:
    print("Ya ganaste las 3 partidas")
    while seguir !="no" or seguir !="si":
        seguir=input ("¿Queres seguir jugando? si/no\n")
        if seguir =="no":
            print ("gracias por jugar")
            break
        elif seguir =="si":
            jugando=0
            break
        else:
            print ("no te cuesta nada escribir bien capo")