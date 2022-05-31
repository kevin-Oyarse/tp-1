class Usuario():
    def __init__(self):
        pass

    def __init__(self, nombre, contra, email, nvl):
        self.nombre = nombre
        self.email = email
        self.contra = contra
        self.nvl = nvl

    
    def __repr__(self):
        return str(self.__dict__)



