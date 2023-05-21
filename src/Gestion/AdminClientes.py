from PyQt6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem

from src.Conex.Conexion import Conexion
from src.GUIS.DClientes import Ui_MainWindow
class AdminClientes(QMainWindow):

    def __init__(self):
        super(AdminClientes, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.con = Conexion()
        self.miConexion = self.con.conectar()
        print('Objeto tipo AdminCliente creado y listo para usarse..!!')

        self.ui.PBTodas.clicked.connect(self.verTodos)
        self.ui.PBBuscar.clicked.connect(self.buscarCliente)
        self.ui.PBAgregar.clicked.connect(self.agregaCliente)
        self.ui.PBModificar.clicked.connect(self.modificarCliente)
        self.ui.PBEliminar.clicked.connect(self.eliminaCliente)
        self.ui.PBSalir.clicked.connect(self.cerrarConexion)

        self.verTodos()

    def cerrarConexion(self):
        self.con.desconectar()
        self.close()

    def verTodos(self):
        cant = 0
        try:
            mycursor = self.miConexion.cursor()
            mycursor.callproc('allClientes')

            total = self.ui.TWTabla.rowCount()
            for rep in range(total):
                self.ui.TWTabla.removeRow(0)

            for result in mycursor.stored_results():
                for (idCliente, nombre, telefono, correo) in result:
                    self.ui.TWTabla.insertRow(cant)
                    celdaId = QTableWidgetItem(str(idCliente))
                    celdaNombre = QTableWidgetItem(nombre)
                    celdaTelefono = QTableWidgetItem(telefono)
                    celdaCorreo = QTableWidgetItem(correo)

                    self.ui.TWTabla.setItem(cant, 0, celdaId)
                    self.ui.TWTabla.setItem(cant, 1, celdaNombre)
                    self.ui.TWTabla.setItem(cant, 2, celdaTelefono)
                    self.ui.TWTabla.setItem(cant, 3, celdaCorreo)

                    cant += 1
            if cant == 0:
                QMessageBox.information(self, "Ver Todos", "No hay clientes registrados..!!")

            mycursor.close()

        except Exception as miError:
            QMessageBox.warning(self, "Error", 'Fallo ejecutando el procedimiento')
            print(miError)

    def buscarCliente(self):
        cant = 0
        idClienteSearch = self.ui.SBId.value()
        if not self.existeIdCliente(idClienteSearch):
            QMessageBox.information(self, "Buscar", "El cliente no existe")
        else:
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('getCliente', [idClienteSearch])

                total = self.ui.TWTabla.rowCount()
                for rep in range(total):
                    self.ui.TWTabla.removeRow(0)

                for result in mycursor.stored_results():
                    for (idClienteSearch, nombre, telefono, correo) in result:
                        self.ui.TWTabla.insertRow(cant)

                        celdaId = QTableWidgetItem(str(idClienteSearch))
                        celdaNombre = QTableWidgetItem(nombre)
                        celdaTelefono = QTableWidgetItem(telefono)
                        celdaCorreo = QTableWidgetItem(correo)

                        self.ui.TWTabla.setItem(cant, 0, celdaId)
                        self.ui.TWTabla.setItem(cant, 1, celdaNombre)
                        self.ui.TWTabla.setItem(cant, 2, celdaTelefono)
                        self.ui.TWTabla.setItem(cant, 3, celdaCorreo)

                mycursor.close()

            except Exception as miError:
                QMessageBox.warning(self, "Error", 'Fallo ejecutando el procedimiento')
                print(miError)

    def agregaCliente(self):

        idCliente = self.ui.SBId2.value()

        if self.existeIdCliente(idCliente):
            QMessageBox.information(self, "Agregar", "El cliente ya existe, no se puede repetir")
        else:
            nombre = self.ui.LENombre.text()
            telefono = self.ui.LETelefono.text()
            correo = self.ui.LECorreo.text()
            if self.existeCorreo(correo):
                QMessageBox.information(self, "Agregar", "Ya existe un cliente con ese correo!")
            else:
                try:
                    mycursor = self.miConexion.cursor()

                    mycursor.callproc('newCliente', [idCliente, nombre, telefono, correo])
                    self.miConexion.commit()

                    QMessageBox.information(self, "Agregar", "El cliente ha sido creado!")
                    mycursor.close()

                except Exception as miError:
                    QMessageBox.warning(self, "Error", 'Fallo ejecutando el procedimiento')
                    print(miError)
        self.verTodos()

    def eliminaCliente(self):
        idClienteDel = self.ui.SBId.value()
        if not self.existeIdCliente(idClienteDel):
            QMessageBox.information(self, "Eliminar", "El cliente no existe, no se puede eliminar")
        else:
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('delCliente', [idClienteDel])
                self.miConexion.commit()

                QMessageBox.information(self, "Eliminar", 'El cliente ha sido eliminado..!!')
                mycursor.close()
            except Exception as miError:
                QMessageBox.warning(self, "Error", 'Fallo ejecutando el procedimiento')
                print(miError)
        self.verTodos()

    def modificarCliente(self):

        idClienteOld = self.ui.SBId2.value()

        if not self.existeIdCliente(idClienteOld):
            QMessageBox.information(self, "Modificar", 'Ese cliente no existe, no se pude modificar')
        else:
            try:
                mycursor = self.miConexion.cursor()
                idClienteNew = self.ui.SBNuevoId.value()
                if idClienteNew != idClienteOld and self.existeIdCliente(idClienteNew):
                    QMessageBox.information(self, "Modificar",
                                            "Ya existe un cliente con ese ID, no se puede modificar")
                nombreNew = self.ui.LENewNombre.text()
                telefonoNew = self.ui.LENewTelefono.text()
                correoNew = self.ui.LENewCorreo.text()
                if self.existeCorreo(correoNew):
                    QMessageBox.information(self, "Modificar",
                                            "Ya existe un cliente con ese correo, no se puede modificar")
                    mycursor.close()
                else:
                    mycursor.callproc('modCliente', [idClienteNew, nombreNew, telefonoNew, correoNew, idClienteOld])
                    self.miConexion.commit()
                    QMessageBox.information(self, "Modificar","Has modificado el cliente con éxito")
                    mycursor.close()
            except Exception as miError:
                QMessageBox.warning(self, "Error", 'Fallo ejecutando el procedimiento')
                print(miError)
        self.verTodos()

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
