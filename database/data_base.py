import mysql.connector
# mysql -u root -p;


class Database:
    def __init__(self, host, usuario, senha, banco):
        self.conexao = mysql.connector.connect(host=host, user=usuario, password=senha, database=banco)
        self.cursor = self.conexao.cursor()

    def create_table_users(self):
        sql = \
            'CREATE TABLE IF NOT EXISTS `cadastroPessoas`.`Usuario` ( ' \
            '`idUsuario` INT NOT NULL AUTO_INCREMENT,' \
            '`nome` VARCHAR(45) NOT NULL,' \
            '`cpf` VARCHAR(20) NOT NULL,' \
            '`endereco` VARCHAR(50) NOT NULL,' \
            '`nascimento` VARCHAR(20) NOT NULL,' \
            'PRIMARY KEY (`idUsuario`))'

        self.cursor.execute(sql)
        self.conexao.commit()

    def insert_users(self, nome, cpf, endereco, nascimento):
        values = (nome, cpf, endereco, nascimento)
        sql = "INSERT INTO Usuario (nome, cpf, endereco, nascimento) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(sql, values)
        self.conexao.commit()

    def search_user(self, cpf):
        sql = f"SELECT * FROM Usuario WHERE cpf={cpf}"
        self.cursor.execute(sql)
        return self.cursor

    def delete_line_users_table(self):
        self.cursor.execute('DELETE FROM Usuario')

    def list_table(self, table_name):
        list = []
        self.cursor.execute(f'SELECT * FROM {table_name}')

    def close_db(self):
        self.conexao.close()
