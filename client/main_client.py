import sys
from PyQt5 import QtWidgets
from pages.main.tela_main import Ui_main
from pages.criar_conta.tela_criar_conta import Ui_criar_conta
from pages.login.tela_login import Ui_login
from pages.dashboard.tela_dashboard import Ui_dashboard
from pages.sacar.tela_sacar import Ui_sacar
from pages.depositar.tela_depositar import Ui_depositar
from pages.tranferir.tela_transferir import Ui_tranferir
from connection import connect_server

"""
    The screen class creates all screens so that the user can
    interact and transit through it, sending and receiving requests
    that will be printed on the user's screens.
"""


class Telas:
    """
    Attributes
    ----------

    MainWindow : QtWidgets.QMainWindow
        Main screen used to add interface items.
    _cpf_conta_ativa : str
        CPF number of the active account in the application.
    client_socket : socket.socket
        Socket to send and receive server requests.
    ui_main : Ui_main
        Main application window.
    ui_criar_conta : Ui_criar_conta
        Account creation window.
    ui_login : Ui_login
        Window to log in to the application.
    ui_dashboard : Ui_dashboard
        Window with system functionalities.
    self.ui_sacar : Ui_sacar
        Window to withdraw money from the account.
    self.ui_depositar : Ui_depositar()
        Account deposit window.
    ui_tranferir : Ui_tranferir
        Window to make the transfer.

    Methods
    -------

    send_request(self, request)
        Send requests to the server.
    exit()
        end the program.
    main():
        starts the main program window.
    tela_criar_conta()
        launches the program's account creation window.
    tela_login(self):
        launches the program's login window.
    tela_dashboard(self):
        Starts the main window of the program's bank account.
    print_historico(self):
        Return an account history.
    atualizar_dados(self):
        Updates the data on the user's screen.
    tela_depositar(self):
        Launches the bank deposit screen.
    tela_transferir(self):
        Starts the bank transfer screen.
    tela_sacar(self):
        Starts the bank withdrawal screen.
    criar_conta()
        Runs the bank account creation process.
    fazer_login(self):
        Runs the bank login process.
    depositar(self)
        Executes the bank deposit process.
    sacar(self)
        runs the bank withdrawal process.
    transferir(self)
        runs the bank transfer process.
    """
    def __init__(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self._cpf_conta_ativa = ''
        # criar conex??o com o banco
        try:
            self.client_socket = connect_server('localhost', 8000)
        except ConnectionRefusedError:
            QtWidgets.QMessageBox.information(None, 'ERROR', f'N??o foi poss??vel conectar ao servidor.'
                                                             f'\nVerifique a conex??o e tente novamente')
            sys.exit()

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

        self.MainWindow.show()

    def send_request(self, request):
        """
        Send requests to the server and return the request
        sent from the server.

        parameters
        ----------
        request : str
            Request to be sent.
        Returns
        -------
            return request.
        """
        self.client_socket.send(request.encode())
        recv = self.client_socket.recv(1024)
        return recv.decode()

    def exit(self):
        """
        End the program.
        """
        self.send_request('exit')
        sys.exit()

    def main(self):
        """
            starts the main program window.
        """
        self.ui_main.setupUi(self.MainWindow)
        self.ui_main.pushButton_criar_conta.clicked.connect(self.tela_criar_conta)
        self.ui_main.pushButton_entrar.clicked.connect(self.tela_login)
        self.ui_main.pushButton_sair.clicked.connect(self.exit)

    # criar conta
    def tela_criar_conta(self):
        """
            launches the program's account creation window.
        """
        self.ui_criar_conta.setupUi(self.MainWindow)
        # botao voltar
        self.ui_criar_conta.pushButton_voltar.clicked.connect(self.main)
        # botao criar conta
        self.ui_criar_conta.pushButton_criar_conta.clicked.connect(self.criar_conta)

    # tela_login
    def tela_login(self):
        """
        launches the program's login window.
        """
        self.ui_login.setupUi(self.MainWindow)
        # botao voltar
        self.ui_login.pushButton_voltar.clicked.connect(self.main)
        # botao entrar
        self.ui_login.pushButton_entrar.clicked.connect(self.fazer_login)

    # tela_dashboard
    def tela_dashboard(self):
        """
        Starts the main window of the program's bank account.
        """
        # requisi????o para buscar as informa????es da conta ativa
        request = f'nome_titular*{self._cpf_conta_ativa}'
        nome = self.send_request(request)

        self.ui_dashboard.setupUi(self.MainWindow)
        self.atualizar_dados()
        self.ui_dashboard.label_nome_usuario.setText(f'{nome}')
        self.print_historico()

        # atualizar
        self.ui_dashboard.pushButton_atualizar.clicked.connect(self.atualizar_dados)

        # voltar
        self.ui_dashboard.pushButton_sair.clicked.connect(self.main)

        # depositar
        self.ui_dashboard.pushButton_depositar.clicked.connect(self.tela_depositar)

        # sacar
        self.ui_dashboard.pushButton_sacar.clicked.connect(self.tela_sacar)

        # tranferir
        self.ui_dashboard.pushButton_transferir.clicked.connect(self.tela_transferir)

    def print_historico(self):
        """
        Print an account history in screen.
        """
        # carregar historico
        request = f'historico_titular*{self._cpf_conta_ativa}'
        request_return = self.send_request(request).split('\n')
        if request != 'False':
            historico = []
            for x in request_return:
                historico.append(list(x.split('*')))
            historico.pop()

            # definir a quantidade de linhas necessarias
            self.ui_dashboard.tableWidget.setRowCount(len(historico))

            for index, log in enumerate(historico):
                self.ui_dashboard.tableWidget.setItem(index, 0, QtWidgets.QTableWidgetItem(log[0]))
                self.ui_dashboard.tableWidget.setItem(index, 1, QtWidgets.QTableWidgetItem(log[1]))

    def atualizar_dados(self):
        """
        Updates the data on the user's screen.
        """
        request = f'saldo_titular*{self._cpf_conta_ativa}'
        saldo = self.send_request(request)
        self.ui_dashboard.label_saldo.setText(f'Saldo R$ {round(float(saldo), 2)}')

        self.print_historico()

    # tela_depositar
    def tela_depositar(self):
        """
        Launches the bank deposit screen.
        """
        self.ui_depositar.setupUi(self.MainWindow)
        self.ui_depositar.pushButton_voltar.clicked.connect(self.tela_dashboard)
        self.ui_depositar.pushButton_depositar.clicked.connect(self.depositar)

    # tela_transferir
    def tela_transferir(self):
        """
        Starts the bank transfer screen.
        """
        self.ui_tranferir.setupUi(self.MainWindow)
        self.ui_tranferir.pushButton_voltar.clicked.connect(self.tela_dashboard)
        self.ui_tranferir.pushButton_transferir.clicked.connect(self.transferir)

    # tela_sacar
    def tela_sacar(self):
        """
        Starts the bank withdrawal screen.
        """
        self.ui_sacar.setupUi(self.MainWindow)
        self.ui_sacar.pushButton_voltar.clicked.connect(self.tela_dashboard)
        self.ui_sacar.pushButton_sacar.clicked.connect(self.sacar)

    # servidor

    @property
    def cpf_conta_ativa(self):
        return self._cpf_conta_ativa

    @cpf_conta_ativa.setter
    def cpf_conta_ativa(self, cpf):
        self._cpf_conta_ativa = cpf

    # Criar conta
    def criar_conta(self):
        """
        Runs the bank account creation process.
        """
        nome = self.ui_criar_conta.lineEdit_nome.text()
        cpf = self.ui_criar_conta.lineEdit_cpf.text()
        senha = self.ui_criar_conta.lineEdit_senha.text()
        data_nascimento = self.ui_criar_conta.dateEdit.text()
        try:
            if nome != '' and cpf != '' and senha != '':
                int(cpf)
                # requisi????o enviando os dados do usuario para criar uma conta
                request = f'criar_conta*{nome}*{cpf}*{data_nascimento}*{senha}'
                request_return = self.send_request(request)
                if len(cpf) == 11:
                    if request_return != 'False':
                        # mensagem de conta criada
                        QtWidgets.QMessageBox.information(None, 'Conta criada', request_return)
                        self.main()
                    else:
                        # n??o foi poss??vel criar
                        QtWidgets.QMessageBox.information(None, 'ERROR', f'N??o foi poss??vel criar a conta')
                else:
                    QtWidgets.QMessageBox.information(None, 'ERROR', f'O campo CPF deve conter 11 n??meros')
            else:
                QtWidgets.QMessageBox.information(None, 'ERROR', f'Nenhum campo pode ficar em branco!')
        except:
            QtWidgets.QMessageBox.information(None, 'ERROR',
                                              f'O campo CPF n??o pode conter letras ou caracteres especiais')

    # Fazer login
    # Fazer login receber?? por parametro o email e a senha digitados na parte do cliente
    def fazer_login(self):
        """
        Runs the bank login process.
        """
        cpf = self.ui_login.lineEdit_cpf.text()
        senha = self.ui_login.lineEdit_senha.text()
        request = f'login*{cpf}*{senha}'
        request_return = self.send_request(request)
        # self._conta_ativa = self.banco.login(cpf, senha)
        if request_return != 'False':
            # login permitido
            self.cpf_conta_ativa = cpf
            self.tela_dashboard()
        else:
            # acesso negado
            QtWidgets.QMessageBox.information(None, 'Acesso Negado', 'N??o foi poss??vel fazer login')

    # Depositar
    # Depositar receber?? do cliente o valor e o cpf para deposito
    def depositar(self):
        """
        Executes the bank deposit process.
        """
        valor = self.ui_depositar.lineEdit_valor.text()
        request = f'depositar*{valor}*{self._cpf_conta_ativa}'
        return_request = self.send_request(request)
        if return_request != 'False':
            # retornar para o cliente a informa????o que foi efetuado (Um True e os parametros da QtWidgets)
            QtWidgets.QMessageBox.information(None, 'Opera????o realizada', 'Deposito realizado com sucesso')
            self.tela_dashboard()
        else:
            # retornar para o cliente a informa????o se foi o n??o efetuado (False e os parametros da QtWidgets)
            QtWidgets.QMessageBox.information(None, 'ERROR', 'N??o foi poss??vel realizar o deposito\n'
                                                             'Valor invalido!')

    # Sacar
    # Sacar receber?? o valor e o cpf do titular
    def sacar(self):
        """
        runs the bank withdrawal process.
        """
        valor = self.ui_sacar.lineEdit_valor.text()
        request = f'sacar*{valor}*{self._cpf_conta_ativa}'
        return_request = self.send_request(request)
        if return_request != 'False':
            # retornar para o cliente a informa????o que foi efetuado (Um True e os parametros da QtWidgets)
            QtWidgets.QMessageBox.information(None, 'Opera????o realizada', 'Saque realizado com sucesso')
            self.tela_dashboard()
        else:
            # retornar para o cliente a informa????o que n??o foi efetuado(Um True e os parametros da QtWidgets)
            QtWidgets.QMessageBox.information(None, 'ERROR', 'N??o foi poss??vel realizar o saque')

    # Transferir
    # tranferir receber?? o valor da transferencia, o remetente e o destinatario
    def transferir(self):
        """
        runs the bank transfer process.
        """
        valor = self.ui_tranferir.lineEdit_valor.text()
        destinatario = self.ui_tranferir.lineEdit.text()
        nome_destinatario = self.send_request(f'nome_titular*{destinatario}')
        request = f'transferir*{valor}*{self._cpf_conta_ativa}*{destinatario}'
        return_request = self.send_request(request)
        if destinatario != self.cpf_conta_ativa:
            if return_request != 'False':
                # tranferencia efetuada
                # retornar para o cliente a informa????o que foi efetuado (Um True e os parametros da QtWidgets)
                QtWidgets.QMessageBox.information(None, 'Opera????o realizada',
                                                  f'Transferencia de R${valor} realizada para {nome_destinatario}')
                self.tela_dashboard()
            else:
                # retornar para o cliente a informa????o que n??o foi efetuado (Um True e os parametros da QtWidgets)
                QtWidgets.QMessageBox.information(None, 'ERROR', 'N??o foi poss??vel realizar a transfer??ncia!')
        else:
            # retornar para o cliente a informa????o que n??o foi efetuado (Um True e os parametros da QtWidgets)
            QtWidgets.QMessageBox.information(None, 'ERROR', 'N??o ?? poss??vel transferir para a mesma conta!')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    telas = Telas()
    sys.exit(app.exec_())
