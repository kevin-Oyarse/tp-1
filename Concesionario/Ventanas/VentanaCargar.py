from tkinter import ttk as ttk 
from tkinter import *
from model.Auto import *
from data.Auto import *

#auto
def Cargar_Auto():
    #Ventana

    winauto=Toplevel()
    winauto.title("Cargar auto")
    winauto.config(width=400,height=320)
    #String Var
    global marcaVar
    global modeloVar
    global precioVar
    global estadoVar
    global kmVar
    global detalleVar
    marcaVar=StringVar()
    modeloVar=StringVar()
    precioVar=StringVar()
    estadoVar=StringVar()
    kmVar=StringVar()
    detalleVar=StringVar()

    #Label
    marcaLabel=Label(winauto,text="Marca")
    marcaLabel.grid(column=1,row=1,columnspan=2)

    modeloLabel=Label(winauto,text="Modelo:")
    modeloLabel.grid(column=3,row=1,columnspan=2)

    precioLabel=Label(winauto,text="Precio:")
    precioLabel.grid(column=1,row=3,columnspan=2)

    estadoLabel=Label(winauto,text="Estado:")
    estadoLabel.grid(column=3,row=3,columnspan=2)

    detalleLabel=Label(winauto,text="Detalle")
    detalleLabel.grid(column=1,row=5,columnspan=2)

    kmLabel=Label(winauto,text=("km:"))
    kmLabel.grid(column=3,row=5,columnspan=2)
    #Entrada de datos
    marcaEntry=Entry(winauto,textvariable=marcaVar)
    marcaEntry.grid(column=1,row=2,columnspan=2)

    modeloEntry=Entry(winauto,textvariable=modeloVar)
    modeloEntry.grid(column=3,row=2,columnspan=2)

    precioEntry=Entry(winauto,textvariable=precioVar)
    precioEntry.grid(column=1,row=4,columnspan=2)

    estadoEntry=Entry(winauto,textvariable=estadoVar)
    estadoEntry.grid(column=3,row=4,columnspan=2)

    detalleEntry=Entry(winauto,textvariable=detalleVar)
    detalleEntry.grid(column=1,row=6,columnspan=2)

    kmEntry=Entry(winauto,textvariable=kmVar)
    kmEntry.grid(column=3,row=6,columnspan=2)

    #Botones
    botonCargar=ttk.Button (winauto,text="Cargar Auto",command=ingresar_auto)
    botonCargar.grid(column=1,row=14)
    botonVolver=ttk.Button(winauto,text="cerrar ventana",command=winauto.destroy)
    botonVolver.grid(column=3,row=14)
#moto
def Cargar_Moto():
    #Ventana

    winauto=Toplevel()
    winauto.title("Cargar Moto")
    winauto.config(width=400,height=320)

    #Label
    marcaLabel=Label(winauto,text="Marca")
    marcaLabel.grid(column=1,row=1,columnspan=2)

    modeloLabel=Label(winauto,text="Modelo:")
    modeloLabel.grid(column=3,row=1,columnspan=2)

    precioLabel=Label(winauto,text="Precio:")
    precioLabel.grid(column=1,row=3,columnspan=2)

    estadoLabel=Label(winauto,text="Estado:")
    estadoLabel.grid(column=3,row=3,columnspan=2)

    detalleLabel=Label(winauto,text="Detalle")
    detalleLabel.grid(column=1,row=5,columnspan=2)

    kmLabel=Label(winauto,text=("km:"))
    kmLabel.grid(column=3,row=5,columnspan=2)
    #Entrada de datos
    marcaEntry=Entry(winauto)
    marcaEntry.grid(column=1,row=2,columnspan=2)

    modeloEntry=Entry(winauto)
    modeloEntry.grid(column=3,row=2,columnspan=2)

    precioEntry=Entry(winauto)
    precioEntry.grid(column=1,row=4,columnspan=2)

    estadoEntry=Entry(winauto)
    estadoEntry.grid(column=3,row=4,columnspan=2)

    detalleEntry=Entry(winauto)
    detalleEntry.grid(column=1,row=6,columnspan=2)

    kmEntry=Entry(winauto)
    kmEntry.grid(column=3,row=6,columnspan=2)

    #Botones
    botonCargar=ttk.Button (winauto,text="Cargar Moto",textvariable=ingrese_moto)
    botonCargar.grid(column=1,row=14)
    botonVolver=ttk.Button(winauto,text="cerrar ventana",command=winauto.destroy)
    botonVolver.grid(column=3,row=14)
