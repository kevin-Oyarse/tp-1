from tkinter import ttk as ttk
from tkinter import *
from tkinter import messagebox as messagebox
from controller.UsuariosControllers import menuInvitado
from model.Usuario import Usuario
from data.Usuarios import _usuariosRegistrados
from ui.Views import *
from controller.UsuariosControllers import buscarUsuario, validarContrasenia, menu


root= Tk()
nombreUser=StringVar()
contraUser=StringVar()

def inicio():
    #Ventana principal
    #root= Tk()
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

    RegistarBoton=ttk.Button(mainFrame,text="Registar",command=registarUser)
    RegistarBoton.grid(column=0,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    loginButon=ttk.Button(mainFrame,text="Invitado",command=menuInvitado)
    loginButon.grid(column=2,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    loginButon=ttk.Button(mainFrame,text="Salir",command=quit)
    loginButon.grid(column=2,row=0,ipadx=5,ipady=5,padx=10,pady=10)
    bienvenida()
    root.mainloop()

def inicioSesion():
    user=buscarUsuario(nombreUser.get())
    if(user):
        usuarioconPass=validarContrasenia(contraUser.get())
        while user:
            if(usuarioconPass[1]):
                user= menu(usuarioconPass[1])
                messagebox.showinfo("Conectado","Se inicio sesion con exito")
            else:
                messagebox.showerror("Error","Contraseña incorrecta")
            break
    else:
        messagebox.showerror("Error","No existen usuarios con ese nombre")
def registarUser():
    name=nombreUser.get()
    passwd=contraUser.get()
    newUser=Usuario(name,passwd,email=name+"@gmail.com",nvl="3")
    _usuariosRegistrados.append(newUser)
    messagebox.showinfo("Registro exitoso",f"Se registro el usuaio {name} con exito")
    nombreUser.set("")
    contraUser.set("")


if __name__=="__main__":
    inicio()

