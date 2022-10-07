import hashlib


def hash(senha):
    """
    senha : str

    transform the password string ontro a Hash

    returns
    -------
        Return the password Hash.
    """
    senha = senha.encode()
    hash = hashlib.md5(senha)
    return hash.hexdigest()
