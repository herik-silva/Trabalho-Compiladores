# Tipos de Token
TK_IDENTIFICADOR     = 0
TK_NUMERO            = 1
TK_LITERAL           = 2
TK_PALAVRA_RES       = 3
TK_SIMB_ESP          = 4 
TK_OPERADOR_MAT      = 5
TK_ATRIBUICAO        = 6
TK_BOOLEANO          = 7
TK_OPERADOR_LOG      = 8
TK_OPERADOR_REL      = 9
TK_STR = {
        0:'IDENTIFICADOR', 
        1:'NUMERO', 
        2:'LITERAL', 
        3:'PALAVRA RESERVADA',
        4:'PONTUACAO', 
        5:'OPERADOR MATEMATICO', 
        6:'ATRIBUICAO', 
        7:'BOOLEANO',
        8:'OPERADOR LOGICO', 
        9:'OPERADOR RELACIONAL'
    }
class Token:

    def __init__(self, tipo, texto, linha) -> None:
        self._tipo = tipo
        self._texto = texto
        self.linha = linha
    
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
        return "Token<tipo=" + TK_STR[self.tipo] + ", texto=" + self.texto + ">"
    