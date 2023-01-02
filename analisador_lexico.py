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

    #REVISAR O COMPORTAMENTO 
    """ def __ehOperadorRelacional(self, char: chr):
        return char == '=' or char == '?' or char == '<' or char == '>'
    
    def __ehOperadorMat(self, char: chr):
        return char == '+' or char == '-' or char == '*' or char == '/' or char == '%' """
    
    def __isSpace(self, char:chr): #Rever a função
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
                elif self.__ehCharLower(char_atual):
                    cadeia += char_atual
                    self._estado = 1
                elif char_atual == "/":
                    cadeia += char_atual
                    self._estado = 8 

            elif self._estado == 1:
                if self.__ehCharLower(char_atual) or self.__ehCharUp(char_atual) or self.__ehDigito(char_atual):
                    cadeia += char_atual
                else:  
                    self._estado = 2
                    self.retrocesso()
            
            elif self._estado == 2:
                print('Token aceito: Identificador<', cadeia, '>')
                char_atual = ''
                cadeia = ''
                self._estado = 0

            elif self._estado == 3:
                if self.__ehDigito(char_atual):
                    cadeia += char_atual

                else: 
                    if not (self.__ehCharUp(char_atual) or self.__ehCharLower(char_atual)):
                       self._estado = 4
                       self.retrocesso()
                    else:
                        print('Erro estado 3, digito invalido')
                        char_atual = ''
                        cadeia = ''
                        self._estado = 0
                        
            elif self._estado == 4:
                print('Token aceito: Inteiro<', cadeia, '>')
                char_atual = ''
                cadeia = ''
                self._estado = 0
                self.retrocesso()
            
            elif self._estado == 5:
                pass
            elif self._estado == 6:
                pass
            elif self._estado == 7:
                pass
            elif self._estado == 8:
                if char_atual != '%':
                    self._estado = 18
                    self.retrocesso()
                elif char_atual == '%':
                    cadeia += char_atual
                    self._estado = 9
            elif self._estado == 9:
                if char_atual == '/':
                    cadeia += char_atual
                    self._estado = 10
            elif self._estado == 10:
                if char_atual != "\n": #Não usamos is_space porque trata todos
                    cadeia += char_atual
                else:
                    print("Comentário: ",cadeia)
                    self.retrocesso()
                    self._estado = 0

                
            elif self._estado == 18:
                print('Token aceito: <', cadeia, '>')
                char_atual = ''
                cadeia = ''
                self._estado = 0
                
                    
