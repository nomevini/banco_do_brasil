import mysql.connector
# mysql -u root -p;

"""
    This file contains methods for connecting and manipulating 
    MySQL databases.
"""


class Database:
    """
    Class used to manipulate databases.

    Attributes
    ----------
    conexao : mysql.connector
    cursor : mysql.connector.cursor.MySQLCursor

    """
    def __init__(self, host, usuario, senha, banco):
        """

        Parameters
        ----------
        host : str
            database host.
        usuario : str
            user with access to the database.
        senha : str
            database password.
        banco : str
            database name.
        """
        self.conexao = mysql.connector.connect(host=host, user=usuario, password=senha, database=banco,
                                               auth_plugin='mysql_native_password')
        self.cursor = self.conexao.cursor()

    def insert_users(self, nome, cpf, nascimento):
        """
        Insert users into the database.

        nome : str
            username to be added.
        cpf : str
            CPF that will be added.
        nascimento : str
            birth date of the user that will be added.
        """
        values = (nome, cpf, nascimento)
        sql = "INSERT INTO Pessoa (nome, cpf, data_nascimento) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, values)
        self.conexao.commit()

    def insert_account(self, id_user, numeroConta, senha):
        """
        Insert an account into the database.

        id_user :
            Account user id.
        numeroConta :
            Account number.
        senha :
            Password;
        """
        try:
            # criar conta
            sql = f"INSERT INTO Conta (senha, numeroConta, saldo, Pessoa_idUsuario) VALUES (MD5({senha}), " \
                  f"{numeroConta}, {0.00}, {id_user})"
            self.cursor.execute(sql)
            self.conexao.commit()
            return True
        except:
            return False

    def search_user(self, cpf):
        """
        Search for a user in the database.

        cpf : str
            identifier code of the user you want to search.
        """
        sql = f"SELECT * FROM Pessoa WHERE cpf={cpf}"
        self.cursor.execute(sql)
        return list(self.cursor)

    def id_user(self, cpf):
        """
        Searches the user id in the database table through the unique
        identifier CPF.

        cpf : str
            identifier code of the user you want to search.

        """
        sql = f"SELECT idUsuario FROM Pessoa WHERE cpf={cpf}"
        self.cursor.execute(sql)
        return list(self.cursor)

    def search_account(self, id_user):
        """
        Search for an account in the database by the user id.

        id_user : str
            Person table identifier for each user.
        """

        # busca todos os dados de uma conta
        sql = f"SELECT * FROM Conta WHERE Pessoa_idUsuario={id_user}"
        self.cursor.execute(sql)
        return list(self.cursor)

    def update_balance(self, id_user, new_balance):
        """
        Updates the account balance amount in the database.

        id_user: str
            Person table identifier for each user.
        new_balance: Float
            New user account value.
        """
        sql = f'UPDATE Conta SET saldo = {new_balance} WHERE Conta.Pessoa_idUsuario = {id_user}'
        self.cursor.execute(sql)
        self.conexao.commit()

    def update_historico(self, data, operacao, idConta):
        """
        Adds transactions made to the account history.

        data : Date
            Date of completion of the transaction.
        operacao : str
            What type of transaction was performed.
        idConta : str
            The id in the cotna table that performed the transaction
        """
        sql = f"INSERT INTO Historico (data, operacao, Conta_idConta) VALUES ('{data}', '{operacao}', {idConta})"
        self.cursor.execute(sql)
        self.conexao.commit()

    def load_user_historico(self, Conta_idConta):
        """
        Returns the history of an account.

        Conta_idConta:
            Id of the account that you want to access the history.
        """
        sql = f"SELECT * FROM Historico WHERE Conta_idConta={Conta_idConta}"
        self.cursor.execute(sql)
        return list(self.cursor)

    def delete_line_users_table(self):
        """
        Deletes the User table.
        """
        self.cursor.execute('DELETE FROM Usuario')

    def list_table(self, table_name):
        """
        Prints all data in a table.

        table_name:
            name of the table you want to print its values.
        """
        self.cursor.execute(f'SELECT * FROM {table_name}')

    def close_db(self):
        """
        Close the conection with database.
        """
        self.conexao.close()
