from src.Modelo.Plato import Plato
from src.Conex.Conexion import Conexion

class AdminPlatos:

    def __init__(self):
        self.con = Conexion()
        self.miConexion = self.con.conectar()

        print('Objeto tipo AdminPlatos creado')
        self.menu()

    def menu(self):
        opcion = -1
        while opcion != 0:

            print('\n===============')
            print(' Platos')
            print('===============')
            print("0. Salir")
            print("1. Nuevo plato")
            print("2. Ver todos los platos")
            print("3. Buscar plato")
            print("4. Eliminar plato")
            print("5. Modificar plato")

            opcion = int(input("Opción: "))
            print()

            if opcion == 0:
                self.miConexion = self.con.desconectar()
                print("Fin del menu de Platos")

            elif opcion == 1:
                self.nuevoPlato()
            elif opcion == 2:
                self.verTodos()
            elif opcion == 3:
                self.buscarPlato()
            elif opcion == 4:
                self.eliminarPlato()
            elif opcion == 5:
                self.modificarPlato()
            else:
                print('Esa opción no existe!')

    def nuevoPlato(self):

        id = int(input("¿Cuál es el ID?: "))

        if self.existeId(id):
            print("Ya existe un plato con ese código.")
            return

        nombre = input("¿Cuál es el nombre?: ")
        precio = int(input("¿Cuál es el precio?: "))
        mani = input("¿Tiene mani?: ")
        picante = input("¿Tiene picante?: ")

        restaurante = int(input("¿Cuál es el restaurante?: "))
        if not self.existeRestaurante(restaurante):
            print("No existe un restaurante con ese código.")
            return

        descripcion = input("¿Cuál es la descripcion?: ")
        if self.existeDescripcion(descripcion):
            print("Ya existe esa descripción en otro plato.")
            return

        try:
            mycursor = self.miConexion.cursor()

            mycursor.callproc('newPlato', [id, nombre, precio, mani, picante, restaurante, descripcion])
            self.miConexion.commit()

            print('El plato ha sido creado!')
            mycursor.close()

        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError)

    def verTodos(self):

        print("---Lista de Platos---\n")

        cant = 0
        try:
            mycursor = self.miConexion.cursor()
            mycursor.callproc('allPlatos')

            for result in mycursor.stored_results():

                for (idPlato, nombre, precio, mani, picante, restaurante, descripcion) in result:
                    elPlato = Plato(idPlato, nombre, precio, mani, picante, restaurante, descripcion)
                    elPlato.toString()
                    cant = cant + 1

            if cant == 0:
                print("No hay platos registrados")

            mycursor.close()

        except Exception as miError:
            print('Fallo ejecutando el procedimiento!')
            print(miError)

    def buscarPlato(self):

        id = int(input('Digite el ID a buscar: '))
        if not self.existeId(id):
            print("Ese plato no existe")
        else:
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('getPlato', [id])

                for result in mycursor.stored_results():
                    for (idPlato, nombre, precio, mani, picante, restaurante, descripcion) in result:
                        elPlato = Plato(idPlato, nombre, precio, mani, picante, restaurante, descripcion)
                        elPlato.toString()

            except Exception as miError:
                print('Fallo ejecutando el procedimiento')
                print(miError)

    def eliminarPlato(self):

        id = int(input('Digite el ID a eliminar: '))
        if not self.existeId(id):
            print("Ese plato no existe, no se puede eliminar")

        else:
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('delPlato', [id])
                self.miConexion.commit()

                print('El plato ha sido eliminado..!!')

            except Exception as miError:
                print('Fallo ejecutando el procedimiento')
                print(miError)

    def modificarPlato(self):

        id = int(input("¿Digite el ID a modificar:  "))
        print()

        if not self.existeId(id):
            print("Ese plato no existe, no se pude modificar")
        else:
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('getPlato', [id])

                for result in mycursor.stored_results():
                    for (idPlato, nombre, precio, mani, picante, restaurante, descripcion) in result:
                        elPlato = Plato(idPlato, nombre, precio, mani, picante, restaurante, descripcion)

                newId = int(input("¿Cuál es el nuevo Id?: "))

                if self.existeId(newId) and newId != elPlato.getIdCliente():
                    print("Ese Id ya existe")
                    mycursor.close()
                    return

                newNombre = input("¿Cuál es el nuevo nombre?: ")
                newPrecio = int(input("¿Cuál es el nuevo precio?: "))
                newMani = input("¿Tiene maní?: ")
                newPicante = input("¿Tiene picante?: ")

                newRestaurante = int(input("¿Cuál es el restaurante?: "))
                if not self.existeRestaurante(newRestaurante):
                    print("No existe un restaurante con ese código.")
                    return

                newDescripcion = input("¿Cuál es la descripcion?")
                if self.existeDescripcion(newDescripcion) and newDescripcion != elPlato.getDescripcion():
                    print("Ya existe esa descripción en otro plato.")
                    return

                mycursor.callproc('modPlato', [newId, newNombre, newPrecio, newMani, newPicante, newRestaurante, newDescripcion, id])
                self.miConexion.commit()
                print("\nHas modificado el plato con éxito.")
                mycursor.close()

            except Exception as miError:
                print('Fallo ejecutando el procedimiento')
                print(miError)

    def existeId(self, id):
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


    def existeRestaurante(self, restaurante):
        try:
            mycursor = self.miConexion.cursor()
            query = "SELECT count(*) FROM restaurantes WHERE idRestaurante = %s;"
            mycursor.execute(query, [restaurante])
            resultados = mycursor.fetchall()

            for registro in resultados:
                if registro[0] == 1:
                    return True
                return False

        except Exception as miError:
            print('Fallo ejecutando el programa!')
            print(miError)

    def existeDescripcion(self, descripcion):
        try:
            mycursor = self.miConexion.cursor()
            query = "SELECT count(*) FROM platos WHERE descripcion = %s;"
            mycursor.execute(query, [descripcion])
            resultados = mycursor.fetchall()

            for registro in resultados:
                if registro[0] == 1:
                    return True
                return False

        except Exception as miError:
            print('Fallo ejecutando el programa!')
            print(miError)
