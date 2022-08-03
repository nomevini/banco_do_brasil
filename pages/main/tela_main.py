# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_main(object):
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"    background-color: rgb(32, 74, 135);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(-1, 50, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalFrame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalFrame.sizePolicy().hasHeightForWidth())
        self.horizontalFrame.setSizePolicy(sizePolicy)
        self.horizontalFrame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_banco = QtWidgets.QLabel(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_banco.sizePolicy().hasHeightForWidth())
        self.label_banco.setSizePolicy(sizePolicy)
        self.label_banco.setMaximumSize(QtCore.QSize(350, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_banco.setFont(font)
        self.label_banco.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_banco.setStyleSheet("#label_banco {\n"
"    color: rgb(244, 222, 30);\n"
"}")
        self.label_banco.setAlignment(QtCore.Qt.AlignCenter)
        self.label_banco.setObjectName("label_banco")
        self.horizontalLayout.addWidget(self.label_banco)
        self.verticalLayout_2.addWidget(self.horizontalFrame, 0, QtCore.Qt.AlignTop)
        self.vertical_frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vertical_frame.sizePolicy().hasHeightForWidth())
        self.vertical_frame.setSizePolicy(sizePolicy)
        self.vertical_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.vertical_frame.setMaximumSize(QtCore.QSize(16777215, 300))
        self.vertical_frame.setObjectName("vertical_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.vertical_frame)
        self.verticalLayout.setContentsMargins(175, 1, 175, 1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.vertical_frame_buttons = QtWidgets.QFrame(self.vertical_frame)
        self.vertical_frame_buttons.setObjectName("vertical_frame_buttons")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.vertical_frame_buttons)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_3.setContentsMargins(120, 1, 110, 10)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_entrar = QtWidgets.QPushButton(self.vertical_frame_buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_entrar.sizePolicy().hasHeightForWidth())
        self.pushButton_entrar.setSizePolicy(sizePolicy)
        self.pushButton_entrar.setMaximumSize(QtCore.QSize(190, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(14)
        self.pushButton_entrar.setFont(font)
        self.pushButton_entrar.setStyleSheet("#pushButton_entrar {\n"
"    border-radius: 20px;\n"
"    background-color: rgb(244, 222, 30);\n"
"    color: rgb(20, 34, 143)\n"
"}")
        self.pushButton_entrar.setObjectName("pushButton_entrar")
        self.verticalLayout_3.addWidget(self.pushButton_entrar)
        self.pushButton_criar_conta = QtWidgets.QPushButton(self.vertical_frame_buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_criar_conta.sizePolicy().hasHeightForWidth())
        self.pushButton_criar_conta.setSizePolicy(sizePolicy)
        self.pushButton_criar_conta.setMaximumSize(QtCore.QSize(190, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(14)
        self.pushButton_criar_conta.setFont(font)
        self.pushButton_criar_conta.setStyleSheet("#pushButton_criar_conta {\n"
"    border-radius: 20px;\n"
"    background-color: rgb(244, 222, 30);\n"
"    color: rgb(20, 34, 143)\n"
"}")
        self.pushButton_criar_conta.setObjectName("pushButton_criar_conta")
        self.verticalLayout_3.addWidget(self.pushButton_criar_conta)
        self.verticalLayout.addWidget(self.vertical_frame_buttons)
        self.horizontalFrame1 = QtWidgets.QFrame(self.vertical_frame)
        self.horizontalFrame1.setObjectName("horizontalFrame1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalFrame1)
        self.horizontalLayout_2.setContentsMargins(-1, 1, -1, -1)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_sair = QtWidgets.QPushButton(self.horizontalFrame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_sair.sizePolicy().hasHeightForWidth())
        self.pushButton_sair.setSizePolicy(sizePolicy)
        self.pushButton_sair.setMaximumSize(QtCore.QSize(190, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(14)
        self.pushButton_sair.setFont(font)
        self.pushButton_sair.setStyleSheet("#pushButton_sair {\n"
"    border-radius: 20px;\n"
"    background-color: rgb(244, 222, 30);\n"
"    color: rgb(20, 34, 143)\n"
"}")
        self.pushButton_sair.setObjectName("pushButton_sair")
        self.horizontalLayout_2.addWidget(self.pushButton_sair)
        self.verticalLayout.addWidget(self.horizontalFrame1)
        self.verticalLayout_2.addWidget(self.vertical_frame)
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
        self.label_banco.setText(_translate("MainWindow", "Banco do Brasil"))
        self.pushButton_entrar.setText(_translate("MainWindow", "Entrar"))
        self.pushButton_criar_conta.setText(_translate("MainWindow", "Criar Conta"))
        self.pushButton_sair.setText(_translate("MainWindow", "Fechar o programa"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_main()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

