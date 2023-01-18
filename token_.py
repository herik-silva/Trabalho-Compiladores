from enum_token import TokenEnum

class Token:

    def __init__(self, tipo: TokenEnum, texto: str, linha: int) -> None:
        self._tipo = tipo
        self._texto = texto
        self._linha = linha
    
    @property
    def tipo(self):
        return self._tipo
       
    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo
    
    @property
    def texto(self):
        return self._texto
       
    @texto.setter
    def texto(self, texto):
        self._texto = texto
    
    @property
    def linha(self):
        return self._linha
       
    @linha.setter
    def linha(self, linha):
        self._linha = linha
    
    def __str__(self) -> str:
        return "Token<tipo=" + str(self.tipo) + ", texto=" + self.texto + ">" 
    