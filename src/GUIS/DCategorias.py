# Form implementation generated from reading ui file 'src/GUIS/DCategorias.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1097, 686)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 113, 170))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 113, 170))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 113, 170))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ToolTipText, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 10, 971, 441))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.SBId = QtWidgets.QSpinBox(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SBId.setFont(font)
        self.SBId.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.SBId.setMaximum(999999999)
        self.SBId.setObjectName("SBId")
        self.gridLayout.addWidget(self.SBId, 1, 1, 1, 2)
        self.TWTabla = QtWidgets.QTableWidget(parent=self.layoutWidget)
        self.TWTabla.setMinimumSize(QtCore.QSize(711, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TWTabla.setFont(font)
        self.TWTabla.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.TWTabla.setObjectName("TWTabla")
        self.TWTabla.setColumnCount(2)
        self.TWTabla.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.TWTabla.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.TWTabla.setHorizontalHeaderItem(1, item)
        self.TWTabla.horizontalHeader().setDefaultSectionSize(144)
        self.TWTabla.horizontalHeader().setHighlightSections(True)
        self.TWTabla.verticalHeader().setVisible(False)
        self.TWTabla.verticalHeader().setMinimumSectionSize(60)
        self.gridLayout.addWidget(self.TWTabla, 7, 0, 1, 3)
        self.PBEliminar = QtWidgets.QPushButton(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PBEliminar.setFont(font)
        self.PBEliminar.setObjectName("PBEliminar")
        self.gridLayout.addWidget(self.PBEliminar, 3, 0, 1, 1)
        self.LTitulo = QtWidgets.QLabel(parent=self.layoutWidget)
        self.LTitulo.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.LTitulo.setFont(font)
        self.LTitulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.LTitulo.setObjectName("LTitulo")
        self.gridLayout.addWidget(self.LTitulo, 0, 0, 1, 3)
        self.PBSalir = QtWidgets.QPushButton(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PBSalir.setFont(font)
        self.PBSalir.setObjectName("PBSalir")
        self.gridLayout.addWidget(self.PBSalir, 8, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        self.LId = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LId.setFont(font)
        self.LId.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.LId.setObjectName("LId")
        self.gridLayout.addWidget(self.LId, 1, 0, 1, 1)
        self.PBTodas = QtWidgets.QPushButton(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PBTodas.setFont(font)
        self.PBTodas.setObjectName("PBTodas")
        self.gridLayout.addWidget(self.PBTodas, 3, 2, 1, 1)
        self.PBBuscar = QtWidgets.QPushButton(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PBBuscar.setFont(font)
        self.PBBuscar.setObjectName("PBBuscar")
        self.gridLayout.addWidget(self.PBBuscar, 3, 1, 1, 1)
        self.PBModificar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.PBModificar.setGeometry(QtCore.QRect(550, 550, 231, 37))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PBModificar.setFont(font)
        self.PBModificar.setObjectName("PBModificar")
        self.PBAgregar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.PBAgregar.setGeometry(QtCore.QRect(300, 550, 231, 37))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PBAgregar.setFont(font)
        self.PBAgregar.setObjectName("PBAgregar")
        self.LIdAgregar = QtWidgets.QLabel(parent=self.centralwidget)
        self.LIdAgregar.setGeometry(QtCore.QRect(20, 480, 71, 37))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LIdAgregar.setFont(font)
        self.LIdAgregar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.LIdAgregar.setObjectName("LIdAgregar")
        self.SBId2 = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.SBId2.setGeometry(QtCore.QRect(100, 490, 161, 34))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SBId2.setFont(font)
        self.SBId2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.SBId2.setMaximum(999999999)
        self.SBId2.setObjectName("SBId2")
        self.LNombreAgregar = QtWidgets.QLabel(parent=self.centralwidget)
        self.LNombreAgregar.setGeometry(QtCore.QRect(310, 490, 121, 37))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LNombreAgregar.setFont(font)
        self.LNombreAgregar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.LNombreAgregar.setObjectName("LNombreAgregar")
        self.LENombre = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.LENombre.setGeometry(QtCore.QRect(450, 490, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.LENombre.setFont(font)
        self.LENombre.setObjectName("LENombre")
        self.LNuevoId = QtWidgets.QLabel(parent=self.centralwidget)
        self.LNuevoId.setGeometry(QtCore.QRect(760, 490, 121, 37))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LNuevoId.setFont(font)
        self.LNuevoId.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.LNuevoId.setObjectName("LNuevoId")
        self.SBNuevoId = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.SBNuevoId.setGeometry(QtCore.QRect(890, 490, 161, 34))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SBNuevoId.setFont(font)
        self.SBNuevoId.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.SBNuevoId.setMaximum(999999999)
        self.SBNuevoId.setObjectName("SBNuevoId")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1097, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.TWTabla.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.TWTabla.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        self.PBEliminar.setText(_translate("MainWindow", "Eliminar"))
        self.LTitulo.setText(_translate("MainWindow", "Administración de Categorias"))
        self.PBSalir.setText(_translate("MainWindow", "Salir Categorias"))
        self.LId.setText(_translate("MainWindow", "ID"))
        self.PBTodas.setText(_translate("MainWindow", "Ver Todas"))
        self.PBBuscar.setText(_translate("MainWindow", "Buscar"))
        self.PBModificar.setText(_translate("MainWindow", "Modificar"))
        self.PBAgregar.setText(_translate("MainWindow", "Agregar"))
        self.LIdAgregar.setText(_translate("MainWindow", "ID"))
        self.LNombreAgregar.setText(_translate("MainWindow", "Nombre"))
        self.LNuevoId.setText(_translate("MainWindow", "Nuevo ID"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
