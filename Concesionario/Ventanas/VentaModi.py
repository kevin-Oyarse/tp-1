from Concesionario.data.Auto import obtenerBici, obtenerCamion, obtenerCamioneta, obtenerCole, obtenerMoto
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

    global precioVar

    global numVar

    precioVar=StringVar()
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

    global detalleVar
    global numVar

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
def DetallesMoto():
    detalleauto=Toplevel()
    detalleauto.title("Detalles moto")
    detalleauto.config(width=480,height=320)

    global detalleVar
    global numVar

    detalleVar=StringVar()
    numVar=StringVar()

    selectMoto=Label (detalleauto,text="seleccionar posicion de la moto: ")
    selectMoto.grid(column=1,row=2,ipadx=5,ipady=5,padx=10,pady=10)

    IndexMoto=(Entry(detalleauto,textvariable=numVar))
    IndexMoto.grid(column=2,row=2,ipadx=5,ipady=5,padx=10,pady=10)

    detalleLabel=Label (detalleauto,text="Ingrese detalle: ")
    detalleLabel.grid(column=2,row=4,ipadx=5,ipady=5,padx=10,pady=10)

    detalleEntry=(Entry(detalleauto,textvariable=detalleVar))
    detalleEntry.grid(column=2,row=5,ipadx=5,ipady=5,padx=10,pady=10)

    botonBuscar=ttk.Button(detalleauto,text="Actuazliar detalle",command=cambiardetalle)
    botonBuscar.grid(column=2,row=3,ipadx=5,ipady=5,padx=10,pady=10)
def cambiardetalle():
    num=int(numVar.get())
    moto = obtenerMoto(num)
    moto.detalles = detalleVar.get()

#Colectivo
def DetallesCole():
    detalleauto=Toplevel()
    detalleauto.title("Detalles Colectivo")
    detalleauto.config(width=480,height=320)

    global detalleVar
    global numVar

    detalleVar=StringVar()
    numVar=StringVar()

    selectColectivo=Label (detalleauto,text="seleccionar posicion del Colectivo: ")
    selectColectivo.grid(column=1,row=2,ipadx=5,ipady=5,padx=10,pady=10)

    IndexColectivo=(Entry(detalleauto,textvariable=numVar))
    IndexColectivo.grid(column=2,row=2,ipadx=5,ipady=5,padx=10,pady=10)

    detalleLabel=Label (detalleauto,text="Ingrese detalle: ")
    detalleLabel.grid(column=2,row=4,ipadx=5,ipady=5,padx=10,pady=10)

    detalleEntry=(Entry(detalleauto,textvariable=detalleVar))
    detalleEntry.grid(column=2,row=5,ipadx=5,ipady=5,padx=10,pady=10)

    botonBuscar=ttk.Button(detalleauto,text="Actuazliar detalle",command=cambiardetalle)
    botonBuscar.grid(column=2,row=3,ipadx=5,ipady=5,padx=10,pady=10)
def cambiardetalle():
    num=int(numVar.get())
    Cole = obtenerCole(num)
    Cole.detalles = detalleVar.get()

#Camion
def DetallesCamion():
    detalleauto=Toplevel()
    detalleauto.title("Detalles Camion")
    detalleauto.config(width=480,height=320)

    global detalleVar
    global numVar

    detalleVar=StringVar()
    numVar=StringVar()

    selectCamion=Label (detalleauto,text="seleccionar posicion del Camion: ")
    selectCamion.grid(column=1,row=2,ipadx=5,ipady=5,padx=10,pady=10)

    IndexCamion=(Entry(detalleauto,textvariable=numVar))
    IndexCamion.grid(column=2,row=2,ipadx=5,ipady=5,padx=10,pady=10)

    detalleLabel=Label (detalleauto,text="Ingrese detalle: ")
    detalleLabel.grid(column=2,row=4,ipadx=5,ipady=5,padx=10,pady=10)

    detalleEntry=(Entry(detalleauto,textvariable=detalleVar))
    detalleEntry.grid(column=2,row=5,ipadx=5,ipady=5,padx=10,pady=10)

    botonBuscar=ttk.Button(detalleauto,text="Actuazliar detalle",command=cambiardetalle)
    botonBuscar.grid(column=2,row=3,ipadx=5,ipady=5,padx=10,pady=10)

