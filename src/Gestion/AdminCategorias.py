import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem

from src.Conex.Conexion import Conexion
from src.GUIS.DCategorias import Ui_MainWindow


class AdminCategorias(QMainWindow):

    def __init__(self):
        super(AdminCategorias, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.con = Conexion()
        self.miConexion = self.con.conectar()
        print('Objeto tipo AdminCategoria creado y listo para usarse..!!')

        self.ui.PBTodas.clicked.connect(self.verTodas)
        self.ui.PBBuscar.clicked.connect(self.buscarCategoria)
        self.ui.PBAgregar.clicked.connect(self.agregaCategoria)
        self.ui.PBModificar.clicked.connect(self.modifyCategoria)
        self.ui.PBEliminar.clicked.connect(self.eliminaCategoria)
        self.ui.PBSalir.clicked.connect(self.cerrarConexion)

        self.verTodas()

    def cerrarConexion(self):
        self.con.desconectar()
        self.close()

    def verTodas(self):
        cant = 0
        try:
            mycursor = self.miConexion.cursor()
            mycursor.callproc('allCategorias')

            total = self.ui.TWTabla.rowCount()
            for rep in range(total):
                self.ui.TWTabla.removeRow(0)

            for result in mycursor.stored_results():
                for (idCategoria, nombre) in result:
                    self.ui.TWTabla.insertRow(cant)

                    celdaId = QTableWidgetItem(str(idCategoria))
                    celdaNombre = QTableWidgetItem(nombre)

                    self.ui.TWTabla.setItem(cant, 0, celdaId)
                    self.ui.TWTabla.setItem(cant, 1, celdaNombre)

                    cant = cant + 1
            if cant == 0:
                QMessageBox.information(self, "Ver Todas", "No hay categorias registradas..!!")

            mycursor.close()
        except Exception as miError:
            QMessageBox.warning(self, "Error", 'Fallo ejecutando el procedimiento')
            print(miError)

    def buscarCategoria(self):
        cant = 0

        idCategoriaSearch = self.ui.SBId.value()
        if not self.existeIdCategoria(idCategoriaSearch):
            QMessageBox.information(self, "Buscar", "La categoria no existe")
        else:
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('getCategoria', [idCategoriaSearch])

                total = self.ui.TWTabla.rowCount()
                for rep in range(total):
                    self.ui.TWTabla.removeRow(0)

                for result in mycursor.stored_results():
                    for (idCategoria, nombre) in result:
                        self.ui.TWTabla.insertRow(cant)

                        celdaId = QTableWidgetItem(str(idCategoria))
                        celdaNombre = QTableWidgetItem(nombre)

                        self.ui.TWTabla.setItem(cant, 0, celdaId)
                        self.ui.TWTabla.setItem(cant, 1, celdaNombre)

                mycursor.close()

            except Exception as miError:
                QMessageBox.warning(self, "Error", 'Fallo ejecutando el procedimiento')
                print(miError)

    def agregaCategoria(self):
        idCategoriaNew = self.ui.SBId2.value()
        if self.existeIdCategoria(idCategoriaNew):
            QMessageBox.information(self, "Agregar Categoria", "La categoria ya existe, no se puede repetir")
        else:
            nombreNew = self.ui.LENombre.text()
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc("newCategoria", [idCategoriaNew, nombreNew])
                self.miConexion.commit()
                QMessageBox.information(self, "Agregar Categoria", "La categoria ha sido creada")
                mycursor.close()

            except Exception as miError:
                QMessageBox.warning(self, "Agregar Categoria", "La categoria ya existe, no se puede repetir")
                print(miError)
        self.verTodas()


    def eliminaCategoria(self):

        idCategoriaDel = self.ui.SBId.value()
        if not self.existeIdCategoria(idCategoriaDel):
            QMessageBox.information(self, "Eliminar", "La categoria no existe, no se puede eliminar")
        else:
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('delCategoria', [idCategoriaDel])
                self.miConexion.commit()

                QMessageBox.information(self, "Eliminar", 'La categoria ha sido eliminada..!!')
                mycursor.close()
            except Exception as miError:
                QMessageBox.warning(self, "Eliminar", 'Fallo ejecutando el procedimiento')
                print(miError)
        self.verTodas()

    def modifyCategoria(self):
        idCategoriaOld = self.ui.SBId2.value()
        if not self.existeIdCategoria(idCategoriaOld):
            QMessageBox.information(self, "Modificar", "La categoria no existe")
        else:
            idCategoriaNew = self.ui.SBNuevoId.value()
            if idCategoriaNew != idCategoriaOld and self.existeIdCategoria(idCategoriaNew):
                QMessageBox.information(self, "Modificar",
                                        "Ya existe una categoria con ese ID, No se puede modificar")
            else:
                nombreNew = self.ui.LENombre.text()
                try:
                    mycursor = self.miConexion.cursor()
                    mycursor.callproc('modCategoria', [idCategoriaNew, nombreNew, idCategoriaOld])
                    self.miConexion.commit()
                    QMessageBox.information(self, "Modificar", 'La categoria ha sido modificada..!!')
                    mycursor.close()

                    self.verTodas()

                except Exception as miError:
                    QMessageBox.warning(self, "Modificar", 'Fallo ejecutando el procedimiento')
                    print(miError)
        self.verTodas()

    def existeIdCategoria(self, idCategoria):
        try:
            mycursor = self.miConexion.cursor()
            query = "SELECT count(*) FROM CATEGORIAS WHERE idCategoria = %s"
            mycursor.execute(query, [idCategoria])
            resultados = mycursor.fetchall()
            for registro in resultados:
                if registro[0] == 1:
                    return True
                return False
        except Exception as miError:
            QMessageBox.information(self, "Existe Categoria", 'Fallo ejecutando el procedimiento')
            print(miError)


if __name__ == '__main__':
    app = QApplication([])
    ventanaAdminCategorias = AdminCategorias()
    ventanaAdminCategorias.show()
    sys.exit(app.exec())