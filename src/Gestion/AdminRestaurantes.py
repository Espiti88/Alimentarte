from src.Modelo.Restaurante import Restaurante
from src.Conex.Conexion import Conexion

class AdminRestaurantes:

    def __init__(self):
        self.con = Conexion()
        self.miConexion = self.con.conectar()

        print('Objeto tipo AdminRestaurantes creado')
        self.menu()

    def menu(self):
        opcion = -1
        while opcion != 0:

            print('\n===============')
            print(' Restaurantes')
            print('===============')
            print("0. Salir")
            print("1. Nuevo restaurante")
            print("2. Ver todos los restaurantes")
            print("3. Buscar restaurante")
            print("4. Eliminar restaurante")
            print("5. Modificar restaurante")

            opcion = int(input("Opción: "))
            print()

            if opcion == 0:
                self.miConexion = self.con.desconectar()
                print("Fin del menu de Restaurantes")

            elif opcion == 1:
                self.nuevoRestaurante()
            elif opcion == 2:
                self.verTodos()
            elif opcion == 3:
                self.buscarRestaurante()
            elif opcion == 4:
                self.eliminarRestaurante()
            elif opcion == 5:
                self.modificarRestaurantePlato()
            else:
                print('Esa opción no existe!')

    def nuevoRestaurante(self):

        id = int(input("¿Cuál es el ID?: "))

        if self.existeId(id):
            print("Ya existe un restaurante con ese código.")
            return

        nombre = input("¿Cuál es el nombre?")
        categoria = int(input("¿Cuál es la categoria?"))
        if not self.existeCategoria(categoria):
            print("No existe una categoria con ese código.")
            return

        slogan = input("¿Cuál es el slogan?")
        direccion = input("¿Cuál es la dirección?")

        try:
            mycursor = self.miConexion.cursor()

            mycursor.callproc('newRestaurante', [id, nombre, categoria, slogan, direccion])
            self.miConexion.commit()

            print('El restaurante ha sido creado!')
            mycursor.close()

        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError)

    def verTodos(self):

        print("---Lista de Restaurantes---\n")

        cant = 0
        try:
            mycursor = self.miConexion.cursor()
            mycursor.callproc('allRestaurantes')

            for result in mycursor.stored_results():

                for (idRestaurante, nombre, categoria, slogan, direccion) in result:
                    elRestaurante = Restaurante(idRestaurante, nombre, categoria, slogan, direccion)
                    elRestaurante.toString()
                    cant = cant + 1

            if cant == 0:
                print("No hay restaurantes registrados")

            mycursor.close()

        except Exception as miError:
            print('Fallo ejecutando el procedimiento!')
            print(miError)

    def buscarRestaurante(self):

        id = int(input('Digite el ID a buscar: '))
        if not self.existeId(id):
            print("Ese restaurante no existe")
        else:
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('getRestaurante', [id])

                for result in mycursor.stored_results():
                    for (idRestaurante, nombre, categoria, slogan, direccion) in result:
                        elRestaurante = Restaurante(idRestaurante, nombre, categoria, slogan, direccion)
                        elRestaurante.toString()

            except Exception as miError:
                print('Fallo ejecutando el procedimiento')
                print(miError)

    def eliminarRestaurante(self):

        id = int(input('Digite el ID a eliminar: '))
        if not self.existeId(id):
            print("Ese restaurante no existe, no se puede eliminar")

        else:
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('delRestaurante', [id])
                self.miConexion.commit()

                print('El restaurante ha sido eliminado..!!')

            except Exception as miError:
                print('Fallo ejecutando el procedimiento')
                print(miError)

    def modificarRestaurante(self):

        id = int(input("¿Digite el ID a modificar:  "))
        print()

        if not self.existeId(id):
            print("Ese restaurante no existe, no se pude modificar")
        else:
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('getRestaurante', [id])

                for result in mycursor.stored_results():
                    for (idRestaurante, nombre, categoria, slogan, direccion) in result:
                        elRestaurante = Restaurante(idRestaurante, nombre, categoria, slogan, direccion)

                newId = int(input("¿Cuál es el nuevo Id?: "))

                if self.existeId(newId) and newId != elRestaurante.getIdCliente():
                    print("Ese Id ya existe")
                    mycursor.close()
                    return

                newNombre = input("¿Cuál es el nuevo nombre?: ")

                newCategoria = int(input("¿Cuál es la nueva categoria?: "))
                if not self.existeCategoria(newCategoria):
                    print("No existe una categoria con ese código.")
                    return

                newSlogan = input("¿Cuál es el nuevo slogan?: ")
                newDireccion = input("¿Cuál es la nueva dirección?: ")

                mycursor.callproc('modPlato', [newId, newNombre, newCategoria, newSlogan, newDireccion, id])
                self.miConexion.commit()
                print("\nHas modificado el restaurante con éxito.")
                mycursor.close()

            except Exception as miError:
                print('Fallo ejecutando el procedimiento')
                print(miError)

    def existeId(self, id):
        try:
            mycursor = self.miConexion.cursor()
            query = "SELECT count(*) FROM restaurantes WHERE idRestaurante = %s;"
            mycursor.execute(query, [id])
            resultados = mycursor.fetchall()

            for registro in resultados:
                if registro[0] == 1:
                    return True
                return False

        except Exception as miError:
            print('Fallo ejecutando el programa!')
            print(miError)


    def existeCategoria(self, categoria):
        try:
            mycursor = self.miConexion.cursor()
            query = "SELECT count(*) FROM categorias WHERE idCategoria = %s;"
            mycursor.execute(query, [categoria])
            resultados = mycursor.fetchall()

            for registro in resultados:
                if registro[0] == 1:
                    return True
                return False

        except Exception as miError:
            print('Fallo ejecutando el programa!')
            print(miError)
