from model.Auto import Bicleta, Auto
from model.Usuario import Usuario
from data.Usuarios import agregaUsuarios, printUsuarios
from data.Auto import*

def crearUsuarios():
    usuario = Usuario("admin","admin@gmail.com","admin123",1)
    agregaUsuarios(usuario)
    usuario = Usuario("empleado","empleado@gmail.com","empleado123",2)
    agregaUsuarios(usuario)

def crearAuto():
    auto=Auto("Ford","Fiesta","0","$190.000","Full","Nuevo")
    agregaAutos(auto)
    auto=Auto("Ford","Focus","25.000","120.000","Full","Usado")
    agregaAutos(auto)

def crear_moto():
    moto=Auto("BMW","G 650 GS","1700","17.700","motor nuevo","usada")
    agregarMoto(moto)
    moto=Auto("Ducati","DesertX","0","14.000","Sin estrenar","Nueva")
    agregarMoto(moto)


def crear_coplado():
    acoplado=Auto("","","","","","")
    agregarAcoplado(acoplado)
    acoplado=Auto("","","","","","")
    agregarAcoplado(acoplado)



def crear_bicleta():
    bici=Bicleta("fire bird","rodado 29","14.000","Sin estrenar","Nueva")
    agregarbici(bici)
    bici=Bicleta("Klatter","Mountain Bike","$17.000","tiene la rueda de atras con pinchada ","usada")
    agregarbici(bici)



def crear_camioneta():
    camioneta=Auto("Volkswagen","Amarok","0 km","Full","$250.000","Nueva")
    agregarCamioneta(camioneta)
    camioneta=Auto("Ford","Ranger","0 km","Full","$250.000","Nueva")
    agregarCamioneta(camioneta)


def crear_camion():
    camion=Auto("","","","","","")
    agregarCamion(camion)
    camion=Auto("","","","","","")
    agregarCamion(camion)

def crear_colectivo():
    cole=Auto("Agrake","MT 12","156.000","abollado del lado derecho","220.000","usado")
    agregarcolectivo(cole)
    cole=Auto("Mercedez Benz","500","0","Full","280.000","nuevo")

def ingrese_auto():
    marca=input("Ingrese marca: ")
    modelo=input("Ingrese modelo: ")
    estado=input("Ingrese el estado: ")
    km=input("Ingrese los km: ")
    precio=input("Ingrese el precio: ")
    estado=input("Ingrese estado del auto: ")
    detalle=input ("Ingrese detalles: ")
    auto_ingresado=Auto(marca,modelo,km,detalle,precio,estado)
    agregaAutos(auto_ingresado)

def ingrese_moto():
    marca=input("Ingrese marca: ")
    modelo=input("Ingrese modelo: ")
    estado=input("Ingrese el estado: ")
    km=input("Ingrese los km: ")
    precio=input("Ingrese el precio: ")
    estado=input("Ingrese estado del auto: ")
    detalle=input ("Ingrese detalles: ")
    moto_ingresado=Auto(marca, modelo,km,detalle,precio,estado)
    agregarMoto(moto_ingresado)


def ingrese_acoplado():
    marca=input("Ingrese marca: ")
    modelo=input("Ingrese modelo: ")
    estado=input("Ingrese el estado: ")
    km=input("Ingrese los km: ")
    precio=input("Ingrese el precio: ")
    estado=input("Ingrese estado del auto: ")
    detalle=input ("Ingrese detalles: ")
    acoplado_ingresado=Auto(marca, modelo,km,detalle,precio,estado)
    agregarAcoplado(acoplado_ingresado)



def ingrese_bicicleta():
    marca=input("Ingrese marca: ")
    modelo=input("Ingrese modelo: ")
    estado=input("Ingrese el estado: ")
    precio=input("Ingrese el precio: ")
    estado=input("Ingrese estado del auto: ")
    detalle=input("Ingrese detalle del auto: ")
    bicicleta_ingresado=Bicleta(marca, modelo,detalle,precio,estado)
    agregarbici(bicicleta_ingresado)


def ingrese_camioneta():
    marca=input("Ingrese marca: ")
    modelo=input("Ingrese modelo: ")
    estado=input("Ingrese el estado: ")
    km=input("Ingrese los km: ")
    precio=input("Ingrese el precio: ")
    estado=input("Ingrese estado del auto: ")
    detalle=input("Ingrese algun detalle: ")
    camioneta_ingresado=Auto(marca, modelo,km,detalle,precio,estado)
    agregarCamioneta(camioneta_ingresado)


def ingrese_camion():
    marca=input("Ingrese marca: ")
    modelo=input("Ingrese modelo: ")
    estado=input("Ingrese el estado: ")
    km=input("Ingrese los km: ")
    precio=input("Ingrese el precio: ")
    detalle=input("Ingrese algun detalle: ")
    camion_ingresado=Auto(marca, modelo,km,detalle,precio,estado)
    agregarCamion(camion_ingresado)

def ingrese_colectivo():
    marca=input("Ingrese marca: ")
    modelo=input("Ingrese modelo: ")
    estado=input("Ingrese el estado: ")
    km=input("Ingrese los km: ")
    precio=input("Ingrese el precio: ")
    detalle=input("Ingrese algun detalle: ")
    colectivo_ingresado=Auto(marca, modelo,km,detalle,precio,estado)
    agregarcolectivo(colectivo_ingresado)