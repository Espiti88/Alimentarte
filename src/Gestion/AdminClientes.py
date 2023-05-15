from src.Modelo.Cliente import Cliente
from src.Conex.Conexion import Conexion

class AdminClientes:

    def __init__(self):
        self.con = Conexion()
        self.miConexion = self.con.conectar()

        print('Objeto tipo AdminClientes creado')
        self.menu()

    def menu(self):
        opcion = -1
        while opcion != 0:

            print('\n===============')
            print(' Clientes')
            print('===============')
            print("0. Salir")
            print("1. Nuevo cliente")
            print("2. Ver todos los clientes")
            print("3. Buscar cliente")
            print("4. Eliminar cliente")
            print("5. Modificar cliente")

            opcion = int(input("Opción: "))
            print()

            if opcion == 0:
                self.miConexion = self.con.desconectar()
                print("Fin del menu de Clientes")

            elif opcion == 1:
                self.nuevoCliente()
            elif opcion == 2:
                self.verTodos()
            elif opcion == 3:
                self.buscarCliente()
            elif opcion == 4:
                self.eliminarCliente()
            elif opcion == 5:
                self.modificarCliente()
            else:
                print('Esa opción no existe!')

    def nuevoCliente(self):

        id = int(input("¿Cuál es el ID?: "))

        if self.existeId(id):
            print("Ya existe un cliente con ese código.")
            return

        nombre = input("¿Cuál es el nombre?: ")
        telefono = input("¿Cuál es el teléfono?: ")

        correo = input("¿Cuál es el correo?: ")
        if self.existeCorreo(correo):
            print("Ya existe un cliente con ese correo.")
            return

        try:
            mycursor = self.miConexion.cursor()

            mycursor.callproc('newCliente', [id, nombre, telefono, correo])
            self.miConexion.commit()

            print('El cliente ha sido creada!')
            mycursor.close()

        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError)

    def verTodos(self):

        print("---Lista de Clientes---\n")

        cant = 0
        try:
            mycursor = self.miConexion.cursor()
            mycursor.callproc('allClientes')

            for result in mycursor.stored_results():

                for (idCliente, nombre, telefono, correo) in result:
                    elCliente = Cliente(idCliente, nombre, telefono, correo)
                    elCliente.toString()
                    cant = cant + 1

            if cant == 0:
                print("No hay clientes registrados")

            mycursor.close()

        except Exception as miError:
            print('Fallo ejecutando el procedimiento!')
            print(miError)

    def buscarCliente(self):

        id = int(input('Digite el ID a buscar: '))
        if not self.existeId(id):
            print("Ese cliente no existe")
        else:
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('getCliente', [id])

                for result in mycursor.stored_results():
                    for (idCliente, nombre, telefono, correo) in result:
                        elCliente = Cliente(idCliente, nombre, telefono, correo)
                        elCliente.toString()

            except Exception as miError:
                print('Fallo ejecutando el procedimiento')
                print(miError)

    def eliminarCliente(self):

        id = int(input('Digite el ID a eliminar: '))
        if not self.existeId(id):
            print("Ese cliente no existe, no se puede eliminar")

        else:
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('delCliente', [id])
                self.miConexion.commit()

                print('El cliente ha sido eliminado..!!')

            except Exception as miError:
                print('Fallo ejecutando el procedimiento')
                print(miError)

    def modificarCliente(self):

        id = int(input("¿Digite el ID a modificar:  "))
        print()

        if not self.existeId(id):
            print("Ese cliente no existe, no se pude modificar")
        else:
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('getCliente', [id])

                for result in mycursor.stored_results():
                    for (idCliente, nombre, telefono, correo) in result:
                        elCliente = Cliente(idCliente, nombre, telefono, correo)

                newId = int(input("¿Cuál es el nuevo Id?: "))

                if self.existeId(newId) and newId != elCliente.getIdCliente():
                    print("Ese Id ya existe")
                    mycursor.close()
                    return

                newNombre = input("¿Cuál es el nuevo nombre?: ")
                newTelefono = input("¿Cuál es el nuevo teléfono?: ")

                newCorreo = input("¿Cuál es el nuevo correo?: ")
                if self.existeCorreo(newCorreo) and newCorreo != elCliente.getCorreo():
                    print("Ese correo ya existe")
                    mycursor.close()
                    return

                mycursor.callproc('modCliente', [newId, newNombre, newTelefono, newCorreo, id])
                self.miConexion.commit()
                print("\nHas modificado el cliente con éxito.")
                mycursor.close()

            except Exception as miError:
                print('Fallo ejecutando el procedimiento')
                print(miError)

    def existeId(self, id):
        try:
            mycursor = self.miConexion.cursor()
            query = "SELECT count(*) FROM clientes WHERE idCliente = %s;"
            mycursor.execute(query, [id])
            resultados = mycursor.fetchall()

            for registro in resultados:
                if registro[0] == 1:
                    return True
                return False

        except Exception as miError:
            print('Fallo ejecutando el programa!')
            print(miError)


    def existeCorreo(self, correo):
        try:
            mycursor = self.miConexion.cursor()
            query = "SELECT count(*) FROM clientes WHERE correo = %s;"
            mycursor.execute(query, [correo])
            resultados = mycursor.fetchall()

            for registro in resultados:
                if registro[0] == 1:
                    return True
                return False

        except Exception as miError:
            print('Fallo ejecutando el programa!')
            print(miError)
