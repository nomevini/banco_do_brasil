import socket

# 10.180.41.142
host = 'localhost'
port = 8000
addr = (host, port)
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.bind(addr)
serv_socket.listen(10)
print('aguardando conexao')
con, cliente = serv_socket.accept() # servidor aguardando conexao
print('conectado')
print('aguardando mensagem')

while True:
    try:
        recebe = con.recv(1024) # define que os pacotes recebidos no maximo com 1024 bytes
        recebe = recebe.decode()
        print('mensagem recebida: ' + recebe)
        if recebe == 'exit':
            con.send('exit'.encode())
            raise Exception('Sistema Finalizado')
        else:
            enviar = input('digite uma mensagem para enviar ao cliente: ')
            if enviar == 'exit':
                con.send(enviar.encode())
                raise Exception('Sistema Finalizado')
            else:
                con.send(enviar.encode())
                print('Mensagem enviada')
    except:
        serv_socket.close()
        exit()