def cambiardetalle():
    num=int(numVar.get())
    Camion = obtenerCamion(num)
    Camion.detalles = detalleVar.get()

#Camioneta
def DetallesCamioneta():
    detalleauto=Toplevel()
    detalleauto.title("Detalles Camioneta")
    detalleauto.config(width=480,height=320)
    global detalleVar
    global numVar
    detalleVar=StringVar()
    numVar=StringVar()

    selectCamioneta=Label (detalleauto,text="seleccionar posicion del Camioneta: ")
    selectCamioneta.grid(column=1,row=2,ipadx=5,ipady=5,padx=10,pady=10)

    IndexCamioneta=(Entry(detalleauto,textvariable=numVar))
    IndexCamioneta.grid(column=2,row=2,ipadx=5,ipady=5,padx=10,pady=10)

    detalleLabel=Label (detalleauto,text="Ingrese detalle: ")
    detalleLabel.grid(column=2,row=4,ipadx=5,ipady=5,padx=10,pady=10)

    detalleEntry=(Entry(detalleauto,textvariable=detalleVar))
    detalleEntry.grid(column=2,row=5,ipadx=5,ipady=5,padx=10,pady=10)

    botonBuscar=ttk.Button(detalleauto,text="Actuazliar detalle",command=cambiardetalle)
    botonBuscar.grid(column=2,row=3,ipadx=5,ipady=5,padx=10,pady=10)
def cambiardetalle():
    num=int(numVar.get())
    Camioneta = obtenerCamioneta(num)
    Camioneta.detalles = detalleVar.get()
#Bici

def DetallesBici():
    detalleauto=Toplevel()
    detalleauto.title("Detalles Bici")
    detalleauto.config(width=480,height=320)
    global detalleVar
    global numVar
    detalleVar=StringVar()
    numVar=StringVar()

    selectBici=Label (detalleauto,text="seleccionar posicion del Camion: ")
    selectBici.grid(column=1,row=2,ipadx=5,ipady=5,padx=10,pady=10)

    IndexBici=(Entry(detalleauto,textvariable=numVar))
    IndexBici.grid(column=2,row=2,ipadx=5,ipady=5,padx=10,pady=10)

    detalleLabel=Label (detalleauto,text="Ingrese detalle: ")
    detalleLabel.grid(column=2,row=4,ipadx=5,ipady=5,padx=10,pady=10)

    detalleEntry=(Entry(detalleauto,textvariable=detalleVar))
    detalleEntry.grid(column=2,row=5,ipadx=5,ipady=5,padx=10,pady=10)

    botonBuscar=ttk.Button(detalleauto,text="Actuazliar detalle",command=cambiardetalle)
    botonBuscar.grid(column=2,row=3,ipadx=5,ipady=5,padx=10,pady=10)
def cambiardetalle():
    num=int(numVar.get())
    Bici = obtenerBici(num)
    Bici.detalles = detalleVar.get()
#Acoplado

def DetallesAcoplado():
    detalleauto=Toplevel()
    detalleauto.title("Detalles Acoplado")
    detalleauto.config(width=480,height=320)
    global detalleVar
    global numVar
    detalleVar=StringVar()
    numVar=StringVar()

    selectAco=Label (detalleauto,text="seleccionar posicion del Acoplado: ")
    selectAco.grid(column=1,row=2,ipadx=5,ipady=5,padx=10,pady=10)

    IndexAcoplado=(Entry(detalleauto,textvariable=numVar))
    IndexAcoplado.grid(column=2,row=2,ipadx=5,ipady=5,padx=10,pady=10)

    detalleLabel=Label (detalleauto,text="Ingrese detalle: ")
    detalleLabel.grid(column=2,row=4,ipadx=5,ipady=5,padx=10,pady=10)

    detalleEntry=(Entry(detalleauto,textvariable=detalleVar))
    detalleEntry.grid(column=2,row=5,ipadx=5,ipady=5,padx=10,pady=10)

    botonActualizar=ttk.Button(detalleauto,text="Actuazliar detalle",command=cambiardetalle)
    botonActualizar.grid(column=2,row=3,ipadx=5,ipady=5,padx=10,pady=10)
def cambiardetalle():
    num=int(numVar.get())
    auto = obtenerCole(num)
    auto.detalles = detalleVar.get()

def cambiarPrecio():
    num=int(numVar.get())
    auto = obtenerCole(num)
    auto.precio = detalleVar.get()