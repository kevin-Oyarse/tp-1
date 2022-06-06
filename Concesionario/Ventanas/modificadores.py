from tkinter import ttk as ttk 
from tkinter import *
#from Ventanas.MenuPrincipal import MenuPrincial

#precios
def VentanaPrecio():
    #Ventana
    ventanamod=Toplevel()
    ventanamod.title("Modificar Precios")
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


    botonVolver=ttk.Button(ventanamod,text="Volver",command=lambda:[VentanaPrecio(),ventanamod.destroy()])
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

    botonBici=ttk.Button(ventanamod,text="Bicicleta")
    botonBici.grid(column=3,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    botonCamioneta=ttk.Button(ventanamod,text="Camioneta")
    botonCamioneta.grid(column=3,row=4,ipadx=5,ipady=5,padx=10,pady=10)

    botonCamio=ttk.Button(ventanamod,text="Camion")
    botonCamio.grid(column=4,row=2,ipadx=5,ipady=5,padx=10,pady=10)


    botonVolver=ttk.Button(ventanamod,text="Volver",command=lambda:[VentanaPrecio(),ventanamod.destroy()])
    botonVolver.grid(column=5,row=4,ipadx=5,ipady=5,padx=10,pady=10)
#VentanaDetalles

#VentanaListaDeVehiculos

#VentanaUsuarios