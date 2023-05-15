class Pedido:

    def __init__(self, newIdCliente, newIdPlato, newFecha_hora):
        self.idCliente = newIdCliente
        self.idPlato = newIdPlato
        self.fecha_hora = newFecha_hora

    def getIdCliente(self):
        return self.idCliente

    def getIdPlato(self):
        return self.idPlato

    def getFecha_hora(self):
        return self.fecha_hora

    def setIdCliente(self, newIdCliente):
        self.idCliente = newIdCliente

    def setIdPlato(self, newIdPlato):
        self.idPlato = newIdPlato

    def setFecha_hora(self, newFecha_hora):
        self.fecha_hora = newFecha_hora

    def toString(self):
        print(f"Id Cliente = {self.idCliente}, Id Plato = {self.idPlato}, Fecha y Hora = {self.fecha_hora}")
