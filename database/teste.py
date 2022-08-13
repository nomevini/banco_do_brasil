from conexao import criar_conexao, fechar_conexao

conexao = criar_conexao('localhost', 'root', 'Relatividade891!', 'banco_do_brasil')
cursor = conexao.cursor()


def search_user(cpf):
    sql = f"SELECT * FROM Pessoa WHERE cpf={cpf}"
    cursor.execute(sql)
    return list(cursor)

def search_user2(cpf):
    sql = f"SELECT * FROM Pessoa WHERE cpf={cpf}"
    cursor.execute(sql)
    if list(cursor):
        return list(cursor)[0]
    else:
        return False

def search_account(id_user):
    # busca todos os dados de uma conta
    sql = f"SELECT * FROM Conta WHERE Pessoa_idUsuario={id_user}"
    cursor.execute(sql)
    return list(cursor)


def insert_users(nome, cpf, nascimento):
    values = (nome, cpf, nascimento)
    sql = f"INSERT INTO Pessoa (nome, cpf, data_nascimento) VALUES (%s, %s, %s)"
    cursor.execute(sql, values)
    conexao.commit()


def insert_account(id_user, numeroConta, senha):
    try:
        # criar conta
        values = (senha, numeroConta, 0.00, id_user)
        sql = f"INSERT INTO Conta (senha, numeroConta, saldo, Pessoa_idUsuario) VALUES ({senha}, {numeroConta}, {0.00}, {id_user})"
        cursor.execute(sql)
        conexao.commit()
        print('cheguei')
        return True
    except:
        return False


# insert_users('vinicius', '06616540368', '29-01-2002')
insert_account(3, '0027', '1030')

def id_user(cpf):
    sql = f"SELECT idUsuario FROM Pessoa WHERE cpf={cpf}"
    cursor.execute(sql)
    return list(cursor)

