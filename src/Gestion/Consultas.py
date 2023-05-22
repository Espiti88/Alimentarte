from PyQt6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem

from src.Conex.Conexion import Conexion
from src.GUIS.DConsultas import Ui_MainWindow


class Consultas(QMainWindow):

    def __init__(self):
        super(Consultas, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.con = Conexion()
        self.miConexion = self.con.conectar()
        print('Objeto tipo Consultas creado y listo para usarse..!!')

        self.ui.BListadoClientes.clicked.connect(self.listadoClientes)
        self.ui.BMenu.clicked.connect(self.menuFeria)
        self.ui.BRestaurantes.clicked.connect(self.listadoRestaurantes)
        self.ui.BBusquedPlato.clicked.connect(self.busqueda)
        self.ui.BPlatosPrecio.clicked.connect(self.platosPrecio)
        self.ui.BListadoCompras.clicked.connect(self.listadoCompras)
        self.ui.BTerminar.clicked.connect(self.cerrarConexion)

    def cerrarConexion(self):
        self.con.desconectar()
        self.close()

    def listadoClientes(self):
        cant = 0
        try:
            mycursor = self.miConexion.cursor()
            mycursor.execute("SELECT nombre, telefono, correo FROM clientes ORDER BY nombre;")
            resultados = mycursor.fetchall()

            total = self.ui.TWTabla.rowCount()
            for rep in range(total):
                self.ui.TWTabla.removeRow(0)

            self.ui.TWTabla.setHorizontalHeaderItem(0, QTableWidgetItem("Nombre"))
            self.ui.TWTabla.setHorizontalHeaderItem(1, QTableWidgetItem("Teléfono"))
            self.ui.TWTabla.setHorizontalHeaderItem(2, QTableWidgetItem("Correo"))
            self.ui.TWTabla.setHorizontalHeaderItem(3, QTableWidgetItem(""))
            self.ui.TWTabla.setHorizontalHeaderItem(4, QTableWidgetItem(""))

            for registro in resultados:

                self.ui.TWTabla.insertRow(cant)

                celdaNombre = QTableWidgetItem(registro[0])
                celdaTelefono = QTableWidgetItem(registro[1])
                celdaCorreo = QTableWidgetItem(registro[2])

                self.ui.TWTabla.setItem(cant, 0, celdaNombre)
                self.ui.TWTabla.setItem(cant, 1, celdaTelefono)
                self.ui.TWTabla.setItem(cant, 2, celdaCorreo)

                cant += 1

            if cant == 0:
                QMessageBox.information(self, "Listado", "No hay ningún cliente..!!")

            mycursor.close()
        except Exception as miError:
            QMessageBox.warning(self, "Error", 'Fallo ejecutando el procedimiento')
            print(miError)

    def menuFeria(self):
        cant = 0
        try:
            mycursor = self.miConexion.cursor()
            mycursor.execute("SELECT platos.nombre, platos.descripcion, restaurantes.nombre, platos.precio "
                             "FROM (platos INNER JOIN restaurantes "
                             "ON restaurantes.idRestaurante = platos.restaurante) "
                             "ORDER BY platos.nombre;")

            resultados = mycursor.fetchall()

            total = self.ui.TWTabla.rowCount()
            for rep in range(total):
                self.ui.TWTabla.removeRow(0)

            self.ui.TWTabla.setHorizontalHeaderItem(0, QTableWidgetItem("Plato"))
            self.ui.TWTabla.setHorizontalHeaderItem(1, QTableWidgetItem("Descripción"))
            self.ui.TWTabla.setHorizontalHeaderItem(2, QTableWidgetItem("Restaurante"))
            self.ui.TWTabla.setHorizontalHeaderItem(3, QTableWidgetItem("Precio"))
            self.ui.TWTabla.setHorizontalHeaderItem(4, QTableWidgetItem(""))

            for registro in resultados:
                self.ui.TWTabla.insertRow(cant)

                celdaPlato = QTableWidgetItem(registro[0])
                celdaDescripcion = QTableWidgetItem(registro[1])
                celdaRestaurante = QTableWidgetItem(registro[2])
                celdaPrecio = QTableWidgetItem(str(registro[3]))

                self.ui.TWTabla.setItem(cant, 0, celdaPlato)
                self.ui.TWTabla.setItem(cant, 1, celdaDescripcion)
                self.ui.TWTabla.setItem(cant, 2, celdaRestaurante)
                self.ui.TWTabla.setItem(cant, 3, celdaPrecio)

                cant += 1

            if cant == 0:
                QMessageBox.information(self, "Listado", "No hay menú..!!")

            mycursor.close()
        except Exception as miError:
            QMessageBox.warning(self, "Error", 'Fallo ejecutando el procedimiento')
            print(miError)

    def listadoRestaurantes(self):
        cant = 0
        try:
            if self.ui.CBRestaurantes.currentIndex() == 0:

                mycursor = self.miConexion.cursor()
                mycursor.execute("SELECT categorias.nombre, restaurantes.nombre "
                                 "FROM (categorias INNER JOIN restaurantes "
                                 "ON categorias.idCategoria = restaurantes.categoria) "
                                 "ORDER BY categorias.nombre;")

                resultados = mycursor.fetchall()

                total = self.ui.TWTabla.rowCount()
                for rep in range(total):
                    self.ui.TWTabla.removeRow(0)

                self.ui.TWTabla.setHorizontalHeaderItem(0, QTableWidgetItem("Categoría"))
                self.ui.TWTabla.setHorizontalHeaderItem(1, QTableWidgetItem("Restaurante"))
                self.ui.TWTabla.setHorizontalHeaderItem(2, QTableWidgetItem(""))
                self.ui.TWTabla.setHorizontalHeaderItem(3, QTableWidgetItem(""))
                self.ui.TWTabla.setHorizontalHeaderItem(4, QTableWidgetItem(""))

                for registro in resultados:
                    self.ui.TWTabla.insertRow(cant)

                    celdaCategoria = QTableWidgetItem(registro[0])
                    celdaRestaurante = QTableWidgetItem(registro[1])

                    self.ui.TWTabla.setItem(cant, 0, celdaCategoria)
                    self.ui.TWTabla.setItem(cant, 1, celdaRestaurante)

                    cant += 1

                if cant == 0:
                    QMessageBox.information(self, "Listado", "No hay ningún restaurante..!!")

                mycursor.close()

            if self.ui.CBRestaurantes.currentIndex() == 1:

                mycursor = self.miConexion.cursor()
                mycursor.execute("SELECT restaurantes.nombre, categorias.nombre "
                                 "FROM (restaurantes INNER JOIN categorias "
                                 "ON restaurantes.categoria = categorias.idCategoria) "
                                 "ORDER BY restaurantes.nombre;")

                resultados = mycursor.fetchall()

                total = self.ui.TWTabla.rowCount()
                for rep in range(total):
                    self.ui.TWTabla.removeRow(0)

                self.ui.TWTabla.setHorizontalHeaderItem(0, QTableWidgetItem("Restaurantes"))
                self.ui.TWTabla.setHorizontalHeaderItem(1, QTableWidgetItem("Categoría"))
                self.ui.TWTabla.setHorizontalHeaderItem(2, QTableWidgetItem(""))
                self.ui.TWTabla.setHorizontalHeaderItem(3, QTableWidgetItem(""))
                self.ui.TWTabla.setHorizontalHeaderItem(4, QTableWidgetItem(""))

                for registro in resultados:
                    self.ui.TWTabla.insertRow(cant)

                    celdaRestaurante = QTableWidgetItem(registro[0])
                    celdaCategoria = QTableWidgetItem(registro[1])

                    self.ui.TWTabla.setItem(cant, 0, celdaRestaurante)
                    self.ui.TWTabla.setItem(cant, 1, celdaCategoria)

                    cant += 1

                if cant == 0:
                    QMessageBox.information(self, "Listado", "No hay ningún restaurante..!!")

                mycursor.close()

        except Exception as miError:
            QMessageBox.warning(self, "Error", 'Fallo ejecutando el procedimiento')
            print(miError)

    def busqueda(self):
        cant = 0

        try:
            mycursor = self.miConexion.cursor()
            print(self.ui.LEFiltroPlato.text())
            mycursor.execute("SELECT platos.nombre, platos.descripcion, restaurantes.nombre, platos.precio "
                            "FROM (platos INNER JOIN restaurantes "
                            "ON restaurantes.idRestaurante = platos.restaurante) "
                            "WHERE platos.descripcion LIKE %s OR platos.nombre LIKE %s"
                            , ["%" + self.ui.LEFiltroPlato.text() + "%", "%" + self.ui.LEFiltroPlato.text() + "%"])
            resultados = mycursor.fetchall()

            total = self.ui.TWTabla.rowCount()
            for rep in range(total):
                self.ui.TWTabla.removeRow(0)

            self.ui.TWTabla.setHorizontalHeaderItem(0, QTableWidgetItem("Plato"))
            self.ui.TWTabla.setHorizontalHeaderItem(1, QTableWidgetItem("Descripción"))
            self.ui.TWTabla.setHorizontalHeaderItem(2, QTableWidgetItem("Restaurante"))
            self.ui.TWTabla.setHorizontalHeaderItem(3, QTableWidgetItem("Precio"))
            self.ui.TWTabla.setHorizontalHeaderItem(4, QTableWidgetItem(""))

            for registro in resultados:
                self.ui.TWTabla.insertRow(cant)

                celdaPlato = QTableWidgetItem(registro[0])
                celdaDescripcion = QTableWidgetItem(registro[1])
                celdaRestaurante = QTableWidgetItem(registro[2])
                celdaPrecio = QTableWidgetItem(str(registro[3]))

                self.ui.TWTabla.setItem(cant, 0, celdaPlato)
                self.ui.TWTabla.setItem(cant, 1, celdaDescripcion)
                self.ui.TWTabla.setItem(cant, 2, celdaRestaurante)
                self.ui.TWTabla.setItem(cant, 3, celdaPrecio)

                cant += 1

            if cant == 0:
                QMessageBox.information(self, "Listado", "No hay ningún cliente..!!")

            mycursor.close()
        except Exception as miError:
            QMessageBox.warning(self, "Error", 'Fallo ejecutando el procedimiento')
            print(miError)

    def platosPrecio(self):
        cant = 0
        try:
            mycursor = self.miConexion.cursor()
            mycursor.execute("SELECT platos.precio, platos.nombre, platos.descripcion, restaurantes.nombre, restaurantes.direccion "
                             "FROM (platos INNER JOIN restaurantes "
                             "ON restaurantes.idRestaurante = platos.restaurante) "
                             "ORDER BY platos.precio;")

            resultados = mycursor.fetchall()

            total = self.ui.TWTabla.rowCount()
            for rep in range(total):
                self.ui.TWTabla.removeRow(0)

            self.ui.TWTabla.setHorizontalHeaderItem(0, QTableWidgetItem("Precio"))
            self.ui.TWTabla.setHorizontalHeaderItem(1, QTableWidgetItem("Plato"))
            self.ui.TWTabla.setHorizontalHeaderItem(2, QTableWidgetItem("Descripción"))
            self.ui.TWTabla.setHorizontalHeaderItem(3, QTableWidgetItem("Restaurante"))
            self.ui.TWTabla.setHorizontalHeaderItem(4, QTableWidgetItem("Direccion"))

            for registro in resultados:
                self.ui.TWTabla.insertRow(cant)

                celdaPrecio = QTableWidgetItem(str(registro[0]))
                celdaPlato = QTableWidgetItem(registro[1])
                celdaDescripcion = QTableWidgetItem(registro[2])
                celdaRestaurante = QTableWidgetItem(registro[3])
                celdaDireccion = QTableWidgetItem(registro[4])

                self.ui.TWTabla.setItem(cant, 0, celdaPrecio)
                self.ui.TWTabla.setItem(cant, 1, celdaPlato)
                self.ui.TWTabla.setItem(cant, 2, celdaDescripcion)
                self.ui.TWTabla.setItem(cant, 3, celdaRestaurante)
                self.ui.TWTabla.setItem(cant, 4, celdaDireccion)

                cant += 1

            if cant == 0:
                QMessageBox.information(self, "Listado", "No hay menú..!!")

            mycursor.close()
        except Exception as miError:
            QMessageBox.warning(self, "Error", 'Fallo ejecutando el procedimiento')
            print(miError)

    def listadoCompras(self):
        cant = 0
        try:
            mycursor = self.miConexion.cursor()
            mycursor.execute("SELECT pedidos.fecha_hora, clientes.nombre, platos.nombre, platos.precio "
                             "FROM (pedidos INNER JOIN clientes "
                             "ON pedidos.idCliente = clientes.idCliente) INNER JOIN platos "
                             "ON pedidos.idPlato = platos.idPlato "
                             "WHERE clientes.idCliente = %s "
                             "ORDER BY pedidos.fecha_hora;"
                             , [str(self.ui.SBIdListadoCompras.value())])

            resultados = mycursor.fetchall()

            total = self.ui.TWTabla.rowCount()
            for rep in range(total):
                self.ui.TWTabla.removeRow(0)

            self.ui.TWTabla.setHorizontalHeaderItem(0, QTableWidgetItem("Fecha / Hora"))
            self.ui.TWTabla.setHorizontalHeaderItem(1, QTableWidgetItem("Cliente"))
            self.ui.TWTabla.setHorizontalHeaderItem(2, QTableWidgetItem("Plato"))
            self.ui.TWTabla.setHorizontalHeaderItem(3, QTableWidgetItem("Precio"))
            self.ui.TWTabla.setHorizontalHeaderItem(4, QTableWidgetItem(""))

            for registro in resultados:
                self.ui.TWTabla.insertRow(cant)

                celdaFecha = QTableWidgetItem(str(registro[0]))
                celdaCliente = QTableWidgetItem(registro[1])
                celdaPlato = QTableWidgetItem(registro[2])
                celdaPrecio = QTableWidgetItem(str(registro[3]))

                self.ui.TWTabla.setItem(cant, 0, celdaFecha)
                self.ui.TWTabla.setItem(cant, 1, celdaCliente)
                self.ui.TWTabla.setItem(cant, 2, celdaPlato)
                self.ui.TWTabla.setItem(cant, 3, celdaPrecio)

                cant += 1

            if cant == 0:
                QMessageBox.information(self, "Listado", "No hay compras asociadas a ese ID..!!")

            mycursor.close()
        except Exception as miError:
            QMessageBox.warning(self, "Error", 'Fallo ejecutando el procedimiento')
            print(miError)
