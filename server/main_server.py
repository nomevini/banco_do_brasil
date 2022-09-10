import socket
from banco import Banco
import threading


class ClientThread(threading.Thread):
    def __init__(self, clientSock, clientAddress):
        threading.Thread.__init__(self)
        self.clientSock = clientSock
        self.clientAddress = clientAddress

    def run(self):
        # sacar*vinicius
        while True:
            arguments = self.clientSock.recv(1024).decode().split('*')
            # Buscando o método da requisição no banco
            if arguments:
                function = arguments.pop(0)
                if function == 'exit':
                    self.clientSock.close()
                    break
                banco = Banco()
                method = getattr(banco, function)
                # executando o método e passando todos os parametros que foram recebidos na requisição7
                function_return = method(*arguments)
                self.clientSock.send(f'{function_return}'.encode())


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))

    def start(self):
        while True:
            self.server.listen(10)
            print("Aguardando conexão...")
            # servidor aguardando conexao
            client_sock, client_address = self.server.accept()
            print(f'{client_address[0]} conectado')

            # criar thread para a conexao
            new_thread = ClientThread(client_sock, client_address)

            print("Thread iniciada")
            # iniciar a thread
            new_thread.start()


if __name__ == "__main__":
    server = Server('localhost', 8001)
    server.start()
