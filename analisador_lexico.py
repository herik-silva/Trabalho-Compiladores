from token_ import Token
from enum_token import TokenEnum
from erro import Erro

class AnalisadorLexico:

    def __init__(self, path: str) -> None:
        self._pos_arquivo = 0 
        self._linha = 1
        self.tabela_identificador = {}
        arquivo = open(path, 'r')
        self._conteudo = arquivo.read()
        self._conteudo = self._conteudo.strip()
        arquivo.close()

    def _ehDigito(self, char: chr):
        return char >= '0' and char <= '9' 
    
    def _ehCharUp(self, char: chr):
        return char >= 'A' and char <= 'Z'

    def _ehCharLower(self, char: chr):
        return char >= 'a' and char <= 'z'

    def _ehSimbolo(self, char: chr):
        return char == ';' or char == '(' or char == ')' or char == '#' or char == "[" or char == "]"

    def _ehOperadorMat(self, char: chr):
        return char == '+' or char == '-' or char == '*' or char == '%' 

    def  _ehEspaco(self, char: chr):
        return char == ' ' or char == '\t'

    def _ehNovaLinha(self, char: chr):
        return char == '\r' or char == '\n'
    
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
    

    def _aceitaPalavraRes(self, cadeia, linha):
        if cadeia == 'PRINCIPAL':
            return Token(TokenEnum.TK_PRINCIPAL, cadeia, linha)
        elif cadeia == 'INTEIRO':
            return Token(TokenEnum.TK_TIPOVAR, cadeia, linha)
        elif cadeia == 'TEXTO':
            return Token(TokenEnum.TK_TIPOVAR, cadeia, linha)
        elif cadeia == 'SE':
            return Token(TokenEnum.TK_SE, cadeia, linha)
        elif cadeia == 'SENAO':
            return Token(TokenEnum.TK_SENAO, cadeia, linha)
        elif cadeia == 'SENAOSE':
            return Token(TokenEnum.TK_SENAOSE, cadeia, linha)
        elif cadeia == 'ENQUANTO':
            return Token(TokenEnum.TK_ENQUANTO, cadeia, linha)
        elif cadeia == 'PARA':
            return Token(TokenEnum.TK_PARA, cadeia, linha)
        elif cadeia == 'LEIA':
            return Token(TokenEnum.TK_LEIA, cadeia, linha)
        elif cadeia == 'ESCREVA':
            return Token(TokenEnum.TK_ESCREVA, cadeia, linha)
        elif cadeia == 'RETORNE':
            return Token(TokenEnum.TK_RETORNE, cadeia, linha)
        elif cadeia == 'VERDADEIRO':
            return Token(TokenEnum.TK_VALORBOOL, cadeia, linha)
        elif cadeia == 'FALSO':
            return Token(TokenEnum.TK_VALORBOOL, cadeia, linha)
        elif cadeia == 'NAO':
            return Token(TokenEnum.TK_NAO, cadeia, linha)
        elif cadeia == 'E':
            return Token(TokenEnum.TK_E, cadeia, linha)
        elif cadeia == 'OU':
            return Token(TokenEnum.TK_OU, cadeia, linha)
        else:
            raise Erro("Erro Léxico: Palavra reservada inválida '{}'.".format(cadeia), 
                            " Erro na linha {}.".format(linha))

    def _aceitaOperadorMat(self, cadeia, linha):
        if(cadeia == '+'):
            return Token(TokenEnum.TK_MAISMENOS, cadeia, linha)
        elif(cadeia == '-'):
            return Token(TokenEnum.TK_MAISMENOS, cadeia, linha)
        elif(cadeia == '*'):
            return Token(TokenEnum.TK_MULTDIVISAO, cadeia, linha)
        elif(cadeia == '%'):
            return Token(TokenEnum.TK_MOD, cadeia, linha)
        
    def _aceitaSimbolo(self, cadeia, linha):
        if(cadeia == ';'):
            return Token(TokenEnum.TK_DELIMITADOR, cadeia, linha)
        elif(cadeia == '('):
            return Token(TokenEnum.TK_ABPARENTESE, cadeia, linha)
        elif(cadeia == ')'):
            return Token(TokenEnum.TK_FCHPARENTESE, cadeia, linha)
        elif(cadeia == '#'):
            return Token(TokenEnum.TK_CERQUILHA, cadeia, linha)
        elif(cadeia == '['):
            return Token(TokenEnum.TK_ABCOLCHETE, cadeia, linha)
        elif(cadeia == ']'):
            return Token(TokenEnum.TK_FCHCOLCHETE, cadeia, linha)


    def proximoToken(self):
        self._limpar()
        while(True): 
            self._char_atual = self._proximoChar()
            if not self._char_atual:
                return Token(TokenEnum.TK_FIM, self._cadeia, self._linha)
           
            if self._estado == 0:
                if self._ehNovaLinha(self._char_atual):
                    self._linha += 1

                if self._ehCharLower(self._char_atual):
                    self._cadeia += self._char_atual
                    self._estado = 1
                    if self._ehEOF():
                        token = Token(TokenEnum.TK_IDENTIFICADOR, self._cadeia, self._linha)
                        if not token.texto in self.tabela_identificador:
                            self.tabela_identificador[token.texto] = token
                        return token
                        
                elif self._ehDigito(self._char_atual):
                    self._cadeia += self._char_atual
                    self._estado = 3
                    if self._ehEOF():
                        return Token(TokenEnum.TK_NUMERO, self._cadeia, self._linha)

                elif self._char_atual == '"':
                    self._cadeia += self._char_atual
                    self._estado = 5

                elif self._char_atual == '/':
                    self._cadeia += self._char_atual
                    self._estado = 7
                    if self._ehEOF():
                        return Token(TokenEnum.TK_MULTDIVISAO, self._cadeia, self._linha)
                        
                elif self._ehOperadorMat(self._char_atual):
                    self._cadeia += self._char_atual
                    self._estado = 12
                    if self._ehEOF():
                       return self._aceitaOperadorMat(self._cadeia, self._linha)

                elif self._ehSimbolo(self._char_atual):
                    self._cadeia += self._char_atual
                    self._estado = 13
                    if self._ehEOF():
                        return self._aceitaSimbolo(self._cadeia, self._linha)

                elif self._ehCharUp(self._char_atual):
                    self._cadeia += self._char_atual
                    self._estado = 14
                    if self._ehEOF():
                        if self._cadeia in self._operador_logico:
                            return Token(TokenEnum.TK_E, self._cadeia, self._linha)
                        else:
                            raise Erro("Erro Léxico: Palavra reservada inválida '{}'.".format(self._cadeia), 
                                            " Erro na linha {}.".format(self._linha))

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
                        token = Token(TokenEnum.TK_IDENTIFICADOR, self._cadeia, self._linha)
                        if not token.texto in self.tabela_identificador:
                            self.tabela_identificador[token.texto] = token
                        return token
                else:  #Estado 2
                    if self._ehNovaLinha(self._char_atual):
                        self._linha += 1
                        token = Token(TokenEnum.TK_IDENTIFICADOR, self._cadeia, self._linha - 1)
                        if not token.texto in self.tabela_identificador:
                            self.tabela_identificador[token.texto] = token    
                        return token
                    elif self._ehEspaco(self._char_atual):
                        token = Token(TokenEnum.TK_IDENTIFICADOR, self._cadeia, self._linha)
                        if not token.texto in self.tabela_identificador:
                            self.tabela_identificador[token.texto] = token
                        return token
                    else:
                        self._retrocesso()
                        token = Token(TokenEnum.TK_IDENTIFICADOR, self._cadeia, self._linha)
                        if not token.texto in self.tabela_identificador:
                            self.tabela_identificador[token.texto] = token
                        return token
                    
            
            elif self._estado == 3:
                if self._ehDigito(self._char_atual):
                    self._cadeia += self._char_atual
                    #Verifica se é o ultimo digito do arquivo
                    if self._ehEOF():
                        return Token(TokenEnum.TK_NUMERO, self._cadeia, self._linha)
                #Estado 4
                elif not (self._ehCharUp(self._char_atual) or self._ehCharLower(self._char_atual)):
                    if self._ehNovaLinha(self._char_atual):
                        self._linha += 1
                        return Token(TokenEnum.TK_NUMERO, self._cadeia, self._linha - 1)
                    elif self._ehEspaco(self._char_atual):
                        return Token(TokenEnum.TK_NUMERO, self._cadeia, self._linha)
                    else:
                        self._retrocesso()
                        return Token(TokenEnum.TK_NUMERO, self._cadeia, self._linha)
                else:
                    self._cadeia += self._char_atual
                    raise Erro("Erro Léxico: Era esperado um número, não {}.".format(self._cadeia), 
                                                            ' Erro na linha {}.'.format(self._linha))
                
                       
            elif self._estado == 5: # Início do reconhecimento de PALAVRA
                if self._char_atual != '"':
                    self._cadeia += self._char_atual
                #Estado 6
                else:
                    self._cadeia += self._char_atual
                    self._char_atual = self._proximoChar()
                    if self._ehNovaLinha(self._char_atual):
                        self._linha += 1
                        return Token(TokenEnum.TK_LITERAL, self._cadeia, self._linha - 1)
                    elif self._ehEspaco(self._char_atual):
                        return Token(TokenEnum.TK_LITERAL, self._cadeia, self._linha)
                    else:
                        self._retrocesso()
                        return Token(TokenEnum.TK_LITERAL, self._cadeia, self._linha)


            elif self._estado == 7:
                if self._char_atual == '%':
                    self._cadeia += self._char_atual
                    self._estado = 8
                #Estado 11
                else:
                    if self._ehNovaLinha(self._char_atual):
                        self._linha += 1
                        return Token(TokenEnum.TK_MULTDIVISAO, self._cadeia, self._linha - 1)
                    elif self._ehEspaco(self._char_atual):
                        return Token(TokenEnum.TK_MULTDIVISAO, self._cadeia, self._linha)
                    else: 
                        self._retrocesso()
                        return Token(TokenEnum.TK_MULTDIVISAO, self._cadeia, self._linha)
                   

            elif self._estado == 8:
                if self._char_atual == '/':
                    self._estado = 9
                else:
                     raise Erro("Erro Léxico: Era esperado um '/', '/%'. Você quis dizer '/%/'?.", 
                                                            ' Erro na linha {}.'.format(self._linha))

            elif self._estado == 9:
                if self._char_atual != '\n':
                    pass
                #Estado 10
                else:
                    self._linha += 1
                    self._limpar()
               

            elif self._estado == 12:
                if self._ehNovaLinha(self._char_atual):
                    self._linha += 1
                    return self._aceitaOperadorMat(self._cadeia, self._linha - 1)
                elif self._ehEspaco(self._char_atual):
                    return self._aceitaOperadorMat(self._cadeia, self._linha)
                else:
                    self._retrocesso()
                    return self._aceitaOperadorMat(self._cadeia, self._linha)
                

            elif self._estado == 13:
                if self._ehNovaLinha(self._char_atual):
                    self._linha += 1
                    return self._aceitaSimbolo(self._cadeia, self._linha - 1)
                elif self._ehEspaco(self._char_atual):
                    return self._aceitaSimbolo(self._cadeia, self._linha)
                else:
                    self._retrocesso()
                    return self._aceitaSimbolo(self._cadeia, self._linha)
                
            
            elif self._estado == 14:
                if self._ehCharUp(self._char_atual):
                    self._cadeia += self._char_atual
                    if self._ehEOF():
                        return self._aceitaPalavraRes(self._cadeia, self._linha)
                #Estado 15
                else:
                  
                    if self._ehNovaLinha(self._char_atual):
                        self._linha += 1
                        self._aceitaPalavraRes(self._cadeia, self._linha - 1)
                    elif self._ehEspaco(self._char_atual):
                        return self._aceitaPalavraRes(self._cadeia, self._linha)
                    else:
                        self._retrocesso()
                        return self._aceitaPalavraRes(self._cadeia, self._linha)


            elif self._estado == 16:
                if self._char_atual == '?':
                    self._cadeia += self._char_atual
                    return Token(TokenEnum.TK_RELACIONAL, self._cadeia, self._linha)
                else:
                    self._cadeia += self._char_atual
                    raise Erro("Era esperado um '?', '{}'. Você quis dizer '=?' ?.".format(self._cadeia), 
                                                            ' Erro na linha {}.'.format(self._linha))

            elif self._estado == 18:
                #Estado 17
                if self._char_atual == '?':
                    self._cadeia += self._char_atual
                    return Token(TokenEnum.TK_RELACIONAL, self._cadeia, self._linha)
                #Estado 19
                elif self._char_atual == '=':
                    self._cadeia += self._char_atual
                    if self._ehEOF():
                        return Token(TokenEnum.TK_ATRIBUICAO, self._cadeia, self._linha)
                    #Estado 20
                    else:
                        self._char_atual = self._proximoChar()
                        #Estado 20
                        if self._char_atual != '?':
                            if self._ehNovaLinha(self._char_atual):
                                self._linha += 1
                                return Token(TokenEnum.TK_ATRIBUICAO, self._cadeia, self._linha - 1)
                            elif self._ehEspaco(self._char_atual):
                                return Token(TokenEnum.TK_ATRIBUICAO, self._cadeia, self._linha)
                            else:
                                self._retrocesso()
                                return Token(TokenEnum.TK_ATRIBUICAO, self._cadeia, self._linha)
                        #Estado 17
                        else:
                            self._cadeia += self._char_atual
                            return Token(TokenEnum.TK_RELACIONAL, self._cadeia, self._linha)
                #Estado 21
                elif self._char_atual == '>':
                    self._cadeia += self._char_atual
                    self._char_atual = self._proximoChar()
                    #Estado 17
                    if self._char_atual == '?':
                        self._cadeia += self._char_atual
                        return Token(TokenEnum.TK_RELACIONAL, self._cadeia, self._linha)
                    else:
                        self._cadeia += self._char_atual
                        raise Erro("Era esperado um '?', '{}'. Você quis dizer '<>?' ?.".format(self._cadeia), 
                                                            ' Erro na linha {}.'.format(self._linha))
                else:
                    raise Erro("Era esperado um '?', '{}'. Você quis dizer '<?' ?.".format(self._cadeia), 
                                                            ' Erro na linha {}.'.format(self._linha))

            elif self._estado == 22:
                #Estado 17
                if self._char_atual == '?':
                    self._cadeia += self._char_atual
                    return Token(TokenEnum.TK_RELACIONAL, self._cadeia, self._linha)
                #Estado 23
                elif self._char_atual == '=':
                    self._cadeia += self._char_atual
                    if self._ehEOF():
                        raise Erro("Era esperado um '?', '{}'. Você quis dizer '>=?' ?.".format(self._cadeia), 
                                                            ' Erro na linha {}.'.format(self._linha))
                    else:
                        self._char_atual = self._proximoChar()
                        #Estado 17
                        if self._char_atual == '?':
                            self._cadeia += self._char_atual
                            return Token(TokenEnum.TK_RELACIONAL, self._cadeia, self._linha)
                        else:
                            raise Erro("Era esperado um '?', '{}'. Você quis dizer '>=?' ?.".format(self._cadeia), 
                                                            ' Erro na linha {}.'.format(self._linha))
                else:
                     raise Erro("Era esperado um '?', '{}'. Você quis dizer '>?' ?.".format(self._cadeia), 
                                                            ' Erro na linha {}.'.format(self._linha))
