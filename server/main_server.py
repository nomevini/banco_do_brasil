import socket
from server.banco import Banco


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.addr = (self.host, self.port)
        self.serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serv_socket.bind(self.addr)
        self.serv_socket.listen(10)

        print('aguardando conexao')
        # servidor aguardando conexao
        self.con, self.cliente = self.serv_socket.accept()
        print('conectado')
        print('aguardando mensagem')

    def start(self):
        while True:
            banco = Banco()
            arguments = self.con.recv(1024).decode().split('*')
            # Buscando o método da requisição no banco
            if arguments:
                function = arguments.pop(0)
                if function == 'exit':
                    self.serv_socket.close()
                    exit()
                method = getattr(banco, function)
                # executando o método e passando todos os parametros que foram recebidos na requisição7
                function_return = method(*arguments)
                self.con.send(f'{function_return}'.encode())


if __name__ == "__main__":
    server = Server('localhost', 8001)
    server.start()
