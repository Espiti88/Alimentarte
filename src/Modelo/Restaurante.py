class Restaurante:

    def __init__(self, newIdRestaurante, newNombre, newCategoria, newSlogan, newDireccion):
        self.idRestaurante = newIdRestaurante
        self.nombre = newNombre
        self.categoria = newCategoria
        self.slogan = newSlogan
        self.direccion = newDireccion

    def getIdRestaurante(self):
        return self.idRestaurante

    def getNombre(self):
        return self.nombre

    def getCategoria(self):
        return self.categoria

    def getSlogan(self):
        return self.slogan

    def getDireccion(self):
        return self.direccion

    def setIdRestaurante(self, newIdRestaurante):
        self.idRestaurante = newIdRestaurante

    def setNombre(self, newNombre):
        self.nombre = newNombre

    def setCategoria(self, newCategoria):
        self.categoria = newCategoria

    def setSlogan(self, newSlogan):
        self.slogan = newSlogan

    def setDireccion(self, newDireccion):
        self.direccion = newDireccion

    def toString(self):
        print(f"Id Restaurante = {self.idRestaurante}, Nombre = {self.nombre}, Categoria = {self.categoria}, "
              f"Slogan = {self.slogan}, Direccion = {self.direccion}")