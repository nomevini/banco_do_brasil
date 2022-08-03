from pessoa import Pessoa
from conta import Conta
from datetime import datetime

class Banco:

    __slots__ = ['_contas']
    _qtde_contas = 0
    _numero_conta = 1000

    def __init__(self):
        self._contas = {}

    @property
    def contas(self):
        return self._contas

    def criar_conta(self, nome: str, cpf: str, data_nascimento: str, senha: str):
        # criar pessoa
        try:
            if cpf not in self._contas:
                pessoa = Pessoa(nome, cpf, data_nascimento)
                conta = Conta(pessoa, senha, Banco._numero_conta)
                Banco._qtde_contas += 1
                self._contas[cpf] = conta
                Banco._numero_conta += 1
                return True
            else:
                return False
        except:
            return False

    def buscar_conta(self, cpf):
        if cpf in self._contas:
            return self._contas[cpf]
        else:
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
            valor = float(valor)
            if valor <= 0:
                return False
            if valor <= self._contas[cpf].saldo:
                self._contas[cpf].saldo -= valor
                if not transferencia:
                    self._contas[cpf].historico.append((str(datetime.today().date()), f'Saque R${valor}'))
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
