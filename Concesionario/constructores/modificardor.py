from model.Auto import Auto, Bicleta
from data.Auto import *
def modificarkm_auto():
    
    printAutos()
    num = int(input('Ingrese La ubicacion de auto: '))
    auto = obtenerAuto(num)
    auto.km =input("Ingrese los km: ")
    printAutos()

def modificarDetalle_auto():
    printAutos()
    num = int(input('Ingrese La ubicacion de auto: '))
    auto = obtenerAuto(num)
    auto.detalles =input('Agrege detalles: ')
    printAutos()

def modificarDetalle_moto():
    printMoto()
    num = int(input('Ingrese La ubicacion de la moto: '))
    moto = obtenerMoto(num)
    moto.detalles =input('Agrege detalles: ')
    printMoto()

def modificarkm_moto():
    printMoto()
    num = int(input('Ingrese La ubicacion de la moto: '))
    moto = obtenerMoto(num)
    moto.km =input('Ingrese los km de la moto: ')
    printMoto()

def modificarkm_Acoplado():
    printAcoplado()
    num = int(input('Ingrese la ubicacion del acoplado: '))
    acoplado = obtenerAcoplado(num)
    acoplado.km =input('Ingrese los km del acoplado: ')
    printAcoplado()

def modificardetalle_Acoplado():
    printAcoplado()
    num = int(input('Ingrese La ubicacion del acoplado: '))
    acoplado = obtenerAcoplado(num)
    acoplado.detalles =input('Ingrese los detalles del acoplado: ')
    printAcoplado()

def modificarkm_camioneta():
    printcamioneta()
    num=int (input ('Ingrese la ubicaion de la camioneta: '))
    camioneta= obtenerCamioneta (num)
    camioneta.km=input("Ingrese los km de la camioneta: ")
    printcamioneta()

def modificardetalles_camioneta():
    printcamioneta()
    num=int (input ('Ingrese la ubicaion de la camioneta: '))
    camioneta= obtenerCamioneta (num)
    camioneta.detalles=input("Ingrese los detalles de la camioneta: ")
    printcamioneta()

def modificardetalle_bici():
    printbici()
    num=int(input("Ingrese la ubicacion de la bici: "))
    bici=obtenerBici(num)
    bici.detalles=input("Ingrese el detalle de la bici: ")
    printbici()

def modificardetalle_cole():
    printcolectivo()
    num=int(input("Ingrese la ubicacion de la bici: "))
    cole=obtenerCole(num)
    cole.detalles=input("Ingrese el detalle de la bici: ")
    printcolectivo()

def modificarkm_cole():
    printcolectivo()
    num=int(input("Ingrese la ubicacion de la bici: "))
    cole=obtenerCole(num)
    cole.km=input("Ingrese el km de la bici: ")
    printcolectivo()

def modificardetalles_camion():
    printCamion()
    num=int(input("Ingrese la ubicacion del camion: "))
    camion=obtenerCamion(num)
    camion.detalles=input("Ingrese los detalles del camion: ")
    printCamion()

def modificarkm_camion():
    printCamion()
    num=int(input("Ingrese la ubicacion del camion: "))
    camion=obtenerCamion(num)
    camion.km=input("Ingrese los km del camion: ")
    printCamion()

def modificarprecio_auto():
    printAutos()
    num=int(input("Ingrese la ubicacion del auto: "))
    auto=obtenerCamion(num)
    auto.precio=input("Ingrese el precio: ")
    printAutos()

def modificarprecio_moto():
    printMoto()
    num = int(input('Ingrese La ubicacion de la moto: '))
    moto = obtenerMoto(num)
    moto.precio =input('Agrege precio: ')
    printMoto()

def modificarprecio_acoplado():
    printAcoplado()
    num = int(input('Ingrese la ubicacion del acoplado: '))
    acoplado = obtenerAcoplado(num)
    acoplado.precio =input('Ingrese precio: ')
    printAcoplado()

def modificarprecio_camioneta():
    printcamioneta()
    num=int (input ('Ingrese la ubicaion de la camioneta: '))
    camioneta= obtenerCamioneta (num)
    camioneta.precio=input("Ingrese los km de la camioneta: ")
    printcamioneta()

def modificarprecio_bici():
    printbici()
    num=int(input("Ingrese la ubicacion de la bici: "))
    bici=obtenerBici(num)
    bici.detalles=input("Ingrese el detalle de la bici: ")
    printbici()

def modificarprecio_camion():
    printCamion()
    num=int(input("Ingrese la ubicacion del camion: "))
    camion=obtenerCamion(num)
    camion.precio=input("Ingrese los km del camion: ")
    printCamion()

def modificarprecio_colectivo():
    printcolectivo()
    num=int(input("Ingrese la ubicacion de la bici: "))
    cole=obtenerCole(num)
    cole.precio=input("Ingrese el detalle de la bici: ")
    printcolectivo()