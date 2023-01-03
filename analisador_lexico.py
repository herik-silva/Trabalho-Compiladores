class AnalisadorLexico:
    
    def __init__(self, path: str) -> None:
        self._palavra_reservada = ['NAO', 'E', 'OU', 'SE', 'SENAO', 'SENAOSE', 'LACO', 'LACOPARA', 'RETORNE', 'INTEIRO', 'BOOLEANO', 'CONSTANTE', 'VAZIO', 'TEXTO']
        self._pos = 0 
        self._estado = 0
        self.char_atual = ''
        self.cadeia = ''
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
    
    def __isSpace(self, char: chr): #Rever a função
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

    def estadoFinal(self, tipoReconhecido: str):
            """Reinicia os atributos e exibe o Token aceito"""
            print('Token aceito: ', tipoReconhecido, '<', self.cadeia, '>')
            self.char_atual = ''
            self.cadeia = ''
            self._estado = 0

    def token(self):
        while(True):
            if self.__isEOF():
                return 
             
            self.char_atual = self.nextChar()
            if self._estado == 0:
                if self.__ehDigito(self.char_atual):
                    self.cadeia += self.char_atual
                    self._estado = 3
                elif self.__ehCharLower(self.char_atual):
                    self.cadeia += self.char_atual
                    self._estado = 1
                elif self.char_atual == "/":
                    self.cadeia += self.char_atual
                    self._estado = 8
                elif self.char_atual == '"':
                    self.cadeia += self.char_atual
                    self._estado = 5
                    print("INICIO DA PALAVRA")

            elif self._estado == 1:
                if self.__ehCharLower(self.char_atual) or self.__ehCharUp(self.char_atual) or self.__ehDigito(self.char_atual):
                    self.cadeia += self.char_atual
                else:  
                    self._estado = 2
                    self.retrocesso()
            
            elif self._estado == 2:
                print('Token aceito: Identificador<', self.cadeia, '>')
                self.char_atual = ''
                self.cadeia = ''
                self._estado = 0

            elif self._estado == 3:
                if self.__ehDigito(self.char_atual):
                    self.cadeia += self.char_atual

                else: 
                    if not (self.__ehCharUp(self.char_atual) or self.__ehCharLower(self.char_atual)):
                       self._estado = 4
                       self.retrocesso()
                    else:
                        print('Erro estado 3, digito invalido')
                        self.char_atual = ''
                        self.cadeia = ''
                        self._estado = 0
                        
            elif self._estado == 4: # Estado Final gerando NUM_INTEIRO
                self.estadoFinal("Inteiro")
                self.retrocesso()
            
            elif self._estado == 5: # Início do reconhecimento de PALAVRA
                self.cadeia += self.char_atual
                self._estado = 6
                print("QUALQUER SIMBOLO")

            elif self._estado == 6:
                self.cadeia += self.char_atual
                print(self.cadeia)
                if self.char_atual == '"':
                    print("INDO PARA O ESTADO FINAL")
                    self._estado = 7

            elif self._estado == 7: # Estado Final gerando PALAVRA
                self.estadoFinal("Palavra")
                self.retrocesso()

            elif self._estado == 8:
                if self.char_atual != '%':
                    self._estado = 18
                    self.retrocesso()
                elif self.char_atual == '%':
                    self.cadeia += self.char_atual
                    self._estado = 9
            elif self._estado == 9:
                if self.char_atual == '/':
                    self.cadeia += self.char_atual
                    self._estado = 10
            elif self._estado == 10:
                if self.char_atual != "\n": #Não usamos is_space porque trata todos
                    self.cadeia += self.char_atual
                else:
                    print("Comentário: ",self.cadeia)
                    self.retrocesso()
                    self._estado = 0

                
            elif self._estado == 18:
                print('Token aceito: <', self.cadeia, '>')
                self.char_atual = ''
                self.cadeia = ''
                self._estado = 0
                
                    
