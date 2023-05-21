from PyQt6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem

from src.Conex.Conexion import Conexion
from src.GUIS.DRestaurantes import Ui_MainWindow
class AdminRestaurantes(QMainWindow):

    def __init__(self):
        super(AdminRestaurantes, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.con = Conexion()
        self.miConexion = self.con.conectar()
        print('Objeto tipo AdminRestaurante creado y listo para usarse..!!')

        self.ui.PBTodas.clicked.connect(self.verTodos)
        self.ui.PBBuscar.clicked.connect(self.buscarRestaurante)
        self.ui.PBAgregar.clicked.connect(self.agregaRestaurante)
        self.ui.PBModificar.clicked.connect(self.modificarRestaurante)
        self.ui.PBEliminar.clicked.connect(self.eliminarRestaurante)
        self.ui.PBSalir.clicked.connect(self.cerrarConexion)

        self.verTodos()

    def cerrarConexion(self):
        self.con.desconectar()
        self.close()

    def verTodos(self):
        cant = 0
        try:
            mycursor = self.miConexion.cursor()
            mycursor.callproc('allRestaurantes')

            total = self.ui.TWTabla.rowCount()
            for rep in range(total):
                self.ui.TWTabla.removeRow(0)

            for result in mycursor.stored_results():
                for (idRestaurante, nombre, categoria, slogan, direccion) in result:
                    self.ui.TWTabla.insertRow(cant)

                    celdaId = QTableWidgetItem(str(idRestaurante))
                    celdaNombre = QTableWidgetItem(nombre)
                    celdaCategoria = QTableWidgetItem(str(categoria))
                    celdaSlogan = QTableWidgetItem(slogan)
                    celdaDireccion = QTableWidgetItem(direccion)

                    self.ui.TWTabla.setItem(cant, 0, celdaId)
                    self.ui.TWTabla.setItem(cant, 1, celdaNombre)
                    self.ui.TWTabla.setItem(cant, 2, celdaCategoria)
                    self.ui.TWTabla.setItem(cant, 3, celdaSlogan)
                    self.ui.TWTabla.setItem(cant, 4, celdaDireccion)

                    cant = cant + 1
            if cant == 0:
                QMessageBox.information(self, "Ver Todos", "No hay restaurantes registradas..!!")
            mycursor.close()
        except Exception as miError:
            QMessageBox.warning(self, "Error", 'Fallo ejecutando el procedimiento')
            print(miError)

    def buscarRestaurante(self):
        cant = 0

        idRestauranteSearch = self.ui.SBId.value()
        if not self.existeIdRestaurante(idRestauranteSearch):
            QMessageBox.information(self, "Buscar", "El restaurante no existe")
        else:
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('getRestaurante', [idRestauranteSearch])

                total = self.ui.TWTabla.rowCount()
                for rep in range(total):
                    self.ui.TWTabla.removeRow(0)

                for result in mycursor.stored_results():
                    for (idRestaurante, nombre, categoria, slogan, direccion) in result:
                        self.ui.TWTabla.insertRow(cant)

                        celdaId = QTableWidgetItem(str(idRestaurante))
                        celdaNombre = QTableWidgetItem(nombre)
                        celdaCategoria = QTableWidgetItem(str(categoria))
                        celdaSlogan = QTableWidgetItem(slogan)
                        celdaDireccion = QTableWidgetItem(direccion)

                        self.ui.TWTabla.setItem(cant, 0, celdaId)
                        self.ui.TWTabla.setItem(cant, 1, celdaNombre)
                        self.ui.TWTabla.setItem(cant, 2, celdaCategoria)
                        self.ui.TWTabla.setItem(cant, 3, celdaSlogan)
                        self.ui.TWTabla.setItem(cant, 4, celdaDireccion)
                mycursor.close()
            except Exception as miError:
                QMessageBox.warning(self, "Error", 'Fallo ejecutando el procedimiento')
                print(miError)

    def agregaRestaurante(self):
        idRestauranteNew = self.ui.SBId2.value()
        if self.existeIdRestaurante(idRestauranteNew):
            QMessageBox.information(self, "Agregar Restaurante", "El restaurante ya existe, no se puede repetir")
        else:
            nombre = self.ui.LENombre.text()
            categoria = self.ui.SBCategoria.value()
            if not self.existeCategoria(categoria):
                QMessageBox.information(self, "Agregar Restaurante", "No existe una categoria con ese código.")
            else:
                slogan = self.ui.LESlogan.text()
                direccion = self.ui.LEDireccion.text()
                try:
                    mycursor = self.miConexion.cursor()
                    mycursor.callproc('newRestaurante', [idRestauranteNew, nombre, categoria, slogan, direccion])
                    self.miConexion.commit()

                    QMessageBox.information(self, "Agregar", "El restaurante ha sido creado")
                    mycursor.close()

                except Exception as miError:
                    QMessageBox.warning(self, "Error", 'Fallo ejecutando el procedimiento')
                    print(miError)
        self.verTodos()

    def eliminarRestaurante(self):

        idRestauranteDel = self.ui.SBId.value()
        if not self.existeIdRestaurante(idRestauranteDel):
            QMessageBox.information(self, "Eliminar", "El restaurante no existe, no se puede eliminar")
        else:
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('delRestaurante', [idRestauranteDel])
                self.miConexion.commit()

                QMessageBox.information(self, "Eliminar", "El restaurante ha sido eliminado")
                mycursor.close()

            except Exception as miError:
                QMessageBox.warning(self, "Error", 'Fallo ejecutando el procedimiento')
                print(miError)
        self.verTodos()

    def modificarRestaurante(self):

        idRestauranteOld = self.ui.SBId2.value()

        if not self.existeIdRestaurante(idRestauranteOld):
            QMessageBox.information(self, "Modificar", "Ese restaurante no existe, no se pude modificar")
        else:
            idRestauranteNew = self.ui.SBNuevoId.value()
            if idRestauranteNew != idRestauranteOld and self.existeIdRestaurante(idRestauranteNew):
                QMessageBox.information(self, "Modificar",
                                        "Ya existe un restaurante con ese ID, No se puede modificar")
            else:
                categoriaNew = self.ui.SBNewCategoria.value()
                try:
                    mycursor = self.miConexion.cursor()
                    if not self.existeCategoria(categoriaNew):
                        QMessageBox.information(self, "Modificar", "No existe esa categoría")
                    else:
                        nombreNew = self.ui.LENewNombre.text()
                        sloganNew = self.ui.LENewSlogan.text()
                        direccionNew = self.ui.LENewDireccion.text()
                        mycursor.callproc('modRestaurantes', [idRestauranteNew, nombreNew, categoriaNew, sloganNew, direccionNew, idRestauranteOld])
                        self.miConexion.commit()
                        QMessageBox.information(self, "Modificar", "El restaurante ha sido modificado")
                        mycursor.close()
                except Exception as miError:
                    QMessageBox.warning(self, "Error", 'Fallo ejecutando el procedimiento')
                    print(miError)
        self.verTodos()

    def existeIdRestaurante(self, id):
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