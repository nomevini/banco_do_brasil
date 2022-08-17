import hashlib


def hash(senha):
    senha = senha.encode()
    hash = hashlib.md5(senha)
    return hash.hexdigest()
