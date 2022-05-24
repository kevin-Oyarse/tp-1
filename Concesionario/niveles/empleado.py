from model.Usuario import*
from constructores.Constructores import ingrese_acoplado,ingrese_bicicleta,ingrese_camion,ingrese_camioneta,ingrese_colectivo,ingrese_moto,ingrese_auto
from data.Auto import*
'''
Puede ver los automóviles a la venta.
Puede ver los precios y kilómetros del mismo.
Puede modificar los kilómetros.
Agregar detalles sobre el vehículo a la venta.
'''
def Empleado():
    print("1-Mostar lista de vehiculos")
    print("2-Modificar km de autos")
    print("3-Agregar detalles sobre el vehiculo")
    print("4-Salir")
    op=input()
    op=op.lower()
    if op=="1" or op=="mostrar lista":
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
        Empleado()
    elif op=="2" or op=="modificar km de autos":
        print ("proximante")
    elif op=="3" or op=="agregar detalles":
        print("proximanete")
    elif op=="4" or op=="salir":
        print("Gracias por visitarnos")
        quit()
    else:
        print("opcion no valida")
        Empleado()
