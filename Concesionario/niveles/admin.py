from data.Usuarios import agregaUsuarios
from model.Usuario import*
from constructores.Constructores import *
from data.Auto import *
from constructores.modificardor import*
from ui.Views import *
from controller.UsuariosControllers import*

def Admin():
    print("1-Cargar Autos")
    print("2-Modificar precios del auto")
    print("3-Modificar km de autos")
    print("4-Crear usuarios")
    print("5-Agregar detalles sobre el vehiculo")
    print("6-Mostrar lista de vehiculos")
    print("7-Salir")
    op=input()
    op=op.lower()
    if op=="1" or op=="cargar autos":
        datos=input("Que desea cargar Auto,Moto,Colectivo,Bicicleta,Acoplado,Camiones.\n")
        if datos=="auto":
            ingrese_auto()
        elif datos=="moto":
            ingrese_moto()
        elif datos=="acoplado":
            ingrese_acoplado()
        elif datos=="bicicleta" or datos=="bici":
            ingrese_bicicleta()
        elif datos=="camioneta":
            ingrese_camioneta()
        elif datos=="Colectivos":
            agregarcolectivo()
        elif datos=="camiones" or datos=="camion":
            ingrese_camion()
        elif datos =="colectivo":
            ingrese_colectivo()
    elif op=="2" or op=="modificar precios":
        vehiculo=input("elija el tipo de vehiculo para agregar el detalle: ")
        if vehiculo=="auto":
            modificarprecio_auto()
        elif vehiculo=="moto":
            modificarprecio_moto()
        elif vehiculo=="acoplado":
            modificarprecio_acoplado()
        elif vehiculo=="camioneta":
            modificarprecio_camioneta()
        elif vehiculo=="colectivo":
            modificarprecio_colectivo()
        elif vehiculo=="camion":
            modificarprecio_camion()
        Admin()
    elif op=="3" or op=="moficar km":
        vehiculo=input("elija el tipo de vehiculo para agregar el detalle: ")
        if vehiculo=="auto":
            modificarkm_auto()
        elif vehiculo=="moto":
            modificarkm_moto()
        elif vehiculo=="acoplado":
            modificarkm_Acoplado()
        elif vehiculo=="camioneta":
            modificarkm_camioneta()
        elif vehiculo=="colectivo":
            modificarkm_cole()
        elif vehiculo=="camion":
            modificarkm_camion()
        Admin()
    elif op=="4" or op=="crear usuarios":
            user1=Usuario(input("Ingrese un nombre: "),input("Ingrese un correo: "),input("Ingrese una contraseña: "),input("Ingrese el nivel del usuario: "))
            agregaUsuarios(user1)
            printUsuarios()
            Admin()
    elif op=="5" or op=="agregar detalle":
        vehiculo=input("elija el tipo de vehiculo para agregar el detalle: ")
        if vehiculo=="auto":
            modificarDetalle_auto()
        elif vehiculo=="moto":
            modificarDetalle_moto()
        elif vehiculo=="acoplado":
            modificardetalle_Acoplado()
        elif vehiculo=="camioneta":
            modificardetalles_camioneta()
        elif vehiculo=="bici":
            modificardetalle_bici()
        elif vehiculo=="colectivo":
            modificardetalle_cole()
        elif vehiculo=="camion":
            modificardetalles_camion()
        Admin()
    elif op=="6" or op=="mostrar lista":
        print("Autos:")
        printAutos()
        print ("motos:")
        printMoto()
        print("Bicicletas:")
        printbici()
        print("Camiones:")
        printCamion()
        print ("Colectivos:")
        printcolectivo()
        print ("Acoplado:")
        printAcoplado()
        print("Camionetas:")
        printcamioneta()
    elif op=="7" or op=="salir":
        print("Gracias por visitarnos")
        quit()
    else:
        print("opcion no valida")
        Admin()
