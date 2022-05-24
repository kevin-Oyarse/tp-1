from data.Auto import *


def Invitado():
    print("Autos:")
    printAutos()
    print ("motos:")
    printMoto()
    print("Bicicletas:")
    printbici()
    print("Camiones:")
    printCamion()
    print ("Colectivos:")
    printcolectivo()
    print ("Acoplado:")
    printAcoplado()
    print("Camionetas:")
    printcamioneta()

    print("-Salir")
    op=input("")
    if op=="salir":
        print("Gracias por visitarnos")
        quit()
    else:
        print("opcion no valida")
        Invitado()