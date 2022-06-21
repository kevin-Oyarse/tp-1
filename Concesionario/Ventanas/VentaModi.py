from Concesionario.data.Auto import obtenerAcoplado
from data.Auto import obtenerBici, obtenerCamion, obtenerCamioneta, obtenerCole, obtenerMoto
from model.Auto import *
from tkinter import ttk as ttk 
from tkinter import *
from model.Auto import *
from data.Auto import _autos,obtenerAuto

#Auto
def PrecioAuto():
    precioauto=Toplevel()
    precioauto.title("Precio auto")
    precioauto.config(width=400,height=320)
    #String Var

    global precioVar
    global numVar

    precioVar=StringVar()
    numVar=StringVar()

    #Entrada de datos
    selectAuto=Label (precioauto,text="seleccionar posicion del auto: ")
    selectAuto.grid(column=1,row=2,ipadx=5,ipady=5,padx=10,pady=10)

    IndexAuto=(Entry(precioauto,textvariable=numVar))
    IndexAuto.grid(column=2,row=2,ipadx=5,ipady=5,padx=10,pady=10)

    detalleLabel=Label (precioauto,text="Ingrese Precio nuevo: ")
    detalleLabel.grid(column=1,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    detalleEntry=(Entry(precioauto,textvariable=precioVar))
    detalleEntry.grid(column=2,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    #Botones
    botonCargar=ttk.Button (precioauto,text="Cambiar precio",command=cambiarPrecio)
    botonCargar.grid(column=1,row=14)
    botonVolver=ttk.Button(precioauto,text="cerrar ventana",command=precioauto.destroy)
    botonVolver.grid(column=3,row=14)
def cambiarPrecio():
    num=int(numVar.get())
    auto = obtenerAuto(num)
    auto.precio = precioVar.get()
    
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
    detalleLabel.grid(column=1,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    detalleEntry=(Entry(detalleauto,textvariable=detalleVar))
    detalleEntry.grid(column=2,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    botonBuscar=ttk.Button(detalleauto,text="Actuazliar detalle",command=cambiardetalle)
    botonBuscar.grid(column=1,row=14)
    botonVolver=ttk.Button(detalleauto,text="cerrar ventana",command=detalleauto.destroy)
    botonVolver.grid(column=3,row=14)
def cambiardetalle():
    num=int(numVar.get())
    auto = obtenerAuto(num)
    auto.detalles = detalleVar.get()

#Moto
def PrecioMoto():
    preciomoto=Toplevel()
    preciomoto.title("Precio auto")
    preciomoto.config(width=400,height=320)
    #String Var

    global precioVar
    global numVar

    precioVar=StringVar()
    numVar=StringVar()

    #Entrada de datos
    selectAuto=Label (preciomoto,text="seleccionar posicion del auto: ")
    selectAuto.grid(column=1,row=2,ipadx=5,ipady=5,padx=10,pady=10)

    IndexAuto=(Entry(preciomoto,textvariable=numVar))
    IndexAuto.grid(column=2,row=2,ipadx=5,ipady=5,padx=10,pady=10)

    detalleLabel=Label (preciomoto,text="Ingrese Precio nuevo: ")
    detalleLabel.grid(column=1,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    detalleEntry=(Entry(preciomoto,textvariable=precioVar))
    detalleEntry.grid(column=2,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    #Botones
    botonCargar=ttk.Button (preciomoto,text="Cambiar precio",command=cambiarPrecio)
    botonCargar.grid(column=1,row=14)
    botonVolver=ttk.Button(preciomoto,text="cerrar ventana",command=preciomoto.destroy)
    botonVolver.grid(column=3,row=14)
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
    detalleLabel.grid(column=1,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    detalleEntry=(Entry(detalleauto,textvariable=detalleVar))
    detalleEntry.grid(column=2,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    botonActualizar=ttk.Button(detalleauto,text="Actuazliar detalle",command=cambiardetalle)
    botonActualizar.grid(column=1,row=14)

    botonVolver=ttk.Button(detalleauto,text="cerrar ventana",command=detalleauto.destroy)
    botonVolver.grid(column=3,row=14)

def cambiardetalle():
    num=int(numVar.get())
    moto = obtenerMoto(num)
    moto.detalles = detalleVar.get()
def cambiarPrecio():
    num=int(numVar.get())
    moto = obtenerMoto(num)
    moto.precio = precioVar.get()
#Colectivo
def PrecioCole():
    detalleauto=Toplevel()
    detalleauto.title("Precios Colectivo")
    detalleauto.config(width=480,height=320)

    global detalleVar
    global numVar

    detalleVar=StringVar()
    numVar=StringVar()

    selectColectivo=Label (detalleauto,text="seleccionar posicion del Colectivo: ")
    selectColectivo.grid(column=1,row=2,ipadx=5,ipady=5,padx=10,pady=10)

    IndexColectivo=(Entry(detalleauto,textvariable=numVar))
    IndexColectivo.grid(column=2,row=2,ipadx=5,ipady=5,padx=10,pady=10)

    detalleLabel=Label (detalleauto,text="Ingrese precio: ")
    detalleLabel.grid(column=1,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    detalleEntry=(Entry(detalleauto,textvariable=precioVar))
    detalleEntry.grid(column=2,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    botonActualizar=ttk.Button(detalleauto,text="Actuazliar precio",command=cambiarPrecio)
    botonActualizar.grid(column=1,row=14)

    botonVolver=ttk.Button(detalleauto,text="cerrar ventana",command=detalleauto.destroy)
    botonVolver.grid(column=3,row=14)
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
    detalleLabel.grid(column=1,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    detalleEntry=(Entry(detalleauto,textvariable=detalleVar))
    detalleEntry.grid(column=2,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    botonActualizar=ttk.Button(detalleauto,text="Actuazliar detalle",command=cambiardetalle)
    botonActualizar.grid(column=1,row=14)

    botonVolver=ttk.Button(detalleauto,text="cerrar ventana",command=detalleauto.destroy)
    botonVolver.grid(column=3,row=14)

def cambiardetalle():
    num=int(numVar.get())
    Cole = obtenerCole(num)
    Cole.detalles = detalleVar.get()
def cambiarPrecio():
    num=int(numVar.get())
    Cole = obtenerCole(num)
    Cole.precio = precioVar.get()

#Camion
def PrecioCamion():
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

    detalleLabel=Label (detalleauto,text="Ingrese precio: ")
    detalleLabel.grid(column=1,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    detalleEntry=(Entry(detalleauto,textvariable=precioVar))
    detalleEntry.grid(column=2,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    botonActualizar=ttk.Button(detalleauto,text="Actuazliar precio",command=cambiarPrecio)
    botonActualizar.grid(column=1,row=14)

    botonVolver=ttk.Button(detalleauto,text="cerrar ventana",command=detalleauto.destroy)
    botonVolver.grid(column=3,row=14)
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
    detalleLabel.grid(column=1,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    detalleEntry=(Entry(detalleauto,textvariable=detalleVar))
    detalleEntry.grid(column=2,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    botonActualizar=ttk.Button(detalleauto,text="Actuazliar detalle",command=cambiardetalle)
    botonActualizar.grid(column=1,row=14)

    botonVolver=ttk.Button(detalleauto,text="cerrar ventana",command=detalleauto.destroy)
    botonVolver.grid(column=3,row=14)

def cambiardetalle():
    num=int(numVar.get())
    Camion = obtenerCamion(num)
    Camion.detalles = detalleVar.get()
def cambiarPrecio():
    num=int(numVar.get())
    Cole = obtenerCamion(num)
    Cole.precio = precioVar.get()
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
    detalleLabel.grid(column=1,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    detalleEntry=(Entry(detalleauto,textvariable=detalleVar))
    detalleEntry.grid(column=2,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    botonActualizar=ttk.Button(detalleauto,text="Actuazliar detalle",command=cambiardetalle)
    botonActualizar.grid(column=1,row=14)

    botonVolver=ttk.Button(detalleauto,text="cerrar ventana",command=detalleauto.destroy)
    botonVolver.grid(column=3,row=14)
def cambiardetalle():
    num=int(numVar.get())
    Camioneta = obtenerCamioneta(num)
    Camioneta.detalles = detalleVar.get()
#Bici
def PrecioBici():
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

    detalleLabel=Label (detalleauto,text="Ingrese precio: ")
    detalleLabel.grid(column=1,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    detalleEntry=(Entry(detalleauto,textvariable=precioVar))
    detalleEntry.grid(column=2,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    botonActualizar=ttk.Button(detalleauto,text="Actuazliar precio",command=cambiardetalle)
    botonActualizar.grid(column=1,row=14)

    botonVolver=ttk.Button(detalleauto,text="cerrar ventana",command=detalleauto.destroy)
    botonVolver.grid(column=3,row=14)
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
    detalleLabel.grid(column=1,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    detalleEntry=(Entry(detalleauto,textvariable=detalleVar))
    detalleEntry.grid(column=2,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    botonActualizar=ttk.Button(detalleauto,text="Actuazliar detalle",command=cambiardetalle)
    botonActualizar.grid(column=1,row=14)

    botonVolver=ttk.Button(detalleauto,text="cerrar ventana",command=detalleauto.destroy)
    botonVolver.grid(column=3,row=14)

def cambiardetalle():
    num=int(numVar.get())
    Bici = obtenerBici(num)
    Bici.detalles = detalleVar.get()
def cambiarprecio():
    num=int(numVar.get())
    Bici = obtenerBici(num)
    Bici.precio = precioVar.get()
#Acoplado
def PrecioAcoplado():
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

    detalleLabel=Label (detalleauto,text="Ingrese precio: ")
    detalleLabel.grid(column=1,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    detalleEntry=(Entry(detalleauto,textvariable=precioVar))
    detalleEntry.grid(column=2,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    botonActualizar=ttk.Button(detalleauto,text="Actuazliar precio",command=cambiarPrecio)
    botonActualizar.grid(column=1,row=14)

    botonVolver=ttk.Button(detalleauto,text="cerrar ventana",command=detalleauto.destroy)
    botonVolver.grid(column=3,row=14)
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
    detalleLabel.grid(column=1,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    detalleEntry=(Entry(detalleauto,textvariable=detalleVar))
    detalleEntry.grid(column=2,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    botonActualizar=ttk.Button(detalleauto,text="Actuazliar detalle",command=cambiardetalle)
    botonActualizar.grid(column=1,row=14)

    botonVolver=ttk.Button(detalleauto,text="cerrar ventana",command=detalleauto.destroy)
    botonVolver.grid(column=3,row=14)

def cambiardetalle():
    num=int(numVar.get())
    auto = obtenerCole(num)
    auto.detalles = detalleVar.get()
def cambiarPrecio():
    num=int(numVar.get())
    auto = obtenerAcoplado(num)
    auto.precio = precioVar.get()