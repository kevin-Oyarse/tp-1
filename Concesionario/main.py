from tkinter import ttk as ttk 
from tkinter import *
from tkinter import messagebox as messagebox
from model.Usuario import Usuario
from data.Usuarios import _usuariosRegistrados
from ui.Views import *
from controller.UsuariosControllers import buscarUsuario, validarContrasenia, menu,menuInvitado
from Ventanas.MenuPrincipal import *

root= Tk()
nombreUser=StringVar()
contraUser=StringVar()
CorreoUser=StringVar()
nivelUser=StringVar()
def inicio():
    #Ventana principal
    root.title("Login Usuario")

    #mainFrame
    mainFrame=Frame(root)
    mainFrame.pack()
    mainFrame.config(width=480,height=320)#,bg="lightblue")

    #Textos y titulos
    titulo=Label(mainFrame,text="Login de Usuario",font=("Arial",24))
    titulo.grid(column=0,row=0,padx=10,pady=10,columnspan=2)

    nombreLabel=Label(mainFrame,text="Nombre: ")
    nombreLabel.grid(column=0,row=1)
    passLabel=Label (mainFrame,text="Contraseña: ")
    passLabel.grid(column=0,row=2)

    #Etradas user y contra

    # nombreUser=StringVar()
    nombreUser.set("")
    nombreEntry=Entry(mainFrame,textvariable=nombreUser)
    nombreEntry.grid(column=1,row=1)
    
    # contraUser=StringVar()
    contraUser.set("")
    contraEntry=Entry (mainFrame,textvariable=contraUser,show="*")
    contraEntry.grid(column=1,row=2)

    # botones
    loginButon=ttk.Button(mainFrame,text="Iniciar Sesion",command=inicioSesion)
    loginButon.grid(column=1,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    RegistarBoton=ttk.Button(mainFrame,text="Registar",command=vetanaRegistro)
    RegistarBoton.grid(column=0,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    InvitadoButon=ttk.Button(mainFrame,text="Invitado",command=VentanaListaDeVehiculos)
    InvitadoButon.grid(column=2,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    bienvenida()
    root.mainloop()

def inicioSesion():
    user=buscarUsuario(nombreUser.get())
    if(user):
        usuarioconPass=validarContrasenia(contraUser.get())
        while user:
            if(usuarioconPass[1]):
                messagebox.showinfo("Conectado","Se inicio sesion con exito")
                user= menu(usuarioconPass[1])
            else:
                messagebox.showerror("Error","Contraseña incorrecta")
            break
    else:
        messagebox.showerror("Error","No existen usuarios con ese nombre")

def registarUser():  
    name=nombreUser.get()
    passwd=contraUser.get()
    email=CorreoUser.get()
    nivel=int(nivelUser.get())

    newUser=Usuario(name,passwd,email,nivel)
    _usuariosRegistrados.append(newUser)
    if nivel==1:
        messagebox.showinfo("Registro exitoso",f"Se registro el usuaio {name} como administrador exitosamente")
    elif nivel ==2:
        messagebox.showinfo("Registro exitoso",f"Se registro el usuaio {name} como empleado exitosamente")

    nombreUser.set("")
    contraUser.set("")
    CorreoUser.set("")
    nivelUser.set("")

def vetanaRegistro():
    #Ventana Registro
    winregistro=Toplevel()
    winregistro.title ("Ventan Registro")
    titulo=Label(winregistro,text="Registrar usuario",font=("Arial",24),background="lightblue")
    titulo.grid(column=0,row=0,padx=10,pady=10,columnspan=2)
    winregistro.config(width=400,height=320,background="lightblue")

    #Label 
    nombreLabel=Label(winregistro,text="Nombre: ")
    nombreLabel.grid(column=0,row=1)

    passLabel=Label (winregistro,text="Contraseña: ")
    passLabel.grid(column=0,row=2)

    CorreoLabel=Label (winregistro,text="Correo: ")
    CorreoLabel.grid(column=0,row=3)

    nivelLabel=Label(winregistro,text="nivel del usuario: ")
    nivelLabel.grid(column=0,row=4)

    #Entrada de info

    
    nombreEntry=Entry(winregistro,textvariable=nombreUser)
    nombreEntry.grid(column=1,row=1)

    
    contraEntry=Entry (winregistro,textvariable=contraUser,show="*")
    contraEntry.grid(column=1,row=2)

    CorreoEntry=Entry (winregistro,textvariable=CorreoUser)
    CorreoEntry.grid(column=1,row=3)

    nivelEntry=Entry (winregistro,textvariable=nivelUser)
    nivelEntry.grid(column=1,row=4)

    #Boton

    botonRegistrar=Button (winregistro,text="Registrar",command=lambda:[registarUser(),winregistro.destroy()])
    botonRegistrar.grid(column=1,row=5,ipadx=5,ipady=5,padx=10,pady=10)


if __name__=="__main__":
    inicio()
