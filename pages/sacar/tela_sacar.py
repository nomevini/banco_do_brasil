from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sacar(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setPointSize(13)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("#MainWindow{\n"
"    background-color: rgb(32, 74, 135);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"    background-color: rgb(32, 74, 135);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(25, 6, 25, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_sacar = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_sacar.sizePolicy().hasHeightForWidth())
        self.label_sacar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(25)
        self.label_sacar.setFont(font)
        self.label_sacar.setStyleSheet("#label_sacar {\n"
"    color: rgb(244, 222, 30);\n"
"}")
        self.label_sacar.setObjectName("label_sacar")
        self.verticalLayout.addWidget(self.label_sacar, 0, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 55, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(20, 26, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem2)
        self.label_valor = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_valor.sizePolicy().hasHeightForWidth())
        self.label_valor.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(14)
        self.label_valor.setFont(font)
        self.label_valor.setStyleSheet("#label_valor {\n"
"    color: rgb(244, 222, 30)\n"
"}")
        self.label_valor.setObjectName("label_valor")
        self.verticalLayout_3.addWidget(self.label_valor)
        self.lineEdit_valor = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_valor.sizePolicy().hasHeightForWidth())
        self.lineEdit_valor.setSizePolicy(sizePolicy)
        self.lineEdit_valor.setMaximumSize(QtCore.QSize(16777215, 51))
        self.lineEdit_valor.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_valor.setCursorPosition(0)
        self.lineEdit_valor.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_valor.setObjectName("lineEdit_valor")
        self.verticalLayout_3.addWidget(self.lineEdit_valor)
        spacerItem3 = QtWidgets.QSpacerItem(20, 22, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_sacar = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_sacar.sizePolicy().hasHeightForWidth())
        self.pushButton_sacar.setSizePolicy(sizePolicy)
        self.pushButton_sacar.setMaximumSize(QtCore.QSize(190, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_sacar.setFont(font)
        self.pushButton_sacar.setStyleSheet("#pushButton_sacar {\n"
"    border-radius: 20px;\n"
"    background-color: rgb(244, 222, 30);\n"
"    color: rgb(20, 34, 143)\n"
"}")
        self.pushButton_sacar.setObjectName("pushButton_sacar")
        self.horizontalLayout_2.addWidget(self.pushButton_sacar)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 120, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem4)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        spacerItem5 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalFrame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalFrame_2.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_2.setSizePolicy(sizePolicy)
        self.horizontalFrame_2.setMaximumSize(QtCore.QSize(16777215, 83))
        self.horizontalFrame_2.setObjectName("horizontalFrame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_voltar = QtWidgets.QPushButton(self.horizontalFrame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_voltar.sizePolicy().hasHeightForWidth())
        self.pushButton_voltar.setSizePolicy(sizePolicy)
        self.pushButton_voltar.setMaximumSize(QtCore.QSize(190, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(14)
        self.pushButton_voltar.setFont(font)
        self.pushButton_voltar.setStyleSheet("#pushButton_voltar {\n"
"    border-radius: 20px;\n"
"    background-color: rgb(244, 222, 30);\n"
"    color: rgb(20, 34, 143)\n"
"}")
        self.pushButton_voltar.setObjectName("pushButton_voltar")
        self.horizontalLayout_3.addWidget(self.pushButton_voltar)
        self.verticalLayout.addWidget(self.horizontalFrame_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_sacar.setText(_translate("MainWindow", "Sacar"))
        self.label_valor.setText(_translate("MainWindow", "Valor"))
        self.pushButton_sacar.setText(_translate("MainWindow", "Sacar"))
        self.pushButton_voltar.setText(_translate("MainWindow", "voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_sacar()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

