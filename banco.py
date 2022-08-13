from pessoa import Pessoa
from conta import Conta
from datetime import datetime
from database.data_base import Database
from senha import senha


class Banco:

    __slots__ = ['_db', '_senha']
    _qtde_contas = 0
    _numero_conta = 1000

    def __init__(self):
        self._senha = senha()
        self._db = Database('localhost', 'root', f'{self._senha}', 'banco_do_brasil')

    def criar_conta(self, nome: str, cpf: str, data_nascimento: str, senha: str):
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
                    self._db.insert_account(id_user[0][0], self._numero_conta, senha)
                    Banco._numero_conta += 1
                    return True
                else:
                    print('Sai aqui')
                    return False
            else:
                # usuario já cadastrado
                return False
        except:
            return False

    def buscar_conta(self, cpf):
        try:
            user = self._db.search_user(cpf)
            if user:
                id_user, nome, cpf, data_nascimento = user[0][0], user[0][1], user[0][2], user[0][3]
                user = Pessoa(id_user, nome, cpf, data_nascimento)
                account = self._db.search_account(id_user)
                if account:
                    id_account, senha, numeroConta, saldo = account[0][0], account[0][1], account[0][2], account[0][3]
                    account = Conta(id_account, user, senha, numeroConta)
                    return account
            else:
                return False
        except:
            return False

    def login(self, cpf, senha):
        conta = self.buscar_conta(cpf)
        if conta:
            # verificar se a senha está correta
            if senha == conta.senha:
                return conta
        else:
            return False

    def sacar(self, valor, cpf, transferencia=False):
        try:
            account = self.buscar_conta(cpf)
            valor = float(valor)
            if valor <= 0:
                return False
            if valor <= account.saldo:
                account.saldo -= valor
                self._db.update_balance(account.titular.idUsuario, account.saldo)
                if not transferencia:
                    # esse processo será modificado
                    account.historico.append((str(datetime.today().date()), f'Saque R${valor}'))
                return True
            else:
                return False
        except:
            return False

    def depositar(self, valor, cpf, transferencia=False):
        try:
            valor = float(valor)
            if valor > 0:
                self._contas[cpf].saldo += valor
                if not transferencia:
                    self._contas[cpf].historico.append((str(datetime.today().date()), f'Deposito R${valor}'))
            else:
                raise ValueError
            return True
        except ValueError:
            return False

    def transferir(self, valor, cpf_remetente, cpf_destino):
        try:
            valor = float(valor)
            if self.contas[cpf_remetente].saldo >= valor:
                if cpf_destino in self._contas:
                    self.sacar(valor, cpf_remetente, True)
                    self.depositar(valor, cpf_destino, True)
                    # escrevendo no historico do remetente a transferencia
                    self._contas[cpf_remetente].historico.append((str(datetime.today().date()),
                                                                  f'Transferência para '
                                                                  f'{self._contas[cpf_destino].titular.nome} - '
                                                                  f'R${valor}'))
                    # escrevendo no historico do destinatario a transferencia
                    self._contas[cpf_destino].historico.append((str(datetime.today().date()),
                                                                  f'Transferência recebida de '
                                                                  f'{self._contas[cpf_remetente].titular.nome} - '
                                                                  f'R${valor}'))
                    return True
                else:
                    return False
            else:
                return False
        except:
            return False

    @staticmethod
    def get_qtde_contas():
        return Banco._qtde_contas

    @staticmethod
    def get_numero_contas():
        return Banco._numero_conta
