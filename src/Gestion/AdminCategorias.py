from src.Modelo.Categoria import Categoria
from src.Conex.Conexion import Conexion

class AdminCategorias:

    def __init__(self):
        self.con = Conexion()
        self.miConexion = self.con.conectar()

        print('Objeto tipo AdminCategorias creado')
        self.menu()


    def menu(self):
        opcion = -1
        while opcion != 0:

            print('\n===============')
            print(' Categorias')
            print('===============')
            print("0. Salir")
            print("1. Nueva Categoría")
            print("2. Ver todas las categorías")
            print("3. Buscar categoría")
            print("4. Eliminar categoría")
            print("5. Modificar categoría")

            opcion = int(input("Opción: "))
            print()

            if opcion == 0:
                self.miConexion = self.con.desconectar()
                print("Fin del menu de Categorías")

            elif opcion == 1:
                self.nuevaCategoria()
            elif opcion == 2:
                self.verTodas()
            elif opcion == 3:
                self.buscarCategoria()
            elif opcion == 4:
                self.eliminarCategoria()
            elif opcion == 5:
                self.modificarCategoria()
            else:
                print('Esa opción no existe!')


    def nuevaCategoria(self):

        id = int(input("¿Cuál es el ID?: "))

        if self.existeId(id):
            print("Ya existe una categoría con ese código.")
            return

        nombre = input("¿Cuál es el nombre?: ")

        try:
            mycursor = self.miConexion.cursor()

            mycursor.callproc('newCategoria', [id, nombre])
            self.miConexion.commit()

            print('La categoría ha sido creada!')
            mycursor.close()

        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError)


    def verTodas(self):

        print("---Lista de Categorías---\n")

        cant = 0
        try:
            mycursor = self.miConexion.cursor()
            mycursor.callproc('allCategorias')

            for result in mycursor.stored_results():

                for (idCategoria, nombre) in result:
                    laCategoria = Categoria(idCategoria, nombre)
                    laCategoria.toString()
                    cant = cant + 1

            if cant == 0:
                print("No hay categorías registradas")

            mycursor.close()

        except Exception as miError:
            print('Fallo ejecutando el procedimiento!')
            print(miError)


    def buscarCategoria(self):

        id = int(input('Digite el ID a buscar: '))
        if not self.existeId(id):
            print("Esa categoría no existe")
        else:
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('getCategoria', [id])

                for result in mycursor.stored_results():
                    for (idCategoria, nombre) in result:
                        laCategoria = Categoria(idCategoria, nombre)
                        laCategoria.toString()

            except Exception as miError:
                print('Fallo ejecutando el procedimiento')
                print(miError)


    def eliminarCategoria(self):

        id = int(input('Digite el ID a eliminar: '))
        if not self.existeId(id):
            print("Esa categoría no existe, no se puede eliminar")

        else:
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('delCategoria', [id])
                self.miConexion.commit()

                print('La categoría ha sido eliminada..!!')

            except Exception as miError:
                print('Fallo ejecutando el procedimiento')
                print(miError)


    def modificarCategoria(self):

        id = int(input("¿Digite el ID a modificar:  "))
        print()

        if not self.existeId(id):
            print("Esa categoría no existe")
        else:
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('getCategoria', [id])

                for result in mycursor.stored_results():
                    for (idCategoria, nombre) in result:
                        laCategoria = Categoria(idCategoria, nombre)

                newId = int(input("¿Cuál es el nuevo Id?: "))

                if self.existeId(newId) and newId != laCategoria.getIdCategoria():
                    print("Ese Id ya existe")
                    mycursor.close()
                    return

                newNombre = input("¿Cuál es el nuevo nombre?: ")

                mycursor.callproc('modCategoria', [newId, newNombre, id])
                self.miConexion.commit()
                print("\nHas modificado la categoría con éxito.")
                mycursor.close()

            except Exception as miError:
                print('Fallo ejecutando el procedimiento')
                print(miError)

    def existeId(self, id):
        try:
            mycursor = self.miConexion.cursor()
            query = "SELECT count(*) FROM categorias WHERE idCategoria = %s;"
            mycursor.execute(query, [id])
            resultados = mycursor.fetchall()

            for registro in resultados:
                if registro[0] == 1:
                    return True
                return False

        except Exception as miError:
            print('Fallo ejecutando el programa!')
            print(miError)
