class Pessoa:

    """
        Instantiates a person with the data idUsuario, nome, cpf e
        data_nascimento

        Attributes
        ----------
        IdUsuario : str
            user id.
        nome : str
            Username.
        cpf : str
            User's CPF.
        data_nascimento : str
            User's date of birth.
    """

    __slots__ = ['_idUsuario', '_nome', '_cpf', '_data_nascimento']

    def __init__(self, idUsuario, nome, cpf, data_nascimento):
        self._idUsuario = idUsuario
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento

    @property
    def idUsuario(self):
        return self._idUsuario

    @idUsuario.setter
    def idUsuario(self, id):
        self._idUsuario = id

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @nome.setter
    def nome(self, data_nascimento):
        self._data_nascimento = data_nascimento