#camioneta
def Cargar_camioneta():
    #Ventana

    winauto=Toplevel()
    winauto.title("Cargar Camioneta")
    winauto.config(width=400,height=320)

    #Label
    marcaLabel=Label(winauto,text="Marca")
    marcaLabel.grid(column=1,row=1,columnspan=2)

    modeloLabel=Label(winauto,text="Modelo:")
    modeloLabel.grid(column=3,row=1,columnspan=2)

    precioLabel=Label(winauto,text="Precio:")
    precioLabel.grid(column=1,row=3,columnspan=2)

    estadoLabel=Label(winauto,text="Estado:")
    estadoLabel.grid(column=3,row=3,columnspan=2)

    detalleLabel=Label(winauto,text="Detalle")
    detalleLabel.grid(column=1,row=5,columnspan=2)

    kmLabel=Label(winauto,text=("km:"))
    kmLabel.grid(column=3,row=5,columnspan=2)
    #Entrada de datos
    marcaEntry=Entry(winauto)
    marcaEntry.grid(column=1,row=2,columnspan=2)

    modeloEntry=Entry(winauto)
    modeloEntry.grid(column=3,row=2,columnspan=2)

    precioEntry=Entry(winauto)
    precioEntry.grid(column=1,row=4,columnspan=2)

    estadoEntry=Entry(winauto)
    estadoEntry.grid(column=3,row=4,columnspan=2)

    detalleEntry=Entry(winauto)
    detalleEntry.grid(column=1,row=6,columnspan=2)

    kmEntry=Entry(winauto)
    kmEntry.grid(column=3,row=6,columnspan=2)

    #Botones
    botonCargar=ttk.Button (winauto,text="Cargar camioneta",textvariable=ingrese_camioneta)
    botonCargar.grid(column=1,row=14)
    botonVolver=ttk.Button(winauto,text="cerrar ventana",command=winauto.destroy)
    botonVolver.grid(column=3,row=14)
#colectivo
def Cargar_Colectivo():
    #Ventana

    winauto=Toplevel()
    winauto.title("Cargar Colectivo")
    winauto.config(width=400,height=320)

    #Label
    marcaLabel=Label(winauto,text="Marca")
    marcaLabel.grid(column=1,row=1,columnspan=2)

    modeloLabel=Label(winauto,text="Modelo:")
    modeloLabel.grid(column=3,row=1,columnspan=2)

    precioLabel=Label(winauto,text="Precio:")
    precioLabel.grid(column=1,row=3,columnspan=2)

    estadoLabel=Label(winauto,text="Estado:")
    estadoLabel.grid(column=3,row=3,columnspan=2)

    detalleLabel=Label(winauto,text="Detalle")
    detalleLabel.grid(column=1,row=5,columnspan=2)

    kmLabel=Label(winauto,text=("km:"))
    kmLabel.grid(column=3,row=5,columnspan=2)
    #Entrada de datos
    marcaEntry=Entry(winauto)
    marcaEntry.grid(column=1,row=2,columnspan=2)

    modeloEntry=Entry(winauto)
    modeloEntry.grid(column=3,row=2,columnspan=2)

    precioEntry=Entry(winauto)
    precioEntry.grid(column=1,row=4,columnspan=2)

    estadoEntry=Entry(winauto)
    estadoEntry.grid(column=3,row=4,columnspan=2)

    detalleEntry=Entry(winauto)
    detalleEntry.grid(column=1,row=6,columnspan=2)

    kmEntry=Entry(winauto)
    kmEntry.grid(column=3,row=6,columnspan=2)

    #Botones
    botonCargar=ttk.Button (winauto,text="Cargar Colectivo",textvariable=ingrese_colectivo)
    botonCargar.grid(column=1,row=14)
    botonVolver=ttk.Button(text="cerrar ventana",command=winauto.destroy)
    botonVolver.grid(column=3,row=14)
