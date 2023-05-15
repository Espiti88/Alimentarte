class Categoria:

    def __init__(self, newIdCategoria, newNombre):
        self.idCategoria = newIdCategoria
        self.nombre = newNombre

    def getIdCategoria(self):
        return self.idCategoria

    def getNombre(self):
        return self.nombre

    def setIdCategoria(self, newIdCategoria):
        self.idCategoria = newIdCategoria

    def setNombre(self, newNombre):
        self.nombre = newNombre

    def toString(self):
        print(f"Id Categoria = {self.idCategoria}, Nombre = {self.nombre}")