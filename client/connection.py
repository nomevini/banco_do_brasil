import socket


def connect_server(ip, port):
    """
    Parameters
    ----------
    ip: str
        connection ip.
    port: int
        port ip.
    return : socket.socket
        returns the socket of the connection to make requests.
    """
    ip = ip
    port = port
    # define a tupla de endereco
    addr = (ip, port)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # realiza a conexao
    client_socket.connect(addr)
    return client_socket
