class AnalisadorLexico:
    
    def __init__(self, path: str) -> None:
        self._palavra_reservada = ['SE', 'SENAO', 'SENAOSE', 'LACO', 'LACOPARA', 'RETORNE', 'INTEIRO', 'BOOLEANO', 'CONSTANTE', 'VAZIO', 'TEXTO']
        self._operador_logico = ['NAO', 'E', 'OU']
        self._pos_arquivo = 0 
        self._estado = 0
        self._char_atual = ''
        self._cadeia = ''
        arquivo = open(path, 'r')
        self._conteudo = arquivo.read()
        arquivo.close()

    def _ehDigito(self, char: chr):
        return char >= '0' and char <= '9' 
    
    def _ehCharUp(self, char: chr):
        return char >= 'A' and char <= 'Z'

    def _ehCharLower(self, char: chr):
        return char >= 'a' and char <= 'z'

    def _ehSimbolo(self, char: chr):
        return char == ';' or char == '(' or char == ')' or char == '[' or char == ']' or char == '#'

    def _ehOperadorMat(self, char: chr):
        return char == '+' or char == '-' or char == '*' or char == '%' 
    
    def _ehEspaco(self, char: chr): #Rever a função
        return char == ' ' or char == '\t' or char == '\n' or char == '\r'
    
    def _ehEOF(self):
        return self._pos_arquivo >= len(self._conteudo)
    
    def _proximoChar(self):
        if self._ehEOF():
            return None
        aux = self._conteudo[self._pos_arquivo]
        self._pos_arquivo += 1
        return aux
        
    def _retrocesso(self):
        self._pos_arquivo -= 1

    def _limpar(self):
        self._char_atual = ''
        self._cadeia = ''
        self._estado = 0

    def _estadoFinal(self, tipoReconhecido: str):
            """Reinicia os atributos e exibe o Token aceito"""
            print('Token aceito: ', tipoReconhecido, '<', self._cadeia, '>')
            self._limpar()
        
    def token(self):
        while(True): 
            
            self._char_atual = self._proximoChar()
            if not self._char_atual:
                return 

            if self._estado == 0:
                if self._ehCharLower(self._char_atual):
                    self._cadeia += self._char_atual
                    self._estado = 1
                    if self._ehEOF():
                        self._estadoFinal('IDENTIFICADOR')
                elif self._ehDigito(self._char_atual):
                    self._cadeia += self._char_atual
                    self._estado = 3
                    if self._ehEOF():
                        self._estadoFinal('IDENTIFICADOR')
                elif self._char_atual == '"':
                    self._cadeia += self._char_atual
                    self._estado = 5
                elif self._char_atual == '/':
                    self._cadeia += self._char_atual
                    self._estado = 7
                    if self._ehEOF():
                        self._estadoFinal(self._cadeia)
                elif self._ehOperadorMat(self._char_atual):
                    self._cadeia += self._char_atual
                    self._estado = 12
                    if self._ehEOF():
                        self._estadoFinal(self._cadeia)
                elif self._ehSimbolo(self._char_atual):
                    self._cadeia += self._char_atual
                    self._estado = 13
                    if self._ehEOF():
                        self._estadoFinal(self._cadeia)
                elif self._ehCharUp(self._char_atual):
                    self._cadeia += self._char_atual
                    self._estado = 14
                    if self._ehEOF():
                        if self._cadeia in self._operador_logico:
                            self._estadoFinal('OPERADOR LOGICO')
                        else:
                            print('Erro estado 0 para 14')
                            self._limpar()
                elif self._char_atual == '=':
                    self._cadeia += self._char_atual
                    self._estado = 16
                elif self._char_atual == '<':
                    self._cadeia += self._char_atual
                    self._estado = 18
                elif self._char_atual == '>':
                    self._cadeia += self._char_atual
                    self._estado = 22

            elif self._estado == 1:
                if self._ehCharLower(self._char_atual) or self._ehCharUp(self._char_atual) or self._ehDigito(self._char_atual):
                    self._cadeia += self._char_atual
                    #Verifica se é o ultimo caracter do arquivo
                    if self._ehEOF():
                        self._estadoFinal('IDENTIFICADOR')
                else:  #Estado 2
                    self._estadoFinal('IDENTIFICADOR')
                    self._retrocesso()
            
            elif self._estado == 3:
                if self._ehDigito(self._char_atual):
                    self._cadeia += self._char_atual
                    #Verifica se é o ultimo digito do arquivo
                    if self._ehEOF():
                        self._estadoFinal('NUM_INTEIRO')
                #Estado 4
                elif not (self._ehCharUp(self._char_atual) or self._ehCharLower(self._char_atual)):
                       self._estadoFinal('NUM_INTEIRO')
                       self._retrocesso()
                else:
                    print('Erro estado 3, digito invalido')
                    self._limpar()

            elif self._estado == 5: # Início do reconhecimento de PALAVRA
                if self._char_atual != '"':
                    self._cadeia += self._char_atual
                #Estado 6
                else:
                    self._cadeia += self._char_atual
                    self._estadoFinal("PALAVRA")
            
            elif self._estado == 7:
                if self._char_atual == '%':
                    self._cadeia += self._char_atual
                    self._estado = 8
                #Estado 11
                else:
                    self._estadoFinal('/')
                    self._retrocesso()

            elif self._estado == 8:
                if self._char_atual == '/':
                    self._cadeia += self._char_atual
                    self._estado = 9
                else:
                    print('Erro estado 8, símbolo invalido')
                    self._limpar()

            elif self._estado == 9:
                if self._char_atual != '\n' and not self._ehEOF():
                    self._cadeia += self._char_atual
                #Estado 10
                elif self._char_atual == '\n':
                    self._estadoFinal('COMENTARIO')
                else:
                    self._cadeia += self._char_atual
                    self._estadoFinal('COMENTARIO')
                
            elif self._estado == 12:
                self._estadoFinal(self._cadeia)
                self._retrocesso()

            elif self._estado == 13:
                self._estadoFinal(self._cadeia)
                self._retrocesso()
            
            elif self._estado == 14:
                if self._ehCharUp(self._char_atual):
                    self._cadeia += self._char_atual
                    if self._ehEOF():
                        if self._cadeia in self._palavra_reservada:
                            self._estadoFinal('PALAVRA RESERVADA')
                        elif self._cadeia in self._operador_logico:
                            self._estadoFinal('OPERADOR LOGICO')
                        else:
                            print('ERROR PALAVRA RESERVADA ou OPERADOR LOGICO')
                            self._limpar()
                #Estado 15
                else:
                    if self._cadeia in self._palavra_reservada:
                        self._estadoFinal('PALAVRA RESERVADA')
                        self._retrocesso()
                    elif self._cadeia in self._operador_logico:
                        self._estadoFinal('OPERADOR LOGICO')
                        self._retrocesso()
                    else:
                        print('ERROR PALAVRA RESERVADA ou OPERADOR LOGICO')
                        self._limpar()

            elif self._estado == 16:
                if self._char_atual == '?':
                    self._cadeia += self._char_atual
                    self._estadoFinal(self._cadeia)

            elif self._estado == 18:
                #Estado 17
                if self._char_atual == '?':
                    self._cadeia += self._char_atual
                    self._estadoFinal(self._cadeia)
                #Estado 19
                elif self._char_atual == '=':
                    self._cadeia += self._char_atual
                    if self._ehEOF():
                        self._estadoFinal(self._cadeia)
                    #Estado 20
                    else:
                        self._char_atual = self._proximoChar()
                        #Estado 20
                        if self._char_atual != '?':
                            self._estadoFinal(self._cadeia)
                        #Estado 17
                        else:
                            self._cadeia += self._char_atual
                            self._estadoFinal(self._cadeia)
                #Estado 21
                elif self._char_atual == '>':
                    self._cadeia += self._char_atual
                    self._char_atual = self._proximoChar()
                    #Estado 17
                    if self._char_atual == '?':
                        self._cadeia += self._char_atual
                        self._estadoFinal(self._cadeia)
                    else:
                        print('Erro estado 18 <>')
                        self._limpar()

            elif self._estado == 22:
                #Estado 17
                if self._char_atual == '?':
                    self._cadeia += self._char_atual
                    self._estadoFinal(self._cadeia)
                #Estado 23
                elif self._char_atual == '=':
                    self._cadeia += self._char_atual
                    if self._ehEOF():
                        print('ERROR estado 22 >=')
                        self._limpar()
                    else:
                        self._char_atual = self._proximoChar()
                        #Estado 17
                        if self._char_atual == '?':
                            self._cadeia += self._char_atual
                            self._estadoFinal(self._cadeia)
                        else:
                            print('ERROR estado 22 >=x')
                            self._limpar()
            
                    
