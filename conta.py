class Conta:

    __slots__ = ['_titular', '_senha', '_saldo', '_numero', '_historico']

    def __init__(self, titular, senha, numero):
        self._titular = titular
        self._senha = senha
        self._numero = numero
        self._saldo = 0
        self._historico = []

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, titular):
        self.titular = titular

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

    def __str__(self):
        return f'Titular - {self._titular.nome}\nNúmero da conta - {self._numero}\n'
