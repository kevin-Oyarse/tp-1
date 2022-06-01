from model.Usuario import Usuario
from constructores.Constructores import crearUsuarios, crearAuto,crear_bicleta,crear_camion,crear_camioneta,crear_colectivo,crear_coplado,crear_moto


def bienvenida():
    print('Bienvenidos a Concesionaria "El autito"')
    crearUsuarios()
    crearAuto()
    crear_moto()
    crear_coplado()
    crear_bicleta()
    crear_camioneta()
    crear_camion()
    crear_colectivo()
    
def msjUsuario():
    return input('Ingrese usuario: ')
    
def msjErrorUsuario():
    print('Usuario Incorrecto')


def msjPassword():
    return input('Ingrese Password: ')


def msjErrorPassword():
    print('Password Incorrecta')
