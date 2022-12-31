class Scanner:
    
    def __init__(self, path: str) -> None:
        self._pos = 0 
        self._state = 0
        file = open(path, "r")
        self._content = file.read()
        file.close()
    
    def __isDigit(self, char: chr):
        return char >= '0' and char <= '9'
    
    def __isCharUp(self, char: chr):
        return char >= 'A' and char <= 'Z'

    def __isCharLower(self, char: chr):
        return char >= 'a' and char <= 'z'

    def __isOperator(self, char: chr):
        return char == '=' or char == '?' or char == '<' or char == '>'

    def isSpace(self, char:chr):
        return char == ' ' or char == '\t' or char == '\n' or char == '\r'
        
    