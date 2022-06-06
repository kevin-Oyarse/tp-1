from tkinter import ttk as ttk 
from tkinter import *
from constructores.Constructores import ingrese_auto



#Ventana del menu
def MenuPrincial():
    #Ventana
    win=Toplevel()
    win.title ("Menu Principal.")
    win.config(width=480,height=320)

    #titulo

    #botones

    loginButon=ttk.Button(win,text="Cargar vehiculos",command=lambda:[cargarVehiculos(),win.destroy()])
    loginButon.grid(column=2,row=1,ipadx=5,ipady=5,padx=10,pady=10)

    loginButon=ttk.Button(win,text="Modificar precios de los vehiculos")#command=)
    loginButon.grid(column=2,row=2,ipadx=5,ipady=5,padx=10,pady=10)

    loginButon=ttk.Button(win,text="Modificar km de los vehiculos")#command=)
    loginButon.grid(column=2,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    loginButon=ttk.Button(win,text="Menu usuario")#command=)
    loginButon.grid(column=3,row=1,ipadx=5,ipady=5,padx=10,pady=10)

    loginButon=ttk.Button(win,text="Agregar detalles a vehiculos")#command=)
    loginButon.grid(column=3,row=2,ipadx=5,ipady=5,padx=10,pady=10)

    loginButon=ttk.Button(win,text="Mostrar lista de vehiculos")#command=)
    loginButon.grid(column=3,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    loginButon=ttk.Button(win,text="Salir",command=quit)
    loginButon.grid(column=2,row=7,ipadx=5,ipady=5,padx=10,pady=10,columnspan=2)

def cargarVehiculos():
    #Ventana
    winV=Toplevel()
    winV.title("Cargar Vehiculos")
    winV.config(width=480,height=320)

    #Titulo
    titulo=Label(winV,text="Cargar Vehiculo",font=("Arial",24))
    titulo.grid(column=2,row=0,padx=10,pady=10,columnspan=2)
    #botones

    upAutos=ttk.Button(winV,text="Cargar Auto",command=lambda:[Cargar_Auto(),winV.destroy()])
    upAutos.grid(column=2,row=2,ipadx=5,ipady=5,padx=10,pady=10)

    upMotos=ttk.Button(winV,text="Cargar Motos",command=lambda:[Cargar_Moto(),winV.destroy()])
    upMotos.grid(column=2,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    upCamioneta=ttk.Button(winV,text="Cargar Camioneta",command=lambda:[Cargar_camioneta(),winV.destroy()])
    upCamioneta.grid(column=2,row=4,ipadx=5,ipady=5,padx=10,pady=10,columnspan=2)

    upCamion=ttk.Button(winV,text="Cargar Camion",command=lambda:[Cargar_Camion(),winV.destroy()])
    upCamion.grid(column=2,row=1,ipadx=5,ipady=5,padx=10,pady=10)
    
    upAco=ttk.Button(winV,text="Cargar Acoplado",command=lambda:[Cargar_Acoplado(),winV.destroy()])
    upAco.grid(column=3,row=1,ipadx=5,ipady=5,padx=10,pady=10)

    upCole=ttk.Button(winV,text="Cargar Colectivo",command=lambda:[Cargar_Colectivo(),winV.destroy()])
    upCole.grid(column=3,row=2,ipadx=5,ipady=5,padx=10,pady=10)

    upBici=ttk.Button(winV,text="Cargar Bici",command=lambda:[Cargar_Bici(),winV.destroy()])
    upBici.grid(column=3,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    botonVoler=ttk.Button(winV,text="Volver",command=lambda:[MenuPrincial(),winV.destroy()])
    botonVoler.grid(column=3,row=9,ipadx=5,ipady=5,padx=10,pady=10)

#Auto
def Cargar_Auto():
    #Ventana

    winauto=Toplevel()
    winauto.title("Cargar auto")
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
    botonCargar=ttk.Button (winauto,text="Cargar Auto",command=ingrese_auto)
    botonCargar.grid(column=1,row=14)
    botonVolver=ttk.Button(winauto,text="Volver",command=lambda:[cargarVehiculos(),winauto.destroy()])
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
    botonCargar=ttk.Button (winauto,text="Cargar Moto")
    botonCargar.grid(column=1,row=14)
    botonVolver=ttk.Button(winauto,text="Volver",command=lambda:[cargarVehiculos(),winauto.destroy()])
    botonVolver.grid(column=3,row=14)
#camioneta
def Cargar_camioneta():
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
    botonCargar=ttk.Button (winauto,text="Cargar camioneta")
    botonCargar.grid(column=1,row=14)
    botonVolver=ttk.Button(winauto,text="Volver",command=lambda:[cargarVehiculos(),winauto.destroy()])
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
    botonCargar=ttk.Button (winauto,text="Cargar Colectivo")
    botonCargar.grid(column=1,row=14)
    botonVolver=ttk.Button(winauto,text="Volver",command=lambda:[cargarVehiculos(),winauto.destroy()])
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
    botonCargar=ttk.Button (winauto,text="Cargar Camion")
    botonCargar.grid(column=1,row=14)
    botonVolver=ttk.Button(winauto,text="Volver",command=lambda:[cargarVehiculos(),winauto.destroy()])
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
    botonCargar=ttk.Button (winauto,text="Cargar Acoplado")
    botonCargar.grid(column=1,row=14)
    botonVolver=ttk.Button(winauto,text="Volver",command=lambda:[cargarVehiculos(),winauto.destroy()])
    botonVolver.grid(column=3,row=14)
#Bici
def Cargar_Bici():
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
    botonCargar=ttk.Button (winauto,text="Cargar Bici")
    botonCargar.grid(column=1,row=14)
    botonVolver=ttk.Button(winauto,text="Volver",command=lambda:[cargarVehiculos(),winauto.destroy()])
    botonVolver.grid(column=3,row=14)