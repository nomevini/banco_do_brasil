import hashlib


def hash(senha):
    """
    Return the password string into a Hash.

    senha : str
    """
    senha = senha.encode()
    hash = hashlib.md5(senha)
    return hash.hexdigest()
