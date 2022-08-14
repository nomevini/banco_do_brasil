import mysql.connector
# mysql -u root -p;


class Database:
    def __init__(self, host, usuario, senha, banco):
        self.conexao = mysql.connector.connect(host=host, user=usuario, password=senha, database=banco)
        self.cursor = self.conexao.cursor()

    def insert_users(self, nome, cpf, nascimento):
        values = (nome, cpf, nascimento)
        sql = "INSERT INTO Pessoa (nome, cpf, data_nascimento) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, values)
        self.conexao.commit()

    def insert_account(self, id_user, numeroConta, senha):
        try:
            # criar conta
            values = (senha, numeroConta, 0.00, id_user)
            sql = f"INSERT INTO Conta (senha, numeroConta, saldo, Pessoa_idUsuario) VALUES ({senha}, {numeroConta}, {0.00}, {id_user})"
            self.cursor.execute(sql)
            self.conexao.commit()
            return True
        except:
            return False

    def search_user(self, cpf):
        sql = f"SELECT * FROM Pessoa WHERE cpf={cpf}"
        self.cursor.execute(sql)
        return list(self.cursor)

    def id_user(self, cpf):
        sql = f"SELECT idUsuario FROM Pessoa WHERE cpf={cpf}"
        self.cursor.execute(sql)
        return list(self.cursor)

    def search_account(self, id_user):
        # busca todos os dados de uma conta
        sql = f"SELECT * FROM Conta WHERE Pessoa_idUsuario={id_user}"
        self.cursor.execute(sql)
        return list(self.cursor)

    def update_balance(self, id_user, new_balance):
        sql = f'UPDATE Conta SET saldo = {new_balance} WHERE Conta.Pessoa_idUsuario = {id_user}'
        self.cursor.execute(sql)
        self.conexao.commit()

    def update_historico(self, data, operacao, idConta):
        sql = f"INSERT INTO Historico (data, operacao, Conta_idConta) VALUES ('{data}', '{operacao}', {idConta})"
        self.cursor.execute(sql)
        self.conexao.commit()

    def load_user_historico(self, Conta_idConta):
        sql = f"SELECT * FROM Historico WHERE Conta_idConta={Conta_idConta}"
        self.cursor.execute(sql)
        return list(self.cursor)

    def delete_line_users_table(self):
        self.cursor.execute('DELETE FROM Usuario')

    def list_table(self, table_name):
        list = []
        self.cursor.execute(f'SELECT * FROM {table_name}')

    def close_db(self):
        self.conexao.close()
