from ui.Views import *
from controller.UsuariosControllers import buscarUsuario, validarContrasenia, menu
from constructores.Constructores import ingrese_auto
from controller.UsuariosControllers import menuInvitado
bienvenida()
print("1-Login")
print("2-Entrar como invitado")
print("3-Salir")
login=input("")
if login=="1" or login=="login":
    userOk = buscarUsuario(msjUsuario())
    intentos = 3
    try:
        if(userOk):

            usuarioconPass = validarContrasenia(msjPassword())
            while userOk:
                if(usuarioconPass[1]):
                    userOk = menu(usuarioconPass[1])
        else:
            print('El Usuario no existe')

    finally:
        print('Gracias por Visitarnos')
elif login=="2" or login=="invitado":
    menuInvitado()
elif login=="3" or login=="salir":
    print("Gracias por visitarnos")
    quit()

