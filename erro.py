class Erro(Exception):
 
    def __init__(self, mensagem: int, linha: int):
        super().__init__('{}{}'.format(mensagem, linha))   