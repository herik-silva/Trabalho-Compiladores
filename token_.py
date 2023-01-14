class Token:
    # TK_IDENTIFICADOR     = 0
    # TK_NUMERO            = 1
    # TK_LITERAL           = 2
    # TK_PALAVRA_RES       = 3
    # TK_PONTUACAO         = 4 
    # TK_OPERADOR_MAT      = 5
    # TK_ATRIBUICAO        = 6
    # TK_OPERADOR_LOG      = 7
    # TK_OPERADOR_REL      = 8

    TK_STR = {0:'IDENTIFICADOR', 1:'NUMERO', 2:'LITERAL', 3:'PALAVRA RESERVADA',
                    4:'PONTUACAO', 5:'OPERADOR MATEMATICO', 6:'ATRIBUICAO', 
                        7:'OPERADOR LOGICO', 8:'OPERADOR RELACIONAL'}

    def __init__(self) -> None:
        pass

    def __init__(self, type, text) -> None:
        self._type = type
        self._text = text
    
    @property
    def type(self):
        return self._type
       
    @type.setter
    def type(self, type):
        self._type = type
    
    @property
    def text(self):
        return self._text
       
    @text.setter
    def text(self, text):
        self._text = text
    
    def __str__(self) -> str:
        return "Token<type=" + self.TK_STR[self.type] + ", text=" + self.text + ">"
    