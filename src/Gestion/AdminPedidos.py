from src.Modelo.Pedido import Pedido
from datetime import datetime
from src.Conex.Conexion import Conexion


class AdminPedidos:

    def __init__(self):
        self.con = Conexion()
        self.miConexion = self.con.conectar()

        print('Objeto tipo AdminPedidos creado')
        self.menu()

    def menu(self):
        opcion = -1
        while opcion != 0:

            print('\n===============')
            print(' Pedidos')
            print('===============')
            print("0. Salir")
            print("1. Nuevo pedido")
            print("2. Ver todos los pedidos")
            print("3. Buscar pedido")
            print("4. Eliminar pedido")
            print("5. Modificar pedido")

            opcion = int(input("Opción: "))
            print()

            if opcion == 0:
                self.miConexion = self.con.desconectar()
                print("Fin del menu de Pedido")

            elif opcion == 1:
                self.nuevoPedido()
            elif opcion == 2:
                self.verTodos()
            elif opcion == 3:
                self.buscarPedido()
            elif opcion == 4:
                self.eliminarPedido()
            elif opcion == 5:
                self.modificarPedido()
            else:
                print('Esa opción no existe!')

    def nuevoPedido(self):

        idCliente = int(input("¿Cuál es el ID del cliente?: "))
        if not self.existeIdCliente(idCliente):
            print("No existe un cliente con ese código.")
            return

        idPlato = int(input("¿Cuál es el ID del plato?: "))
        if not self.existeIdPlato(idPlato):
            print("No existe un plato con ese código.")
            return

        year = int(input("¿Cuál es el año?: "))
        month = int(input("¿Cuál es el mes?: "))
        day = int(input("¿Cuál es el día?: "))
        hour = int(input("¿Cuál es la hora? (número del 0 - 24): "))
        minute = int(input("¿Cuál es el minuto?: "))
        second = int(input("¿Cuál es el segundo?: "))

        fecha_hora = datetime(year, month, day, hour, minute, second)
        if self.existeCodigo(idCliente, idPlato, fecha_hora):
            print("Ya existe un pedido con ese código.")
            return

        try:
            mycursor = self.miConexion.cursor()

            mycursor.callproc('newPedido', [idCliente, idPlato, fecha_hora])
            self.miConexion.commit()

            print('El pedido ha sido creado!')
            mycursor.close()

        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError)

    def verTodos(self):

        print("---Lista de Pedidos---\n")

        cant = 0
        try:
            mycursor = self.miConexion.cursor()
            mycursor.callproc('allPedidos')

            for result in mycursor.stored_results():

                for (idCliente, idPlato, fecha_hora) in result:
                    elPedido = Pedido(idCliente, idPlato, fecha_hora)
                    elPedido.toString()
                    cant = cant + 1

            if cant == 0:
                print("No hay pedidos registrados")

            mycursor.close()

        except Exception as miError:
            print('Fallo ejecutando el procedimiento!')
            print(miError)

    def buscarPedido(self):

        idCliente = int(input("¿Cuál es el ID del cliente a buscar?: "))
        idPlato = int(input("¿Cuál es el ID del plato a buscar?: "))

        year = int(input("¿Cuál es el año?: "))
        month = int(input("¿Cuál es el mes?: "))
        day = int(input("¿Cuál es el día?: "))
        hour = int(input("¿Cuál es la hora? (número del 0 - 24): "))
        minute = int(input("¿Cuál es el minuto?: "))
        second = int(input("¿Cuál es el segundo?: "))

        fecha_hora = datetime(year, month, day, hour, minute, second)
        if not self.existeCodigo(idCliente, idPlato, fecha_hora):
            print("Ese cliente no existe")

        else:
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('getPedido', [idCliente, idPlato, fecha_hora])

                for result in mycursor.stored_results():
                    for (idCliente, idPlato, fecha_hora) in result:
                        elPedido = Pedido(idCliente, idPlato, fecha_hora)
                        elPedido.toString()

            except Exception as miError:
                print('Fallo ejecutando el procedimiento')
                print(miError)

    def eliminarPedido(self):

        idCliente = int(input("¿Cuál es el ID del cliente a eliminar?: "))
        idPlato = int(input("¿Cuál es el ID del plato a eliminar?: "))

        year = int(input("¿Cuál es el año?: "))
        month = int(input("¿Cuál es el mes?: "))
        day = int(input("¿Cuál es el día?: "))
        hour = int(input("¿Cuál es la hora? (número del 0 - 24): "))
        minute = int(input("¿Cuál es el minuto?: "))
        second = int(input("¿Cuál es el segundo?: "))

        fecha_hora = datetime(year, month, day, hour, minute, second)
        if not self.existeCodigo(idCliente, idPlato, fecha_hora):
            print("Ese cliente no existe, no se puede eliminar")

        else:
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('delPedido', [idCliente, idPlato, fecha_hora])
                self.miConexion.commit()

                print('El pedido ha sido eliminado..!!')

            except Exception as miError:
                print('Fallo ejecutando el procedimiento')
                print(miError)

    def modificarPedido(self):

        idCliente = int(input("¿Cuál es el ID del cliente a modificar?: "))
        idPlato = int(input("¿Cuál es el ID del plato a modificar?: "))

        year = int(input("¿Cuál es el año?: "))
        month = int(input("¿Cuál es el mes?: "))
        day = int(input("¿Cuál es el día?: "))
        hour = int(input("¿Cuál es la hora? (número del 0 - 24): "))
        minute = int(input("¿Cuál es el minuto?: "))
        second = int(input("¿Cuál es el segundo?: "))

        fecha_hora = datetime(year, month, day, hour, minute, second)
        if not self.existeCodigo(idCliente, idPlato, fecha_hora):
            print("Ese pedido no existe, no se puede modificar")
        else:
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('getPedido', [idCliente, idPlato, fecha_hora])

                for result in mycursor.stored_results():
                    for (idCliente, idPlato, fecha_hora) in result:
                        elPedido = Pedido(idCliente, idPlato, fecha_hora)

                newIdCliente = int(input("¿Cuál es el nuevo Id del cliente?: "))
                if not self.existeIdCliente(newIdCliente):
                    print("Ese cliente no existe")
                    mycursor.close()
                    return

                newIdPlato = int(input("¿Cuál es el nuevo Id del plato?: "))
                if not self.existeIdPlato(newIdPlato):
                    print("Ese plato no existe")
                    mycursor.close()
                    return

                newYear = int(input("¿Cuál es el nuevo año?: "))
                newMonth = int(input("¿Cuál es el nuevo mes?: "))
                newDay = int(input("¿Cuál es el nuevo día?: "))
                newHour = int(input("¿Cuál es la nueva hora? (número del 0 - 24): "))
                newMinute = int(input("¿Cuál es el nuevo minuto?: "))
                newSecond = int(input("¿Cuál es el segundo?: "))

                newFecha_hora = datetime(newYear, newMonth, newDay, newHour, newMinute, newSecond)
                if self.existeCodigo(newIdCliente, newIdPlato, newFecha_hora) and (newIdCliente != elPedido.idCliente or newIdPlato != elPedido.idPlato or newFecha_hora != fecha_hora):
                    print("Ese código ya existe")
                    mycursor.close()
                    return

                mycursor.callproc('modPedido', [newIdCliente, newIdPlato, newFecha_hora, idCliente, idPlato, fecha_hora])
                self.miConexion.commit()
                print("\nHas modificado el pedido con éxito.")
                mycursor.close()

            except Exception as miError:
                print('Fallo ejecutando el procedimiento')
                print(miError)

    def existeIdCliente(self, id):
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

    def existeIdPlato(self, id):
        try:
            mycursor = self.miConexion.cursor()
            query = "SELECT count(*) FROM platos WHERE idPlato = %s;"
            mycursor.execute(query, [id])
            resultados = mycursor.fetchall()

            for registro in resultados:
                if registro[0] == 1:
                    return True
                return False

        except Exception as miError:
            print('Fallo ejecutando el programa!')
            print(miError)

    def existeCodigo(self, idCliente, idPlato, fecha_hora):
        try:
            mycursor = self.miConexion.cursor()
            query = "SELECT count(*) FROM pedidos WHERE idCliente = %s AND idPlato = %s AND fecha_hora = %s;"
            mycursor.execute(query, [idCliente, idPlato, fecha_hora])
            resultados = mycursor.fetchall()

            for registro in resultados:
                if registro[0] == 1:
                    return True
                return False

        except Exception as miError:
            print('Fallo ejecutando el programa!')
            print(miError)
