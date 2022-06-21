from model.Auto import *
from tkinter import ttk as ttk 
from tkinter import *
from model.Auto import *
from data.Auto import _autos,obtenerAuto

#Auto
def PrecioAuto():
    precioauto=Toplevel()
    precioauto.title("Cargar auto")
    precioauto.config(width=400,height=320)
    #String Var
    global marcaVar
    global modeloVar
    global precioVar
    global estadoVar
    global kmVar
    global detalleVar
    global numVar
    marcaVar=StringVar()
    modeloVar=StringVar()
    precioVar=StringVar()
    estadoVar=StringVar()
    kmVar=StringVar()
    detalleVar=StringVar()
    numVar=StringVar()

    #Entrada de datos
    precioLabel=Label(precioauto,text=_autos)
    precioLabel.grid(column=4,row=4)
    precioEntry=Entry(precioauto,textvariable=precioVar)
    precioEntry.grid(column=1,row=4,columnspan=2)
    #Botones
    botonCargar=ttk.Button (precioauto,text="Cambiar precio")
    botonCargar.grid(column=1,row=14)
    botonVolver=ttk.Button(precioauto,text="cerrar ventana",command=precioauto.destroy)
    botonVolver.grid(column=3,row=14)

def DetallesAuto():
    detalleauto=Toplevel()
    detalleauto.title("Detalles auto")
    detalleauto.config(width=480,height=320)
    global marcaVar
    global modeloVar
    global precioVar
    global estadoVar
    global kmVar
    global detalleVar
    global numVar
    marcaVar=StringVar()
    modeloVar=StringVar()
    precioVar=StringVar()
    estadoVar=StringVar()
    kmVar=StringVar()
    detalleVar=StringVar()
    numVar=StringVar()

    selectAuto=Label (detalleauto,text="seleccionar posicion del auto: ")
    selectAuto.grid(column=1,row=2,ipadx=5,ipady=5,padx=10,pady=10)

    IndexAuto=(Entry(detalleauto,textvariable=numVar))
    IndexAuto.grid(column=2,row=2,ipadx=5,ipady=5,padx=10,pady=10)

    detalleLabel=Label (detalleauto,text="Ingrese detalle: ")
    detalleLabel.grid(column=2,row=4,ipadx=5,ipady=5,padx=10,pady=10)

    detalleEntry=(Entry(detalleauto,textvariable=detalleVar))
    detalleEntry.grid(column=2,row=5,ipadx=5,ipady=5,padx=10,pady=10)

    botonBuscar=ttk.Button(detalleauto,text="Actuazliar detalle",command=cambiardetalle)
    botonBuscar.grid(column=2,row=3,ipadx=5,ipady=5,padx=10,pady=10)

def cambiardetalle():
    num=int(numVar.get())
    auto = obtenerAuto(num)
    auto.detalles = detalleVar.get()

#Moto

#Colectivo

#Camion

#Camioneta

#Bici

#Acoplado