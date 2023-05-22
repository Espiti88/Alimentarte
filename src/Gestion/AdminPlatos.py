from PyQt6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem

from src.Conex.Conexion import Conexion
from src.GUIS.DPlatos import Ui_MainWindow

class AdminPlatos(QMainWindow):

    def __init__(self):
        super(AdminPlatos, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.con = Conexion()
        self.miConexion = self.con.conectar()
        print('Objeto tipo AdminPlato creado y listo para usarse..!!')

        self.ui.PBTodas.clicked.connect(self.verTodos)
        self.ui.PBBuscar.clicked.connect(self.buscarPlato)
        self.ui.PBAgregar.clicked.connect(self.agregarPlato)
        self.ui.PBModificar.clicked.connect(self.modificarPlato)
        self.ui.PBEliminar.clicked.connect(self.eliminarPlato)
        self.ui.PBSalir.clicked.connect(self.cerrarConexion)

        self.verTodos()

    def cerrarConexion(self):
        self.con.desconectar()
        self.close()

    def verTodos(self):
        cant = 0
        try:
            mycursor = self.miConexion.cursor()
            mycursor.callproc('allPlatos')
            total = self.ui.TWTabla.rowCount()
            for rep in range(total):
                self.ui.TWTabla.removeRow(0)
            for result in mycursor.stored_results():
                for (idPlato, nombre, precio, mani, picante, restaurante, descripcion) in result:
                    self.ui.TWTabla.insertRow(cant)
                    celdaId = QTableWidgetItem(str(idPlato))
                    celdaNombre = QTableWidgetItem(nombre)
                    celdaPrecio = QTableWidgetItem(str(precio))
                    celdaMani = QTableWidgetItem(mani)
                    celdaPicante = QTableWidgetItem(picante)
                    celdaRestaurante = QTableWidgetItem(str(restaurante))
                    celdaDescripcion = QTableWidgetItem(descripcion)
                    self.ui.TWTabla.setItem(cant, 0, celdaId)
                    self.ui.TWTabla.setItem(cant, 1, celdaNombre)
                    self.ui.TWTabla.setItem(cant, 2, celdaPrecio)
                    self.ui.TWTabla.setItem(cant, 3, celdaMani)
                    self.ui.TWTabla.setItem(cant, 4, celdaPicante)
                    self.ui.TWTabla.setItem(cant, 5, celdaRestaurante)
                    self.ui.TWTabla.setItem(cant, 6, celdaDescripcion)

                    cant += 1
            if cant == 0:
                QMessageBox.information(self, "Ver Todos", "No hay platos registrados..!!")
            mycursor.close()
        except Exception as miError:
            QMessageBox.warning(self, "Error", 'Fallo ejecutando el procedimiento')
            print(miError)

    def buscarPlato(self):
        cant = 0
        idPlato = self.ui.SBIdPlatoBusq.value()
        if not self.existeIdPlato(idPlato):
            QMessageBox.information(self, "Buscar", "El plato no existe")
        else:
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('getPlato', [idPlato])
                total = self.ui.TWTabla.rowCount()
                for rep in range(total):
                    self.ui.TWTabla.removeRow(0)
                for result in mycursor.stored_results():
                    for (idPlato, nombre, precio, mani, picante, restaurante, descripcion) in result:
                        self.ui.TWTabla.insertRow(cant)
                        celdaId = QTableWidgetItem(str(idPlato))
                        celdaNombre = QTableWidgetItem(nombre)
                        celdaPrecio = QTableWidgetItem(str(precio))
                        celdaMani = QTableWidgetItem(mani)
                        celdaPicante = QTableWidgetItem(picante)
                        celdaRestaurante = QTableWidgetItem(str(restaurante))
                        celdaDescripcion = QTableWidgetItem(descripcion)

                        self.ui.TWTabla.setItem(cant, 0, celdaId)
                        self.ui.TWTabla.setItem(cant, 1, celdaNombre)
                        self.ui.TWTabla.setItem(cant, 2, celdaPrecio)
                        self.ui.TWTabla.setItem(cant, 3, celdaMani)
                        self.ui.TWTabla.setItem(cant, 4, celdaPicante)
                        self.ui.TWTabla.setItem(cant, 5, celdaRestaurante)
                        self.ui.TWTabla.setItem(cant, 6, celdaDescripcion)
                mycursor.close()
            except Exception as miError:
                QMessageBox.warning(self, "Error", 'Fallo ejecutando el procedimiento')
                print(miError)

    def agregarPlato(self):
        idPlato = self.ui.SBIdPlato.value()
        if self.existeIdPlato(idPlato):
            QMessageBox.information(self, "Agregar", "Ya existe un plato con ese código")
        else:
            nombre = self.ui.SBIdPlato.value()
            precio = self.ui.SBPrecio.value()
            mani = self.ui.CBMani.currentText().lower()
            picante = self.ui.CBPicante.currentText().lower()

            restaurante = self.ui.SBRestaurante.value()
            if not self.existeRestaurante(restaurante):
                QMessageBox.information(self, "Agregar", "No existe un restaurante con ese código, "
                                                         "no se puede crear el plato")
            else:
                descripcion = self.ui.TEDescripcion.toPlainText()
                if self.existeDescripcion(descripcion):
                    QMessageBox.information(self, "Agregar", "Ya existe esa descripción en otro plato, no se puede repetir")
                else:
                    try:
                        mycursor = self.miConexion.cursor()
                        mycursor.callproc('newPlato', [idPlato, nombre, precio, mani, picante, restaurante, descripcion])
                        self.miConexion.commit()
                        QMessageBox.information(self, "Agregar", "El plato ha sido creado")
                        mycursor.close()
                    except Exception as miError:
                        QMessageBox.warning(self, "Error", 'Fallo ejecutando el procedimiento')
                        print(miError)
        self.verTodos()

    def eliminarPlato(self):
        idPlato = self.ui.SBIdPlatoBusq.value()
        if not self.existeIdPlato(idPlato):
            QMessageBox.information(self, "Eliminar", "No existe un plato con ese código")
        else:
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('delPlato', [idPlato])
                self.miConexion.commit()
                QMessageBox.information(self, "Eliminar", "El plato ha sido elminado")
                mycursor.close()
            except Exception as miError:
                QMessageBox.warning(self, "Error", 'Fallo ejecutando el procedimiento')
                print(miError)
        self.verTodos()

    def modificarPlato(self):
        idPlatoOld = self.ui.SBIdPlato.value()
        if not self.existeIdPlato(idPlatoOld):
            QMessageBox.information(self, "Modificar", "Ese plato no existe, no se puede modificar")
        else:
            try:
                mycursor = self.miConexion.cursor()
                newIdPlato = self.ui.SBnewIdPlato.value()

                if self.existeIdPlato(newIdPlato) and newIdPlato != idPlatoOld:
                    QMessageBox.information(self, "Modificar", "Ya hay un plato con ese ID, no se puede repetir")
                else:
                    newNombre = self.ui.LEnewNombre.text()
                    newPrecio = self.ui.SBnewPrecio.value()
                    newMani = self.ui.CBnewMani.currentText().lower()
                    newPicante = self.ui.CBnewPicante.currentText().lower()

                    newRestaurante = self.ui.SBnewRestaurante.value()
                    if not self.existeRestaurante(newRestaurante):
                        print("No existe un restaurante con ese código.")
                        QMessageBox.information(self, "Modificar", "No existe un restaurante con ese código")
                    else:
                        newDescripcion = self.ui.TEnewDescripcion.toPlainText()
                        if self.existeDescripcion(newDescripcion):
                            QMessageBox.information(self, "Modificar", "Ya existe esa descripción en otro plato.")
                        else:
                            mycursor.callproc('modPlato', [newIdPlato, newNombre, newPrecio, newMani, newPicante, newRestaurante, newDescripcion, idPlatoOld])
                            self.miConexion.commit()
                            QMessageBox.information(self, "Modificar", "El plato fue modificado")
                mycursor.close()

            except Exception as miError:
                QMessageBox.warning(self, "Error", 'Fallo ejecutando el procedimiento')
                print(miError)
        self.verTodos()

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
