class Token:
    TK_NUMBER      = 1
    TK_OPERATOR    = 2
    TK_PONCTUATION = 3
    TK_ASSIGN      = 4

    def __init__(self, type, text) -> None:
        self._type = type
        self._text = text
    
    def __init__(self) -> None:
        pass

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
        return "Token<type=" + self.type + ", text=" + self.text + ">"
    