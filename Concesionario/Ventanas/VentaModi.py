from model.Auto import *
from tkinter import ttk as ttk 
from tkinter import *
from model.Auto import *
from data.Auto import *

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
    precioLabel=Label(precioauto,text=printAutos)
    precioLabel.grid(column=4,row=4)
    precioEntry=Entry(precioauto,textvariable=precioVar)
    precioEntry.grid(column=1,row=4,columnspan=2)
    #Botones
    botonCargar=ttk.Button (precioauto,text="Cambiar precio")
    botonCargar.grid(column=1,row=14)
    botonVolver=ttk.Button(precioauto,text="cerrar ventana",command=precioauto.destroy)
    botonVolver.grid(column=3,row=14)
#Moto

#Colectivo

#Camion

#Camioneta

#Bici

#Acoplado