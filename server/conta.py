class Conta:

    """
    This class creates a bank account with all the account
    data holder data, such as password, number, balance and history.

    Attributes
    ----------
    __slots__ : list
        Defines all attributes that can be created in the class.

     idConta : int
        Bank account identification.
     titular : str
        Name of the account holder.
     senha : str
        Account access password.
     numero : str
        Bank account number.
     saldo: Float
        Account balance.
     historico : str
        bank transaction history.

    Methods
    -------

    formatar_historico_string()
        formats in a string all the operations performed that are
        stored in the history.
    """

    __slots__ = ['_idConta', '_titular', '_senha', '_saldo', '_numero', '_historico']

    def __init__(self, idConta, titular, senha, numero, saldo=0, historico=None):
        self._idConta = idConta
        self._titular = titular
        self._senha = senha
        self._numero = numero
        self._saldo = saldo
        self._historico = historico

    @property
    def idConta(self):
        return self._idConta

    @idConta.setter
    def idConta(self, id):
        self._idConta = id

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, titular):
        self._titular = titular

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, senha):
        self._senha = senha

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    @property
    def historico(self):
        return self._historico

    @historico.setter
    def historico(self, historico):
        self._historico = historico

    def formatar_historico_string(self):
        string = ''
        for operacao in self.historico:
            string += f'{operacao[0]}*{operacao[1]}*{operacao[2]}\n'

    def __str__(self):
        return f'Titular - {self._titular.nome}\nNúmero da conta - {self._numero}\n'
