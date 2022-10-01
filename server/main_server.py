import socket
from banco import Banco
import threading


class ClientThread(threading.Thread):
    """
        Instantiates a Thread so that the simultaneous execution of bank
        applications is possible.

        Attributes
        ---------
        clientSock : socket.socket
            connection socket to send and receive requests.
        clientAddress : str
            Connection IP address

        Methods
        -------
        run()
            initialize the thread
    """
    def __init__(self, clientSock, clientAddress):
        threading.Thread.__init__(self)
        self.clientSock = clientSock
        self.clientAddress = clientAddress

    def run(self):
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
    """
        Server class that waits for connections and when they are made,
        sends them to the threads.

        Attributes
        ----------
        host : str
            localhost to make connections.
        port : str
            Access port for making connections
        server : socket.socket
            connection socket to send and receive requests.

        Methods
        -------
        start(self)
            Run the server so that it waits for connections.

    """
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))

    def start(self):
        """
            Run the server so that it waits for connections.

            When connected, a connection is created and sent to a thread.
        """
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
    server = Server('localhost', 8000)
    server.start()
