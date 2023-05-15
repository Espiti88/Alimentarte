class Cliente:

    def __init__(self, newIdCliente, newNombre, newTelefono, newCorreo):
        self.idCliente = newIdCliente
        self.nombre = newNombre
        self.telefono = newTelefono
        self.correo = newCorreo

    def getIdCliente(self):
        return self.idCliente

    def getNombre(self):
        return self.nombre

    def getTelefono(self):
        return self.telefono

    def getCorreo(self):
        return self.correo

    def setIdCliente(self, newIdCliente):
        self.idCliente = newIdCliente

    def setNombre(self, newNombre):
        self.nombre = newNombre

    def setTelefono(self, newTelefono):
        self.telefono = newTelefono

    def setCorreo(self, newCorreo):
        self.correo = newCorreo

    def toString(self):
        print(f"Id Cliente = {self.idCliente}, Nombre = {self.nombre}, Telefono = {self.telefono}, Correo = {self.correo}")