#Camion
def Cargar_Camion():
    #Ventana

    winauto=Toplevel()
    winauto.title("Cargar Camion")
    winauto.config(width=400,height=320)

    #Label
    marcaLabel=Label(winauto,text="Marca")
    marcaLabel.grid(column=1,row=1,columnspan=2)

    modeloLabel=Label(winauto,text="Modelo:")
    modeloLabel.grid(column=3,row=1,columnspan=2)

    precioLabel=Label(winauto,text="Precio:")
    precioLabel.grid(column=1,row=3,columnspan=2)

    estadoLabel=Label(winauto,text="Estado:")
    estadoLabel.grid(column=3,row=3,columnspan=2)

    detalleLabel=Label(winauto,text="Detalle")
    detalleLabel.grid(column=1,row=5,columnspan=2)

    kmLabel=Label(winauto,text=("km:"))
    kmLabel.grid(column=3,row=5,columnspan=2)
    #Entrada de datos
    marcaEntry=Entry(winauto)
    marcaEntry.grid(column=1,row=2,columnspan=2)

    modeloEntry=Entry(winauto)
    modeloEntry.grid(column=3,row=2,columnspan=2)

    precioEntry=Entry(winauto)
    precioEntry.grid(column=1,row=4,columnspan=2)

    estadoEntry=Entry(winauto)
    estadoEntry.grid(column=3,row=4,columnspan=2)

    detalleEntry=Entry(winauto)
    detalleEntry.grid(column=1,row=6,columnspan=2)

    kmEntry=Entry(winauto)
    kmEntry.grid(column=3,row=6,columnspan=2)

    #Botones
    botonCargar=ttk.Button (winauto,text="Cargar Camion",command=ingrese_camion)
    botonCargar.grid(column=1,row=14)
    botonVolver=ttk.Button(winauto,text="cerrar ventana",command=winauto.destroy)
    botonVolver.grid(column=3,row=14)
#Acoplado
def Cargar_Acoplado():
    #Ventana

    winauto=Toplevel()
    winauto.title("Cargar Acoplado")
    winauto.config(width=400,height=320)

    #Label
    marcaLabel=Label(winauto,text="Marca")
    marcaLabel.grid(column=1,row=1,columnspan=2)

    modeloLabel=Label(winauto,text="Modelo:")
    modeloLabel.grid(column=3,row=1,columnspan=2)

    precioLabel=Label(winauto,text="Precio:")
    precioLabel.grid(column=1,row=3,columnspan=2)

    estadoLabel=Label(winauto,text="Estado:")
    estadoLabel.grid(column=3,row=3,columnspan=2)

    detalleLabel=Label(winauto,text="Detalle")
    detalleLabel.grid(column=1,row=5,columnspan=2)

    kmLabel=Label(winauto,text=("km:"))
    kmLabel.grid(column=3,row=5,columnspan=2)
    #Entrada de datos
    marcaEntry=Entry(winauto)
    marcaEntry.grid(column=1,row=2,columnspan=2)

    modeloEntry=Entry(winauto)
    modeloEntry.grid(column=3,row=2,columnspan=2)

    precioEntry=Entry(winauto)
    precioEntry.grid(column=1,row=4,columnspan=2)

    estadoEntry=Entry(winauto)
    estadoEntry.grid(column=3,row=4,columnspan=2)

    detalleEntry=Entry(winauto)
    detalleEntry.grid(column=1,row=6,columnspan=2)

    kmEntry=Entry(winauto)
    kmEntry.grid(column=3,row=6,columnspan=2)

    #Botones
    botonCargar=ttk.Button (winauto,text="Cargar Acoplado",command=ingrese_acoplado)
    botonCargar.grid(column=1,row=14)
    botonVolver=ttk.Button(winauto,text="cerrar ventana",command=winauto.destroy)
    botonVolver.grid(column=3,row=14)
