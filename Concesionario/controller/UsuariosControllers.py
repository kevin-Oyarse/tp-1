from Ventanas.MenuPrincipal import MenuPrincial
from Ventanas.VentanaEmple import MenuEmpleado
from data.Auto import printAutos
from data.Usuarios import _usuariosRegistrados
from model.Usuario import Usuario
from niveles.admin import Admin
from niveles.invitado import Invitado
from niveles.empleado import Empleado
user = Usuario('','','','')


def buscarUsuario(nombre):
    for usuario in _usuariosRegistrados:
        if usuario.nombre == nombre:
            user.email = usuario.email
            user.contra = usuario.contra
            user.nvl = usuario.nvl
            return True


def validarContrasenia(contra):
    if user.contra == str(contra):
        print ("login exitoso")
        return [True, user.nvl]


def menu(args):
    if(args == "1"):
        return menuAdmin()
    elif args == "2":
        return menuEmpleado()
    else:
        return menuInvitado()


def menuAdmin():
    MenuPrincial()
    #Admin()
    
def menuEmpleado():
    MenuEmpleado()
    #Empleado()


def menuInvitado():
    Invitado()