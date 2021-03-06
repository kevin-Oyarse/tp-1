from Ventanas.MenuPrincipal import VentanaListaDeVehiculos
from Ventanas.MenuPrincipal import MenuPrincial
from Ventanas.VentanaEmple import MenuEmpleado
from data.Usuarios import _usuariosRegistrados
from model.Usuario import Usuario
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
        return [True, user.nvl]


def menu(args):
    if(args == 1):
        return menuAdmin()
    elif args == 2:
        return menuEmpleado()
    else:
        return menuInvitado()


def menuAdmin():
    MenuPrincial()
    
def menuEmpleado():
    MenuEmpleado()


def menuInvitado():
    VentanaListaDeVehiculos()