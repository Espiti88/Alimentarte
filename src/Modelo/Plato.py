class Plato:

    def __init__(self, newIdPlato, newNombre, newPrecio, newMani, newPicante, newRestaurante, newDescripcion):
        self.idPlato = newIdPlato
        self.nombre = newNombre
        self.precio = newPrecio
        self.mani = newMani
        self.picante = newPicante
        self.restaurante = newRestaurante
        self.descripcion = newDescripcion

    def getIdPlato(self):
        return self.idPlato

    def getNombre(self):
        return self.nombre

    def getPrecio(self):
        return self.precio

    def getMani(self):
        return self.mani

    def getPicante(self):
        return self.picante

    def getRestaurante(self):
        return self.restaurante

    def getDescripcion(self):
        return  self.descripcion

    def setIdPlato(self, newIdPlato):
        self.idPlato = newIdPlato

    def setNombre(self, newNombre):
        self.nombre = newNombre

    def setPrecio(self, newPrecio):
        self.precio = newPrecio

    def setMani(self, newMani):
        self.mani = newMani

    def setPicante(self, newPicante):
        self.picante = newPicante

    def setRestaurante(self, newRestaurante):
        self.restaurante = newRestaurante

    def setDescripcion(self, newDescripcion):
        self.descripcion = newDescripcion

    def toString(self):
        print(f"Id Plato = {self.idPlato}, Nombre = {self.nombre}, Precio = {self.precio}, Mani = {self.mani}, "
              f"Picante = {self.picante}, Restaurante = {self.restaurante}, Descripción = {self.descripcion}")