#Bici
def Cargar_Bici():
    #Ventana

    winauto=Toplevel()
    winauto.title("Cargar Bicicleta")
    winauto.config(width=400,height=320)

    #Label
    marcaLabel=Label(winauto,text="Marca")
    marcaLabel.grid(column=1,row=1,columnspan=2)

    modeloLabel=Label(winauto,text="Modelo:")
    modeloLabel.grid(column=3,row=1,columnspan=2)

    precioLabel=Label(winauto,text="Precio:")
    precioLabel.grid(column=1,row=3,columnspan=2)

    estadoLabel=Label(winauto,text="Estado:")
    estadoLabel.grid(column=3,row=3,columnspan=2)

    detalleLabel=Label(winauto,text="Detalle")
    detalleLabel.grid(column=1,row=5,columnspan=2)
    #Entrada de datos
    marcaEntry=Entry(winauto)
    marcaEntry.grid(column=1,row=2,columnspan=2)

    modeloEntry=Entry(winauto)
    modeloEntry.grid(column=3,row=2,columnspan=2)

    precioEntry=Entry(winauto)
    precioEntry.grid(column=1,row=4,columnspan=2)

    estadoEntry=Entry(winauto)
    estadoEntry.grid(column=3,row=4,columnspan=2)

    detalleEntry=Entry(winauto)
    detalleEntry.grid(column=1,row=6,columnspan=2)

    #Botones
    botonCargar=ttk.Button (winauto,text="Cargar Bici",command=ingrese_bicicleta)
    botonCargar.grid(column=1,row=14)
    botonVolver=ttk.Button(winauto,text="cerrar ventana",command=winauto.destroy)
    botonVolver.grid(column=3,row=14)



#Cargar Autos
def ingresar_auto():
    marca=marcaVar.get()
    modelo=modeloVar.get()
    estado=estadoVar.get()
    km=kmVar.get()
    precio=precioVar.get()
    estado=estadoVar.get()
    detalle=detalleVar.get()
    auto_ingresado=Auto(marca,modelo,km,detalle,precio,estado)
    agregaAutos(auto_ingresado)

def ingrese_moto():
    marca=marcaVar.get()
    modelo=modeloVar.get()
    estado=estadoVar.get()
    km=kmVar.get()
    precio=precioVar.get()
    estado=estadoVar.get()
    detalle=detalleVar.get()
    moto_ingresado=Auto(marca, modelo,km,detalle,precio,estado)
    agregarMoto(moto_ingresado)

def ingrese_acoplado():
    marca=marcaVar.get()
    modelo=modeloVar.get()
    estado=estadoVar.get()
    km=kmVar.get()
    precio=precioVar.get()
    estado=estadoVar.get()
    detalle=detalleVar.get()
    acoplado_ingresado=Auto(marca, modelo,km,detalle,precio,estado)
    agregarAcoplado(acoplado_ingresado)

def ingrese_bicicleta():
    marca=marcaVar.get()
    modelo=modeloVar.get()
    estado=estadoVar.get()
    precio=precioVar.get()
    estado=estadoVar.get()
    detalle=detalleVar.get()
    bicicleta_ingresado=Bicleta(marca, modelo,detalle,precio,estado)
    agregarbici(bicicleta_ingresado)

def ingrese_camioneta():
    marca=marcaVar.get()
    modelo=modeloVar.get()
    estado=estadoVar.get()
    km=kmVar.get()
    precio=precioVar.get()
    estado=estadoVar.get()
    detalle=detalleVar.get()
    camioneta_ingresado=Auto(marca, modelo,km,detalle,precio,estado)
    agregarCamioneta(camioneta_ingresado)

def ingrese_camion():
    marca=marcaVar.get()
    modelo=modeloVar.get()
    estado=estadoVar.get()
    km=kmVar.get()
    precio=precioVar.get()
    estado=estadoVar.get()
    detalle=detalleVar.get()
    camion_ingresado=Auto(marca, modelo,km,detalle,precio,estado)
    agregarCamion(camion_ingresado)

def ingrese_colectivo():
    marca=marcaVar.get()
    modelo=modeloVar.get()
    estado=estadoVar.get()
    km=kmVar.get()
    precio=precioVar.get()
    estado=estadoVar.get()
    detalle=detalleVar.get()
    colectivo_ingresado=Auto(marca, modelo,km,detalle,precio,estado)
    agregarcolectivo(colectivo_ingresado)
