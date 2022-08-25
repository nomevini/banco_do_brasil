
class Teste:
    def __init__(self):
       pass

    @staticmethod
    def funcao():
        print('Ola, mundo!')

    @staticmethod
    def funcao2():
        print('Ola, mundo2!')


operacao = 'funcao2'
method_to_call = getattr(Teste, operacao)
method_to_call()
