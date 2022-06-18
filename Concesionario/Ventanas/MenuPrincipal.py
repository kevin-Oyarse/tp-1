from tkinter import ttk as ttk 
from tkinter import *
from model.Usuario import *
from Ventanas.VentaModi import *
from Ventanas.VentanaCargar import*
from data.Auto import _autos
#Ventana del menu
ListaEjemplo = ["Rojo","Ford","$2000","150"]
def MenuPrincial():
    #Ventana
    win=Toplevel()
    win.title ("Menu Principal.")
    win.config(width=480,height=320)

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

    botonLista=ttk.Button(win,text="Mostrar lista de vehiculos",command=lambda:[VentanaListaDeVehiculos(),win.destroy()])
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
    #Text
    for i in _autos:
        print(i)
    Label(ventanaList,textvariable=i)
    botonVoler=ttk.Button(ventanaList,text="Volver",command=lambda:[MenuPrincial(),ventanaList.destroy()])
    botonVoler.grid(column=3,row=9,ipadx=5,ipady=5,padx=10,pady=10)

def VentanaPrecio():
    #Ventana
    ventanamod=Toplevel()
    ventanamod.title("Modificar Precios")
    ventanamod.config(width=480,height=320)
    #Titulo

    #Botones
    botonAuto=ttk.Button(ventanamod,text="Auto",command=PrecioAuto)
    botonAuto.grid (column=2,row=2,ipadx=5,ipady=5,padx=10,pady=10)

    botonMoto=ttk.Button(ventanamod,text=("Moto"))
    botonMoto.grid(column=2,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    botonAcoplado=ttk.Button(ventanamod,text="Acoplado")
    botonAcoplado.grid(column=2,row=4,ipadx=5,ipady=5,padx=10,pady=10)

    botonColectivo=ttk.Button(ventanamod,text="Colectivo")
    botonColectivo.grid(column=3,row=2,ipadx=5,ipady=5,padx=10,pady=10)

    botonBici=ttk.Button(ventanamod,text="Bicicleta")
    botonBici.grid(column=3,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    botonCamioneta=ttk.Button(ventanamod,text="Camioneta")
    botonCamioneta.grid(column=3,row=4,ipadx=5,ipady=5,padx=10,pady=10)

    botonCamio=ttk.Button(ventanamod,text="Camion")
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
    botonAuto=ttk.Button(ventanamod,text="Auto")
    botonAuto.grid (column=2,row=2,ipadx=5,ipady=5,padx=10,pady=10)

    botonMoto=ttk.Button(ventanamod,text=("Moto"))
    botonMoto.grid(column=2,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    botonAcoplado=ttk.Button(ventanamod,text="Acoplado")
    botonAcoplado.grid(column=2,row=4,ipadx=5,ipady=5,padx=10,pady=10)

    botonColectivo=ttk.Button(ventanamod,text="Colectivo")
    botonColectivo.grid(column=3,row=2,ipadx=5,ipady=5,padx=10,pady=10)

    botonCamioneta=ttk.Button(ventanamod,text="Camioneta")
    botonCamioneta.grid(column=3,row=4,ipadx=5,ipady=5,padx=10,pady=10)

    botonCamio=ttk.Button(ventanamod,text="Camion")
    botonCamio.grid(column=4,row=2,ipadx=5,ipady=5,padx=10,pady=10)


    botonVolver=ttk.Button(ventanamod,text="Volver",command=lambda:[MenuPrincial(),ventanamod.destroy()])
    botonVolver.grid(column=5,row=4,ipadx=5,ipady=5,padx=10,pady=10)
    
def VentanaDetalles():
    ventanamod=Toplevel()
    ventanamod.title("Modificar detalles")
    ventanamod.config(width=480,height=320)
    #Titulo

    #Botones
    botonAuto=ttk.Button(ventanamod,text="Auto")
    botonAuto.grid (column=2,row=2,ipadx=5,ipady=5,padx=10,pady=10)

    botonMoto=ttk.Button(ventanamod,text=("Moto"))
    botonMoto.grid(column=2,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    botonAcoplado=ttk.Button(ventanamod,text="Acoplado")
    botonAcoplado.grid(column=2,row=4,ipadx=5,ipady=5,padx=10,pady=10)

    botonColectivo=ttk.Button(ventanamod,text="Colectivo")
    botonColectivo.grid(column=3,row=2,ipadx=5,ipady=5,padx=10,pady=10)

    botonBici=ttk.Button(ventanamod,text="Bicicleta")
    botonBici.grid(column=3,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    botonCamioneta=ttk.Button(ventanamod,text="Camioneta")
    botonCamioneta.grid(column=3,row=4,ipadx=5,ipady=5,padx=10,pady=10)

    botonCamio=ttk.Button(ventanamod,text="Camion")
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
    botonCrear=ttk.Button(ventanaUser,text="Crear User")#,command=lambda:[MenuPrincial(),ventanaUser.destroy()])
    botonCrear.grid(column=2,row=1,ipadx=5,ipady=5,padx=10,pady=10)
    #Mostar user
    botonMostrar=ttk.Button(ventanaUser,text="Mostrar")#,command=lambda:[MenuPrincial(),ventanaUser.destroy()])
    botonMostrar.grid(column=3,row=1,ipadx=5,ipady=5,padx=10,pady=10)

    botonVoler=ttk.Button(ventanaUser,text="Volver",command=lambda:[MenuPrincial(),ventanaUser.destroy()])
    botonVoler.grid(column=3,row=9,ipadx=5,ipady=5,padx=10,pady=10)

