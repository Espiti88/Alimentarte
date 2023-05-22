import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox

from GUIS.Principal import Ui_MainWindow
from src.Gestion.AdminCategorias import AdminCategorias
from src.Gestion.AdminClientes import AdminClientes
from src.Gestion.AdminPedidos import AdminPedidos
from src.Gestion.AdminPlatos import AdminPlatos
from src.Gestion.AdminRestaurantes import AdminRestaurantes
from src.Gestion.Consultas import Consultas


class Principal(QMainWindow):
    def __init__(self):
        super(Principal, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.BCategoria.clicked.connect(self.categoria)
        self.ui.BPlato.clicked.connect(self.plato)
        self.ui.BCliente.clicked.connect(self.cliente)
        self.ui.BRestaurante.clicked.connect(self.restaurante)
        self.ui.BPedido.clicked.connect(self.pedido)
        self.ui.BConsultas.clicked.connect(self.consultas)
        self.ui.BTerminar.clicked.connect(self.terminar)

    def categoria(self):
        print("Se llama a Categoria")
        self.ventanaCategoria = AdminCategorias()
        self.ventanaCategoria.show()

    def plato(self):
        print("Se llama a Plato")
        self.ventanaPlato = AdminPlatos()
        self.ventanaPlato.show()

    def cliente(self):
        print("Se llama a Cliente")
        self.ventanaCliente = AdminClientes()
        self.ventanaCliente.show()

    def restaurante(self):
        print("Se llama a Restaurante")
        self.ventanaRestaurante = AdminRestaurantes()
        self.ventanaRestaurante.show()

    def pedido(self):
        print("Se llama a Pedido")
        self.ventanaPedido = AdminPedidos()
        self.ventanaPedido.show()

    def consultas(self):
        print("Se llama a Consultas")
        self.ventanaConsultas = Consultas()
        self.ventanaConsultas.show()

    def terminar(self):
        QMessageBox.information(self, "Adiós", "Gracias por usar nuestros servicios")
        self.close()


if __name__ == '__main__':
    app = QApplication([])
    ventanaPrincipal = Principal()
    ventanaPrincipal.show()
    sys.exit(app.exec())
