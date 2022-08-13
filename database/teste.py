from conexao import criar_conexao, fechar_conexao

conexao = criar_conexao('localhost', 'root', 'Relatividade891!', 'banco_do_brasil')
cursor = conexao.cursor()
