from PyQt6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from src.Conex.Conexion import Conexion
from src.GUIS.DPedidos import Ui_MainWindow


class AdminPedidos(QMainWindow):

    def __init__(self):
        super(AdminPedidos, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.con = Conexion()
        self.miConexion = self.con.conectar()
        print('Objeto tipo AdminPedido creado y listo para usarse..!!')

        self.ui.PBTodas.clicked.connect(self.verTodos)
        self.ui.PBBuscar.clicked.connect(self.buscarPedido)
        self.ui.PBAgregar.clicked.connect(self.agregaPedido)
        self.ui.PBModificar.clicked.connect(self.modificarPedido)
        self.ui.PBEliminar.clicked.connect(self.eliminarPedido)
        self.ui.PBSalir.clicked.connect(self.cerrarConexion)

        self.verTodos()

    def cerrarConexion(self):
        self.con.desconectar()
        self.close()

    def verTodos(self):
        cant = 0
        try:
            mycursor = self.miConexion.cursor()
            mycursor.callproc('allPedidos')
            total = self.ui.TWTabla.rowCount()
            for rep in range(total):
                self.ui.TWTabla.removeRow(0)
            for result in mycursor.stored_results():
                for (idCliente, idPlato, fecha_hora) in result:
                    self.ui.TWTabla.insertRow(cant)
                    celdaIdCliente = QTableWidgetItem(str(idCliente))
                    celdaIdPlato = QTableWidgetItem(str(idPlato))
                    celdaFecha = QTableWidgetItem(str(fecha_hora))

                    self.ui.TWTabla.setItem(cant, 0, celdaIdCliente)
                    self.ui.TWTabla.setItem(cant, 1, celdaIdPlato)
                    self.ui.TWTabla.setItem(cant, 2, celdaFecha)

                    cant += 1
            if cant == 0:
                QMessageBox.information(self, "Ver Todos", "No hay pedidos registrados..!!")
            mycursor.close()
        except Exception as miError:
            QMessageBox.warning(self, "Error", 'Fallo ejecutando el procedimiento')
            print(miError)

    def buscarPedido(self):
        cant = 0
        idCliente = self.ui.SBCliente.value()
        idPlato = self.ui.SBPlato.value()
        fecha_hora = self.ui.dateTimeEdit.text()
        if not self.existeCodigo(idCliente, idPlato, fecha_hora):
            QMessageBox.information(self, "Buscar", "No existe ese pedido")
        else:
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('getPedido', [idCliente, idPlato, fecha_hora])
                total = self.ui.TWTabla.rowCount()
                for rep in range(total):
                    self.ui.TWTabla.removeRow(0)
                for result in mycursor.stored_results():
                    for (idCliente, idPlato, fecha_hora) in result:
                        self.ui.TWTabla.insertRow(cant)
                        celdaIdCliente = QTableWidgetItem(str(idCliente))
                        celdaIdPlato = QTableWidgetItem(str(idPlato))
                        celdaFecha = QTableWidgetItem(str(fecha_hora))
                        self.ui.TWTabla.setItem(cant, 0, celdaIdCliente)
                        self.ui.TWTabla.setItem(cant, 1, celdaIdPlato)
                        self.ui.TWTabla.setItem(cant, 2, celdaFecha)
                mycursor.close()
            except Exception as miError:
                QMessageBox.warning(self, "Error", 'Fallo ejecutando el procedimiento')
                print(miError)

    def agregaPedido(self):
        idCliente = self.ui.SBCliente.value()
        if not self.existeIdCliente(idCliente):
            QMessageBox.information(self, "Agregar", "No existe un cliente con ese código, no se puede crear el pedido")
        else:
            idPlato = self.ui.SBPlato.value()
            if not self.existeIdPlato(idPlato):
                QMessageBox.information(self, "Agregar", "No existe un plato con ese código, no se puede crear el pedido")
            else:
                fecha_hora = self.ui.dateTimeEdit.text()
                if self.existeCodigo(idCliente, idPlato, fecha_hora):
                    QMessageBox.information(self, "Agregar", "Ya existe ese pedido, no se puede repetir")
                else:
                    try:
                        mycursor = self.miConexion.cursor()
                        mycursor.callproc('newPedido', [idCliente, idPlato, fecha_hora])
                        self.miConexion.commit()
                        QMessageBox.information(self, "Agregar", "El pedido ha sido creado")
                        mycursor.close()
                        self.verTodos()
                    except Exception as miError:
                        QMessageBox.warning(self, "Error", 'Fallo ejecutando el procedimiento')
                        print(miError)

    def eliminarPedido(self):

        idCliente = self.ui.SBCliente.value()
        idPlato = self.ui.SBPlato.value()
        fecha_hora = self.ui.dateTimeEdit.text()
        if not self.existeCodigo(idCliente, idPlato, fecha_hora):
            QMessageBox.information(self, "Eliminar", "Ese pedido no existe, no se puede eliminar")
        else:
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('delPedido', [idCliente, idPlato, fecha_hora])
                self.miConexion.commit()
                mycursor.close()
                QMessageBox.information(self, "Eliminar", "El pedido ha sido eliminado")
                self.verTodos()
            except Exception as miError:
                QMessageBox.warning(self, "Error", 'Fallo ejecutando el procedimiento')
                print(miError)

    def modificarPedido(self):

        idCliente = self.ui.SBCliente.value()
        idPlato = self.ui.SBPlato.value()
        fecha_hora = self.ui.dateTimeEdit.text()
        if not self.existeCodigo(idCliente, idPlato, fecha_hora):
            QMessageBox.information(self, "Modificar", "Ese pedido no existe, no se puede modificar")
        else:
            try:
                mycursor = self.miConexion.cursor()
                newIdCliente = self.ui.SBnewCliente.value()
                if not self.existeIdCliente(newIdCliente):
                    QMessageBox.information(self, "Modificar", "Ese cliente no existe, no se puede modificar el pedido")
                    mycursor.close()
                else:
                    newIdPlato = self.ui.SBnewPlato.value()
                    if not self.existeIdPlato(newIdPlato):
                        QMessageBox.information(self, "Modificar", "Ese plato no existe, no se puede modificar el pedido")
                        mycursor.close()
                    else:
                        newFecha_hora = self.ui.newDateTimeEdit.text()
                        if self.existeCodigo(newIdCliente, newIdPlato, newFecha_hora) and (
                                newIdCliente != idCliente or newIdPlato != idPlato or newFecha_hora != fecha_hora):
                            QMessageBox.information(self, "Modificar", "Ese pedido ya existe, no se puede repetir")
                        else:
                            mycursor.callproc('modPedido',
                                              [newIdCliente, newIdPlato, newFecha_hora, idCliente, idPlato, fecha_hora])
                            self.miConexion.commit()
                            QMessageBox.information(self, "Modificar", "El pedido ha sido modificado")
                            self.verTodos()
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
