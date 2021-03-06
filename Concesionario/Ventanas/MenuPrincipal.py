from tkinter import ttk as ttk 
from tkinter import *
from model.Usuario import *
from Ventanas.VentaModi import *
from Ventanas.VentanaCargar import*
from model.Auto import*
from data.Auto import _autos
from data.Usuarios import _usuariosRegistrados
#Ventana del menu


def MenuPrincial():
    #Ventana
    win=Toplevel()
    win.title ("Menu Principal.")
    win.config(width=480,height=320)
    global nombreUser
    global contraUser
    global CorreoUser
    global nivelUser
    nombreUser=StringVar()
    contraUser=StringVar()
    CorreoUser=StringVar()
    nivelUser=StringVar()
    #titulo
    #botones

    ButonCargar=ttk.Button(win,text="Cargar vehiculos",command=lambda:[cargarVehiculos(),win.destroy()])
    ButonCargar.grid(column=2,row=1,ipadx=5,ipady=5,padx=10,pady=10)

    botonPrecio=ttk.Button(win,text="Modificar precios de los vehiculos",command=lambda:[VentanaPrecio(),win.destroy()])
    botonPrecio.grid(column=2,row=2,ipadx=5,ipady=5,padx=10,pady=10)

    botonkm=ttk.Button(win,text="Modificar km de los vehiculos",command=lambda:[VentanaKm(),win.destroy()])
    botonkm.grid(column=2,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    botonUser=ttk.Button(win,text="Menu usuario",command=lambda:[VentanaUsuarios(),win.destroy()])
    botonUser.grid(column=3,row=1,ipadx=5,ipady=5,padx=10,pady=10)
    
    botonDetalles=ttk.Button(win,text="Agregar detalles a vehiculos",command=lambda:[VentanaDetalles(),win.destroy()])
    botonDetalles.grid(column=3,row=2,ipadx=5,ipady=5,padx=10,pady=10)

    botonLista=ttk.Button(win,text="Mostrar lista de vehiculos",command=VentanaListaDeVehiculos)
    botonLista.grid(column=3,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    botonSalir=ttk.Button(win,text="Salir",command=quit)
    botonSalir.grid(column=2,row=7,ipadx=5,ipady=5,padx=10,pady=10,columnspan=2)

def cargarVehiculos():
    #Ventana
    winV=Toplevel()
    winV.title("Cargar Vehiculos")
    winV.config(width=480,height=320)
    
    #Titulo
    titulo=Label(winV,text="Cargar Vehiculo",font=("Arial",24))
    titulo.grid(column=2,row=0,padx=10,pady=10,columnspan=2)
    #botones

    upAutos=ttk.Button(winV,text="Cargar Auto",command=Cargar_Auto)
    upAutos.grid(column=2,row=2,ipadx=5,ipady=5,padx=10,pady=10)

    upMotos=ttk.Button(winV,text="Cargar Motos",command=Cargar_Moto)
    upMotos.grid(column=2,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    upCamioneta=ttk.Button(winV,text="Cargar Camioneta",command=Cargar_camioneta)
    upCamioneta.grid(column=2,row=4,ipadx=5,ipady=5,padx=10,pady=10,columnspan=2)

    upCamion=ttk.Button(winV,text="Cargar Camion",command=Cargar_Camion)
    upCamion.grid(column=2,row=1,ipadx=5,ipady=5,padx=10,pady=10)
    
    upAco=ttk.Button(winV,text="Cargar Acoplado",command=Cargar_Acoplado)
    upAco.grid(column=3,row=1,ipadx=5,ipady=5,padx=10,pady=10)

    upCole=ttk.Button(winV,text="Cargar Colectivo",command=Cargar_Colectivo)
    upCole.grid(column=3,row=2,ipadx=5,ipady=5,padx=10,pady=10)

    upBici=ttk.Button(winV,text="Cargar Bici",command=Cargar_Bici)
    upBici.grid(column=3,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    botonVoler=ttk.Button(winV,text="Volver",command=lambda:[MenuPrincial(),winV.destroy()])
    botonVoler.grid(column=3,row=9,ipadx=5,ipady=5,padx=10,pady=10)

def VentanaListaDeVehiculos():
    ventanaList=Toplevel()
    ventanaList.title("Lista Vehiculos")
    ventanaList.config(width=480,height=320)
    for i in _autos:
        autos=i
    Listbox=tk.Listbox(ventanaList,width=90,height=50)
    Listbox.pack()
    Listbox.insert(0,autos)
    
    #Text

def VentanaPrecio():
    #Ventana
    ventanamod=Toplevel()
    ventanamod.title("Modificar Precios")
    ventanamod.config(width=480,height=320)
    #Titulo

    #Botones
    botonAuto=ttk.Button(ventanamod,text="Auto",command=PrecioAuto)
    botonAuto.grid (column=2,row=2,ipadx=5,ipady=5,padx=10,pady=10)

    botonMoto=ttk.Button(ventanamod,text="Moto",command=PrecioMoto)
    botonMoto.grid(column=2,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    botonAcoplado=ttk.Button(ventanamod,text="Acoplado",command=PrecioAcoplado)
    botonAcoplado.grid(column=2,row=4,ipadx=5,ipady=5,padx=10,pady=10)

    botonColectivo=ttk.Button(ventanamod,text="Colectivo",command=PrecioCole)
    botonColectivo.grid(column=3,row=2,ipadx=5,ipady=5,padx=10,pady=10)

    botonBici=ttk.Button(ventanamod,text="Bicicleta",command=PrecioBici)
    botonBici.grid(column=3,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    botonCamioneta=ttk.Button(ventanamod,text="Camioneta",command=PrecioCamioneta)
    botonCamioneta.grid(column=3,row=4,ipadx=5,ipady=5,padx=10,pady=10)

    botonCamio=ttk.Button(ventanamod,text="Camion",command=PrecioCamion)
    botonCamio.grid(column=4,row=2,ipadx=5,ipady=5,padx=10,pady=10)


    botonVolver=ttk.Button(ventanamod,text="Volver",command=lambda:[MenuPrincial(),ventanamod.destroy()])
    botonVolver.grid(column=5,row=4,ipadx=5,ipady=5,padx=10,pady=10)

def VentanaKm():
    #Ventana
    ventanamod=Toplevel()
    ventanamod.title("Modificar Km")
    ventanamod.config(width=480,height=320)
    #Titulo

    #Botones
    botonAuto=ttk.Button(ventanamod,text="Auto",command=KmAuto)
    botonAuto.grid (column=2,row=2,ipadx=5,ipady=5,padx=10,pady=10)

    botonMoto=ttk.Button(ventanamod,text="Moto",command=KmMoto)
    botonMoto.grid(column=2,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    botonAcoplado=ttk.Button(ventanamod,text="Acoplado",command=KmAcoplado)
    botonAcoplado.grid(column=2,row=4,ipadx=5,ipady=5,padx=10,pady=10)

    botonColectivo=ttk.Button(ventanamod,text="Colectivo",command=KmCole)
    botonColectivo.grid(column=3,row=2,ipadx=5,ipady=5,padx=10,pady=10)

    botonCamioneta=ttk.Button(ventanamod,text="Camioneta",command=KmCamioneta)
    botonCamioneta.grid(column=3,row=4,ipadx=5,ipady=5,padx=10,pady=10)

    botonCamio=ttk.Button(ventanamod,text="Camion",command=KmCamion)
    botonCamio.grid(column=4,row=2,ipadx=5,ipady=5,padx=10,pady=10)


    botonVolver=ttk.Button(ventanamod,text="Volver",command=lambda:[MenuPrincial(),ventanamod.destroy()])
    botonVolver.grid(column=5,row=4,ipadx=5,ipady=5,padx=10,pady=10)
    
def VentanaDetalles():
    ventanamod=Toplevel()
    ventanamod.title("Modificar detalles")
    ventanamod.config(width=480,height=320)
    #Titulo
    
    #Botones
    botonAuto=ttk.Button(ventanamod,text="Auto",command=DetallesAuto)
    botonAuto.grid (column=2,row=2,ipadx=5,ipady=5,padx=10,pady=10)

    botonMoto=ttk.Button(ventanamod,text="Moto",command=DetallesMoto)
    botonMoto.grid(column=2,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    botonAcoplado=ttk.Button(ventanamod,text="Acoplado",command=DetallesAcoplado)
    botonAcoplado.grid(column=2,row=4,ipadx=5,ipady=5,padx=10,pady=10)

    botonColectivo=ttk.Button(ventanamod,text="Colectivo",command=DetallesCole)
    botonColectivo.grid(column=3,row=2,ipadx=5,ipady=5,padx=10,pady=10)

    botonBici=ttk.Button(ventanamod,text="Bicicleta",command=DetallesBici)
    botonBici.grid(column=3,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    botonCamioneta=ttk.Button(ventanamod,text="Camioneta",command=DetallesCamioneta)
    botonCamioneta.grid(column=3,row=4,ipadx=5,ipady=5,padx=10,pady=10)

    botonCamio=ttk.Button(ventanamod,text="Camion",command=DetallesCamion)
    botonCamio.grid(column=4,row=2,ipadx=5,ipady=5,padx=10,pady=10)


    botonVolver=ttk.Button(ventanamod,text="Volver",command=lambda:[MenuPrincial(),ventanamod.destroy()])
    botonVolver.grid(column=5,row=4,ipadx=5,ipady=5,padx=10,pady=10)   

def VentanaUsuarios():
    ventanaUser=Toplevel()
    ventanaUser.title("Menu Usuario")
    ventanaUser.config(width=480,height=320)
    #Titulo
    #Botones
    #Crear user
    botonCrear=ttk.Button(ventanaUser,text="Crear User",command=lambda:[RegistarUser(),ventanaUser.destroy()])
    botonCrear.grid(column=2,row=1,ipadx=5,ipady=5,padx=10,pady=10)
    #Mostar user
    botonMostrar=ttk.Button(ventanaUser,text="Mostrar")#,command=lambda:[MenuPrincial(),ventanaUser.destroy()])
    botonMostrar.grid(column=3,row=1,ipadx=5,ipady=5,padx=10,pady=10)

    botonVoler=ttk.Button(ventanaUser,text="Volver",command=lambda:[MenuPrincial(),ventanaUser.destroy()])
    botonVoler.grid(column=3,row=9,ipadx=5,ipady=5,padx=10,pady=10)

def RegistarUser():
    winUser=Toplevel()
    winUser.title("Crear Usuario")
    winUser.config(width=480,height=320)

    nombreLabel=Label(winUser,text="Nombre: ")
    nombreLabel.grid(column=0,row=1)

    passLabel=Label (winUser,text="Contrase??a: ")
    passLabel.grid(column=0,row=2)

    CorreoLabel=Label (winUser,text="Correo: ")
    CorreoLabel.grid(column=0,row=3)

    nivelLabel=Label(winUser,text="nivel del usuario: ")
    nivelLabel.grid(column=0,row=4)

    #Entrada de info

    
    nombreEntry=Entry(winUser,textvariable=nombreUser)
    nombreEntry.grid(column=1,row=1)

    
    contraEntry=Entry (winUser,textvariable=contraUser,show="*")
    contraEntry.grid(column=1,row=2)

    CorreoEntry=Entry (winUser,textvariable=CorreoUser)
    CorreoEntry.grid(column=1,row=3)

    nivelEntry=Entry (winUser,textvariable=nivelUser)
    nivelEntry.grid(column=1,row=4)

    botonRegistrar=Button (winUser,text="Registrar",command=User)
    botonRegistrar.grid(column=1,row=5,ipadx=5,ipady=5,padx=10,pady=10)

def User():
    name=nombreUser.get()
    passwd=contraUser.get()
    email=CorreoUser.get()
    nivel=int(nivelUser.get())

    newUser=Usuario(name,passwd,email,nivel)
    _usuariosRegistrados.append(newUser)

    messagebox.showinfo("Registro exitoso",f"Se registro el usuaio {name} con exito")

    nombreUser.set("")
    contraUser.set("")
    CorreoUser.set("")
    nivelUser.set("")

