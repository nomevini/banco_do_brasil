import sys
from PyQt5 import QtWidgets
from tela_main import Ui_main
from pages.criar_conta.tela_criar_conta import Ui_criar_conta
from pages.login.tela_login import Ui_login
from pages.dashboard.tela_dashboard import Ui_dashboard
from pages.sacar.tela_sacar import Ui_sacar
from pages.depositar.tela_depositar import Ui_depositar
from pages.tranferir.tela_transferir import Ui_tranferir
from banco import Banco

# tratamentos necessários ->  o campo cpf só pode conter números

class Telas:
    def __init__(self):
        self.MainWindow = QtWidgets.QMainWindow()

        self.banco = Banco()

        # main
        self.ui_main = Ui_main()
        self.main()

        # criar_conta
        self.ui_criar_conta = Ui_criar_conta()

        # login
        self.ui_login = Ui_login()

        # dashboard
        self.ui_dashboard = Ui_dashboard()

        # sacar
        self.ui_sacar = Ui_sacar()

        # depositar
        self.ui_depositar = Ui_depositar()

        # transferir
        self.ui_tranferir = Ui_tranferir()

        self._conta_ativa = None

        self.MainWindow.show()

    @property
    def conta_ativa(self):
        return self._conta_ativa

    def exit(self):
        sys.exit()

    def main(self):
        self.ui_main.setupUi(self.MainWindow)
        self.ui_main.pushButton_criar_conta.clicked.connect(self.tela_criar_conta)
        self.ui_main.pushButton_entrar.clicked.connect(self.tela_login)
        self.ui_main.pushButton_sair.clicked.connect(self.exit)

    # criar conta
    def tela_criar_conta(self):
        self.ui_criar_conta.setupUi(self.MainWindow)
        # botao voltar
        self.ui_criar_conta.pushButton_voltar.clicked.connect(self.main)
        # botao criar conta
        self.ui_criar_conta.pushButton_criar_conta.clicked.connect(self.criar_conta)

    def criar_conta(self):
        nome = self.ui_criar_conta.lineEdit_nome.text()
        cpf = self.ui_criar_conta.lineEdit_cpf.text()
        senha = self.ui_criar_conta.lineEdit_senha.text()
        data_nascimento = self.ui_criar_conta.dateEdit.text()
        try:
            int(cpf)
            if nome != '' and cpf != '' and senha != '':
                if self.banco.criar_conta(nome, cpf, data_nascimento, senha):
                    # mensagem de conta criada
                    if len(cpf) == 11:
                        QtWidgets.QMessageBox.information(None, 'Conta criada', f'{self.banco.buscar_conta(cpf)}')
                        self.main()
                    else:
                        QtWidgets.QMessageBox.information(None, 'ERROR', f'O campo CPF deve conter 11 números')
                else:
                    # não foi possível criar
                    QtWidgets.QMessageBox.information(None, 'ERROR', f'Não foi possível criar a conta')
            else:
                QtWidgets.QMessageBox.information(None, 'ERROR', f'Nenhum campo pode ficar em branco!')
        except:
            QtWidgets.QMessageBox.information(None, 'ERROR', f'O campo CPF não pode conter letras')

    # login
    def tela_login(self):
        self.ui_login.setupUi(self.MainWindow)
        # botao voltar
        self.ui_login.pushButton_voltar.clicked.connect(self.main)
        # botao entrar
        self.ui_login.pushButton_entrar.clicked.connect(self.fazer_login)

    def fazer_login(self):
        cpf = self.ui_login.lineEdit_cpf.text()
        senha = self.ui_login.lineEdit_senha.text()
        self._conta_ativa = self.banco.login(cpf, senha)
        if self.conta_ativa:
            # login permitido
            self.tela_dashboard()
        else:
            # acesso negado
            QtWidgets.QMessageBox.information(None, 'Acesso Negado', 'Não foi possível fazer login')

    def tela_dashboard(self):
        self.ui_dashboard.setupUi(self.MainWindow)
        self.ui_dashboard.label_saldo.setText(f'Saldo R$ {round(self.conta_ativa.saldo, 2)}')
        self.ui_dashboard.label_nome_usuario.setText(f'{self.conta_ativa.titular.nome}')

        # carregar historico
        # definir a quantidade de linhas necessarias
        self.ui_dashboard.tableWidget.setRowCount(len(self.conta_ativa.historico))

        for index, tupla_dados in enumerate(self.conta_ativa.historico):
            self.ui_dashboard.tableWidget.setItem(index, 0, QtWidgets.QTableWidgetItem(tupla_dados[0]))
            self.ui_dashboard.tableWidget.setItem(index, 1, QtWidgets.QTableWidgetItem(tupla_dados[1]))

        # voltar
        self.ui_dashboard.pushButton_sair.clicked.connect(self.main)

        # depositar
        self.ui_dashboard.pushButton_depositar.clicked.connect(self.tela_depositar)

        # sacar
        self.ui_dashboard.pushButton_sacar.clicked.connect(self.tela_sacar)

        # tranferir
        self.ui_dashboard.pushButton_transferir.clicked.connect(self.tela_transferir)

    def tela_depositar(self):
        self.ui_depositar.setupUi(self.MainWindow)
        self.ui_depositar.pushButton_voltar.clicked.connect(self.tela_dashboard)
        self.ui_depositar.pushButton_depositar.clicked.connect(self.depositar)

    def depositar(self):
        valor = self.ui_depositar.lineEdit_valor.text()
        if self.banco.depositar(valor, self.conta_ativa.titular.cpf):
            QtWidgets.QMessageBox.information(None, 'Operação realizada', 'Deposito realizado com sucesso')
            self.tela_dashboard()
        else:
            QtWidgets.QMessageBox.information(None, 'ERROR', 'Não foi possível realizar o deposito\n'
                                                             'Valor invalido!')

    def tela_sacar(self):
        self.ui_sacar.setupUi(self.MainWindow)
        self.ui_sacar.pushButton_voltar.clicked.connect(self.tela_dashboard)
        self.ui_sacar.pushButton_sacar.clicked.connect(self.sacar)

    def sacar(self):
        valor = self.ui_sacar.lineEdit_valor.text()
        if self.banco.sacar(valor, self.conta_ativa.titular.cpf):
            QtWidgets.QMessageBox.information(None, 'Operação realizada', 'Saque realizado com sucesso')
            self.tela_dashboard()
        else:
            QtWidgets.QMessageBox.information(None, 'ERROR', 'Não foi possível realizar o saque')

    def tela_transferir(self):
        self.ui_tranferir.setupUi(self.MainWindow)
        self.ui_tranferir.pushButton_voltar.clicked.connect(self.tela_dashboard)
        self.ui_tranferir.pushButton_transferir.clicked.connect(self.transferir)

    def transferir(self):
        valor = self.ui_tranferir.lineEdit_valor.text()
        destinatario = self.ui_tranferir.lineEdit.text()
        if destinatario != self.conta_ativa.titular.cpf:
            if self.banco.transferir(valor, self.conta_ativa.titular.cpf, destinatario):
                # tranferencia efetuada
                QtWidgets.QMessageBox.information(None, 'Operação realizada', f'Transferencia de R${valor} realizada para {self.banco.contas[destinatario].titular.nome}')
                self.tela_dashboard()
            else:
                QtWidgets.QMessageBox.information(None, 'ERROR', 'Não foi possível realizar a transferência!')
        else:
            QtWidgets.QMessageBox.information(None, 'ERROR', 'Não é possível transferir para a mesma conta!')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    telas = Telas()
    sys.exit(app.exec_())
