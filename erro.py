class Erro(Exception):
    def __init__(self, mensagem: str, linha: int):
        super().__init__('{}{}'.format(mensagem, linha))   

class ErroSintatico:
    def __init__(self, mensagem: str, linha: int):
        self.mensagem = mensagem
        self.linha = linha

    def __str__(self) -> str:
        return self.mensagem + ' ' + self.linha
        