class Auto():
    def __init__(self):
        pass
    
    def __init__(self, marca, modelo, km, detalles,precio,estado):
        self.marca =marca
        self.modelo =modelo
        self.km=km
        self.precio=precio
        self.detalles=detalles
        self.estado=estado

    def __repr__(self):
        return str(self.__dict__)


class Bicleta():
    def __init__(self,marca,modelo,precios,detalles,estado):
        self.marca=marca
        self.modelo=modelo
        self.precio=precios
        self.detalles=detalles
        self.estado=estado
    def __repr__(self):
        return str(self.__dict__)
    
    def __str__(self) -> str:
        return f'Detalles {self.detalles}'
