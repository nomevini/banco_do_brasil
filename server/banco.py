from pessoa import Pessoa
from conta import Conta
from datetime import datetime
from database.data_base import Database
from database.senha import senha
from hash.hash import hash
import threading


class Banco:
    """
        The Bank class instantiates a Bank object capable of accessing a
        database to record and retrieve bank account data, in addition to
        performing financial transactions such as withdrawals, deposits and
        transfers.

        Attributes
        ----------
        __slots__ : list
            Defines all attributes that can be created in the class.
        _qtde_contas : int
            Stores the number of accounts the bank has.
        _numero_conta : int
            Represents the number of the next bank account that will be
            created and is incremented whenever a new account is created.
        _senha : str
            Stores the database access password.
        _db :
            Stores an instance of the Database class that has the operations
            that can be performed in the database.
        _sinc_thread : threading.Lock
            controls simultaneous access of threads.

        Methods
        -------
        transferir(valor, cpf_remetente, cpf_destino)
            Makes the transfer of value from the sender account to the destination account.
        depositar(valor, cpf, transferencia=False)
            Deposit the amount into your bank account.
        depositar(valor, cpf, transferencia=False)
            Deposit the amount into your bank account.
        sacar(valor, cpf, transferencia=False)
            Withdraw from a bank account.
        login(*args)
            Checks if the data entered by the user corresponds
            to an account and returns the user's CPF if the account exists.
        buscar_conta(cpf)
            Search a user's account in the database through the CPF.
        criar_conta(nome: str, cpf: str, data_nascimento: str, senha: str)
            check if there is already an account with that CPF, if not,
            create the account.
        historico_titular(*args)
            Returns a string with the history of all transactions
            carried out on the account.
        saldo_titular(*args)
            Returns the user's balance
        nome_titular(*args)
            Returns the username of an account.

    """

    __slots__ = ['_db', '_senha', '_sinc_thread']
    _qtde_contas = 0
    _numero_conta = 1000

    def __init__(self):
        self._senha = senha()
        self._db = Database('localhost', 'root', f'{self._senha}', 'banco_do_brasil')
        self._sinc_thread = threading.Lock()

    def nome_titular(self, *args):
        """
        Returns the username of an account.

        args: list
            list of parameters necessary to search for the name of
            the account holder.
        """
        try:
            cpf = args[0]
            conta = self.buscar_conta(cpf)
            if conta:
                return f'{conta.titular.nome}'
            else:
                return False
        except AttributeError:
            return False

    def saldo_titular(self, *args):
        """
        Returns the user's balance
        args: list
            list of parameters needed to search for the account
            holder's balance.
        """
        cpf = args[0]
        conta = self.buscar_conta(cpf)
        return f'{conta.saldo}'

    def historico_titular(self, *args):
        """
        Returns a string with the history of all transactions
        carried out on the account.

        args : list
              list of necessary parameters to search the account
              holder's history.
        """
        string = ''
        cpf = args[0]
        conta = self.buscar_conta(cpf)
        for operacao in conta.historico:
            string += f'{operacao[1]}*{operacao[2]}\n'
        if string:
            return string
        else:
            return False

    def criar_conta(self, nome: str, cpf: str, data_nascimento: str, senha: str):
        """
        check if there is already an account with that CPF, if not,
        create the account.

        nome : str
            Name of the account holder.
        cpf : str
            Account holder's CPF.
        data_nascimento : str
            Account holder's date of birth.
        senha : str
            Account access password.
        """
        # criar pessoa
        # query para verificar se existe aquela conta no banco
        try:
            user = self._db.search_user(cpf)
            if not user:
                # cadastrar conta e o usuario
                self._db.insert_users(nome, cpf, data_nascimento)
                # buscar o idUsuario da pessoa
                id_user = self._db.id_user(cpf)
                if id_user:
                    # criar a conta dessa pessoa e associar a ela
                    self._sinc_thread.acquire()
                    self._db.insert_account(id_user[0][0], self._numero_conta, senha)
                    self._sinc_thread.release()
                    Banco._numero_conta += 1
                    return f'Titular - {nome}\nNúmero da conta - {self._numero_conta}\n'
                else:
                    return False
            else:
                # usuario já cadastrado
                return False
        except:
            return False

    def buscar_conta(self, cpf):
        """
            Search a user's account in the database through the CPF.
        cpf : str
            Account holder's CPF.
        """
        try:
            user = self._db.search_user(cpf)
            if user:
                id_user, nome, cpf, data_nascimento = user[0][0], user[0][1], user[0][2], user[0][3]
                user = Pessoa(id_user, nome, cpf, data_nascimento)
                # buscar conta
                account = self._db.search_account(id_user)
                if account:
                    id_account, senha, numeroConta, saldo = account[0][0], account[0][1], account[0][2], account[0][3]

                    # buscar historico da conta
                    historico = self._db.load_user_historico(id_account)
                    account = Conta(id_account, user, senha, numeroConta, saldo, historico)
                    return account
                else:
                    return False
            else:
                return False
        except:
            return False

    def login(self, *args):
        """
        Checks if the data entered by the user corresponds
        to an account and returns the user's CPF if the account exists.

        args : list
            list containing the CPF and password to log in to the account.
        """
        cpf, senha = args
        conta = self.buscar_conta(cpf)
        senha_hash = hash(senha)
        if conta:
            # verificar se a senha está correta
            if senha_hash == conta.senha:
                return f'{cpf}'
        else:
            return False

    def sacar(self, valor, cpf, transferencia=False):
        """
        Withdraw from a bank account.

        valor: str
            Value to be withdrawn.
        cpf: str
            CPF of the account holder to carry out the transaction.
        transferencia: Boolean
            Boolean value to idenfy whether the transaction refers to
            a withdrawal or a transfer, since the withdrawal function is
            used in the transfer process as well.
        """
        try:
            account = self.buscar_conta(cpf)
            valor = float(valor)
            if valor <= 0:
                return False
            if valor <= account.saldo:
                account.saldo -= valor
                self._sinc_thread.acquire()
                self._db.update_balance(account.titular.idUsuario, account.saldo)
                self._sinc_thread.release()
                if not transferencia:
                    data = datetime.today().date()
                    self._db.update_historico(f'{data}', f'Saque R${valor}', account.idConta)
                return True
            else:
                return False
        except:
            return False

    def depositar(self, valor, cpf, transferencia=False):
        """
        Deposit the amount into your bank account.

        valor : str
            Amount to be deposited.
        cpf : str
            Account holder's CPF.
        transferencia: Boolean
            Boolean value to identify whether the transaction refers
            to a deposit or a transfer, as the deposit function is used
            in the transfer process as well.
        """
        try:
            account = self.buscar_conta(cpf)
            valor = float(valor)
            if valor > 0:
                account.saldo += valor
                self._sinc_thread.acquire()
                self._db.update_balance(account.titular.idUsuario, account.saldo)
                self._sinc_thread.release()
                if not transferencia:
                    data = datetime.today().date()
                    self._db.update_historico(f'{data}', f'Deposito R${valor}', account.idConta)
            else:
                return False
            return True
        except ValueError:
            return False

    def transferir(self, valor, cpf_remetente, cpf_destino):
        """
        Makes the transfer of value from the sender account to the destination account.

        valor : Float
            transfer value
        cpf_remetente : str
            CPF of the sender account holder.
        cpf_destino: str
            CPF of the target account holder.
        """
        try:
            conta_remetente = self.buscar_conta(cpf_remetente)
            conta_destino = self.buscar_conta(cpf_destino)
            valor = float(valor)
            if valor > 0:
                if conta_remetente.saldo >= valor:
                    if conta_destino:
                        self._sinc_thread.acquire()
                        self.sacar(valor, cpf_remetente, True)
                        self.depositar(valor, cpf_destino, True)
                        data = datetime.today().date()

                        # escrevendo no historico do remetente a transferencia

                        self._db.update_historico(f'{data}', f'Transferencia de R${valor} para '
                                                             f'{conta_destino.titular.nome}', conta_remetente.idConta)
                        self._db.update_historico(f'{data}', f'Transferencia de R${valor} recebida de '
                                                             f'{conta_remetente.titular.nome}', conta_destino.idConta)
                        self._sinc_thread.release()
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        except:
            return False

    @staticmethod
    def get_qtde_contas():
        """
        returns the number of accounts present in the bank.
        """
        return Banco._qtde_contas

    @staticmethod
    def get_numero_contas():
        """
        Returns the account number of the next account to be created
        """
        return Banco._numero_conta
