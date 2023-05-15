from src.Conex.Conexion import Conexion
from datetime import datetime

class Consultas:

    def __init__(self):
        self.con = Conexion()
        self.miConexion = self.con.conectar()

        print('Objeto tipo Consultas creado')
        self.listadoClientes()

    def listadoClientes(self):
        try:
            mycursor = self.miConexion.cursor()
            mycursor.execute("SELECT nombre, telefono, correo FROM clientes ORDER BY nombre;")
            resultados = mycursor.fetchall()

            print('\n 1. NOMBRE - TELEFONO - CORREO')
            for registro in resultados:
                print()
                for dato in registro:
                    print(f'-- {dato} -- ', end="")

            input('\nEnter para la siguiente consulta')
            self.listadoArroz()

        except Exception as miError:
            print('Fallo ejecutando el programa!')
            print(miError)

    def listadoArroz(self):
        try:
            mycursor = self.miConexion.cursor()
            mycursor.execute("SELECT platos.nombre, platos.descripcion, restaurantes.nombre "
            "FROM (platos INNER JOIN restaurantes "
            "ON restaurantes.idRestaurante = platos.restaurante) "
            "WHERE platos.descripcion LIKE '%Arroz%' "
            "ORDER BY platos.nombre;")
            resultados = mycursor.fetchall()

            print('\n2. PLATO - DESCRIPCIÓN - RESTAURANTE')
            for registro in resultados:
                print()
                for dato in registro:
                    print(f'-- {dato} -- ', end="")

            input('\nEnter para la siguiente consulta')
            self.menuFeria()

        except Exception as miError:
            print('Fallo ejecutando el programa!')
            print(miError)

    def menuFeria(self):
        try:
            mycursor = self.miConexion.cursor()
            mycursor.execute("SELECT platos.nombre, platos.descripcion, restaurantes.nombre, platos.precio "
                            "FROM (platos INNER JOIN restaurantes "
                            "ON restaurantes.idRestaurante = platos.restaurante) "
                            "ORDER BY platos.nombre;")
            resultados = mycursor.fetchall()

            print('\n3. PLATO - DESCRIPCIÓN - RESTAURANTE - PRECIO')
            for registro in resultados:
                print()
                for dato in registro:
                    print(f'-- {dato} -- ', end="")

            input('\nEnter para la siguiente consulta')
            self.listadoRestaurantes()

        except Exception as miError:
            print('Fallo ejecutando el programa!')
            print(miError)

    def listadoRestaurantes(self):
        try:
            mycursor = self.miConexion.cursor()
            mycursor.execute("SELECT categorias.nombre, restaurantes.nombre "
                            "FROM (categorias INNER JOIN restaurantes "
                            "ON categorias.idCategoria = restaurantes.categoria) "
                            "ORDER BY categorias.nombre;")
            resultados = mycursor.fetchall()

            print('\n4. CATEGORIA - RESTAURANTE')
            for registro in resultados:
                print()
                for dato in registro:
                    print(f'-- {dato} -- ', end="")

            input('\nEnter para la siguiente consulta')
            self.listadoCompras()

        except Exception as miError:
            print('Fallo ejecutando el programa!')
            print(miError)

    def listadoCompras(self):
        try:
            mycursor = self.miConexion.cursor()
            mycursor.execute("SELECT pedidos.fecha_hora, clientes.nombre, platos.nombre, platos.precio "
                            "FROM (pedidos INNER JOIN clientes "
                            "ON pedidos.idCliente = clientes.idCliente) INNER JOIN platos "
                            "ON pedidos.idPlato = platos.idPlato "
                            "ORDER BY pedidos.fecha_hora;")
            resultados = mycursor.fetchall()

            print('\n5. FECHA - CLIENTE - PLATO - PRECIO')
            for registro in resultados:
                print()
                for dato in registro:
                    print(f'-- {dato} -- ', end="")

            input('\nEnter para salir')

        except Exception as miError:
            print('Fallo ejecutando el programa!')
            print(miError)