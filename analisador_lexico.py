class AnalisadorLexico:
    
    def __init__(self, path: str) -> None:
        self._palavra_reservada = ['NAO', 'E', 'OU', 'SE', 'SENAO', 'SENAOSE', 'LACO', 'LACOPARA', 'RETORNE', 'INTEIRO', 'BOOLEANO', 'CONSTANTE', 'VAZIO', 'TEXTO']
        self._pos = 0 
        self._estado = 0
        arquivo = open(path, 'r')
        self._conteudo = arquivo.read()
        arquivo.close()

    def __ehDigito(self, char: chr):
        return char >= '0' and char <= '9' 
    
    def __ehCharUp(self, char: chr):
        return char >= 'A' and char <= 'Z'

    def __ehCharLower(self, char: chr):
        return char >= 'a' and char <= 'z'

    def __ehOperadorRelacional(self, char: chr):
        return char == '=' or char == '?' or char == '<' or char == '>'
    
    def __ehOperadorMat(self, char: chr):
        return char == '+' or char == '-' or char == '*' or char == '/' or char == '%'
    
    def __isSpace(self, char:chr):
        return char == ' ' or char == '\t' or char == '\n' or char == '\r'
    
    def __isEOF(self):
        return self._pos >= len(self._conteudo)
    
    def nextChar(self):
        if self.__isEOF():
            return '\0'

        aux = self._conteudo[self._pos]
        self._pos += 1
        return aux
        
    def retrocesso(self):
        self._pos -= 1

    def token(self):
        char_atual = ''
        cadeia = ''

        while(True):
            if self.__isEOF():
                return 
             
            char_atual = self.nextChar()

            if self._estado == 0:
                if self.__ehDigito(char_atual):
                    cadeia += char_atual
                    self._estado = 3
                else:
                    print(char_atual)
            
            elif self._estado == 1:
                pass
            
            elif self._estado == 2:
                pass

            elif self._estado == 3:
                if self.__ehDigito(char_atual):
                    cadeia += char_atual

                else: 
                    if not (self.__ehCharUp(char_atual) or self.__ehCharLower(char_atual)):
                        print('Token aceito: Token<', cadeia, '>')
                        char_atual = ''
                        cadeia = ''
                        self._estado = 0
                        #Observação verificar
                        self.retrocesso()
                    else:
                        print('Erro estado 3, digito invalido')
                        return
                
