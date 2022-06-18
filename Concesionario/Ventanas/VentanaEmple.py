from cProfile import label
from enum import auto
from msilib.schema import ComboBox
from optparse import Values
from platform import win32_edition
from tkinter import ttk as ttk 
from tkinter import *
from turtle import width
from model.Usuario import *
from Ventanas.VentaModi import *
from Ventanas.VentanaCargar import*
from data.Auto import _autos
#Ventana del menu
ListaEjemplo = ["Rojo","Ford","$2000","150"]
def MenuEmpleado():
    #Ventana
    win=Toplevel()
    win.title ("Menu Principal.")
    win.config(width=480,height=320)

    #titulo
    #botones

    botonkm=ttk.Button(win,text="Modificar km de los vehiculos",command=lambda:[VentanaKm(),win.destroy()])
    botonkm.grid(column=2,row=3,ipadx=5,ipady=5,padx=10,pady=10)


    botonDetalles=ttk.Button(win,text="Agregar detalles a vehiculos",command=lambda:[VentanaDetalles(),win.destroy()])
    botonDetalles.grid(column=3,row=2,ipadx=5,ipady=5,padx=10,pady=10)

    botonLista=ttk.Button(win,text="Mostrar lista de vehiculos",command=lambda:[VentanaListaDeVehiculos(),win.destroy()])
    botonLista.grid(column=3,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    botonSalir=ttk.Button(win,text="Salir",command=quit)
    botonSalir.grid(column=2,row=7,ipadx=5,ipady=5,padx=10,pady=10,columnspan=2)


def VentanaListaDeVehiculos():
    ventanaList=Toplevel()
    ventanaList.title("Lista Vehiculos")
    ventanaList.config(width=480,height=320)
    #Text
    
    
  
        
    botonVoler=ttk.Button(ventanaList,text="Volver",command=lambda:[MenuEmpleado(),ventanaList.destroy()])
    botonVoler.grid(column=3,row=9,ipadx=5,ipady=5,padx=10,pady=10)


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


    botonVolver=ttk.Button(ventanamod,text="Volver",command=lambda:[MenuEmpleado(),ventanamod.destroy()])
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


    botonVolver=ttk.Button(ventanamod,text="Volver",command=lambda:[MenuEmpleado(),ventanamod.destroy()])
    botonVolver.grid(column=5,row=4,ipadx=5,ipady=5,padx=10,pady=10)   


