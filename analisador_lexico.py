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

    def _ehEpaco(self, char: chr): #Rever a função
        return char == ' ' or char == '\t' or char == '\n' or char == '\r'
    
    def _ehEOF(self):
        return self._pos_arquivo >= len(self._conteudo)
    
    def _proximoChar(self):
        if self._ehEOF():
            return '\0'

        aux = self._conteudo[self._pos_arquivo]
        self._pos_arquivo += 1
        return aux
        
    def _retrocesso(self):
        self._pos_arquivo -= 1

    def _estadoFinal(self, tipoReconhecido: str):
            """Reinicia os atributos e exibe o Token aceito"""
            print('Token aceito: ', tipoReconhecido, '<', self._cadeia, '>')
            self._char_atual = ''
            self._cadeia = ''
            self._estado = 0

    def token(self):
        while(True):
            if self._ehEOF():
                return 
             
            self._char_atual = self._proximoChar()
            if self._estado == 0:
                if self._ehDigito(self._char_atual):
                    self._cadeia += self._char_atual
                    self._estado = 3
                elif self._ehCharLower(self._char_atual):
                    self._cadeia += self._char_atual
                    self._estado = 1
                elif self._char_atual == '/':
                    self._cadeia += self._char_atual
                    self._estado = 8
                elif self._char_atual == '"':
                    self._cadeia += self._char_atual
                    self._estado = 5
                elif self._ehCharUp(self._char_atual):
                    self._cadeia+= self._char_atual
                    self._estado = 25
                    

            elif self._estado == 1:
                if self._ehCharLower(self._char_atual) or self._ehCharUp(self._char_atual) or self._ehDigito(self._char_atual):
                    self._cadeia += self._char_atual
                else:  
                    self._estado = 2
                    self._retrocesso()
            
            elif self._estado == 2:
                print('Token aceito: Identificador<', self._cadeia, '>')
                self._char_atual = ''
                self._cadeia = ''
                self._estado = 0

            elif self._estado == 3:
                if self._ehDigito(self._char_atual):
                    self._cadeia += self._char_atual
                elif not (self._ehCharUp(self._char_atual) or self._ehCharLower(self._char_atual)):
                       self._estado = 4
                       self._retrocesso()
                else:
                    print('Erro estado 3, digito invalido')
                    self._char_atual = ''
                    self._cadeia = ''
                    self._estado = 0
                        
            elif self._estado == 4: # Estado Final gerando NUM_INTEIRO
                self._estadoFinal("Inteiro")
                self._retrocesso()
            
            elif self._estado == 5: # Início do reconhecimento de PALAVRA
                self._cadeia += self._char_atual
                self._estado = 6
                print("QUALQUER SIMBOLO")

            elif self._estado == 6:
                self._cadeia += self._char_atual
                print(self._cadeia)
                if self._char_atual == '"':
                    print("INDO PARA O ESTADO FINAL")
                    self._estado = 7

            elif self._estado == 7: # Estado Final gerando PALAVRA
                self._estadoFinal("Palavra")
                self._retrocesso()

            elif self._estado == 8:
                if self._char_atual != '%':
                    self._estado = 18
                    self._retrocesso()
                elif self._char_atual == '%':
                    self._cadeia += self._char_atual
                    self._estado = 9
            elif self._estado == 9:
                if self._char_atual == '/':
                    self._cadeia += self._char_atual
                    self._estado = 10
            elif self._estado == 10:
                if self._char_atual != "\n": #Não usamos is_space porque trata todos
                    self._cadeia += self._char_atual
                else:
                    print("Comentário: ",self._cadeia)
                    self._retrocesso()
                    self._estado = 0

                
            elif self._estado == 18:
                print('Token aceito: <', self._cadeia, '>')
                self._char_atual = ''
                self._cadeia = ''
                self._estado = 0
            
            elif self._estado == 25:
                if self._cadeia in self._palavra_reservada:
                    print('Token aceito: Palavra Reservada <', self._cadeia, '>')
                    self._char_atual = ''
                    self._cadeia = ''
                    self._estado = 0
                elif self._cadeia in self._operador_logico:
                    print('Token aceito: Operador lógico <', self._cadeia, '>')
                    self._char_atual = ''
                    self._cadeia = ''
                    self._estado = 0
                
                self._cadeia += self._char_atual
                
                    
