import socket

ip = 'localhost'
port = 8000
# define a tupla de endereco
addr = (ip, port)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# realiza a conexao
client_socket.connect(addr)

while True:
    try:
        mensagem = input('digite uma mensagem para enviar ao servidor: ')
        if mensagem == 'sair':
            client_socket.send(mensagem.encode())
            raise Exception('Sistema Finalizado')
        client_socket.send(mensagem.encode())
        print('mensagem enviada')
        mensagem_recebida = client_socket.recv(1024).decode()
        print('mensagem recebida: ' + mensagem_recebida)
        if mensagem_recebida == 'sair':
            client_socket.send(mensagem.encode())
            raise Exception('Sistema Finalizado')
    except:
        # fecha conexao
        client_socket.close()
        exit()