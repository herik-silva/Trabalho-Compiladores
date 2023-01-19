from analisador_lexico import AnalisadorLexico
from token_ import *
from erro import Erro

MAX_TOKEN = 2 # Máximo de tokens no vetor de token.

class AnalisadorSintatico:
    token: Token
    def __init__(self, lexico: AnalisadorLexico):
        self.lexico = lexico
        self.token = []

    def lerToken(self):
        if len(self.token):
            self.token.pop(0)
        
        while len(self.token) < MAX_TOKEN: 
            if not self.lexico._ehEOF(): 
                self.token.append(self.lexico.proximoToken())

        print(self.token[0])
        print(self.token[1])
    
    def olharAdiante(self, tkIndex: int) -> Token:
        if len(self.token) == 0:
            return None

        if tkIndex > MAX_TOKEN: # Retorna o último
            return self.token[MAX_TOKEN - 1]

        return self.token[tkIndex-1]

    def combinar(self, tk_tipo: TokenEnum):
        tk_aux = self.olharAdiante(1)
        if tk_aux.tipo == tk_tipo:
            print("Match: ", tk_aux)
            self.lerToken()
        else:
            raise Erro("Erro sintático...")


    def conteudo(self):
        self.token = self.olhar_adiante(2)
        print(self.token)
        """  if(TK_STR[self.token.tipo] == 'LITERAL'):
                print(self.token)
                self.token = self.lexico.proximoToken() """

    def declaracaol(self):
        self.token = self.lexico.proximoToken()
        if(TK_STR[self.token.tipo] == 'ATRIBUICAO'):
            print(self.token)
            self.conteudo()

    def variavel(self):
        self.token = self.lexico.proximoToken()
        if(TK_STR[self.token.tipo] == 'IDENTIFICADOR'):
            print(print(self.token))

    def tipo(self):
        print(self.token)

    def declaracao(self):
        if self.token.texto == 'INTEIRO' or self.token.texto == 'TEXTO':
            self.tipo()
            self.variavel()
            self.declaracaol()

    def comando(self):
        if(self.token.texto == 'INTEIRO' or self.token.texto == 'TEXTO'
            or self.token.texto == 'IDENTIFICADOR' or self.token.texto == '(' 
            or self.token.texto == 'NUMERO'):
                self.declaracao()

    def escopo(self):
        if self.token:
            if(TK_STR[self.token.tipo] == 'PALAVRA RESERVADA'
                or TK_STR[self.token.tipo] == 'IDENTIFICADOR'
                or TK_STR[self.token.tipo] == 'NUMERO'):
                    self.comando()
                    self.escopo()
            elif(self.token.texto == '#'):
                print(self.token, '\nAnalise sintática ok.')

    def inicio(self):
        self.token = self.lexico.proximoToken()
        if(self.token.texto == 'PRINCIPAL'):
            print(self.token)
            self.token = self.lexico.proximoToken()
            if(self.token.texto == '#'):
                print(self.token)
                self.token = self.lexico.proximoToken()
                self.escopo()

   
                
   
      

   

   

    def atribuicao(self):
        if(self.token.TK_STR[self.token.type] == 'PALAVRA RESERVADA'):
            if(self.token.text == 'INTEIRO' or self.token.text == 'TEXTO'
                or self.token.text == 'CONSTANTE'):
                self.declaracao()

   
    
   

    def calMatematico(self):
        self.E()

    def E(self):
        self.T()
        self.El()

    def El(self):
        if(self.token.text == '+' or self.token.text == '-'):
            print(self.token)
            self.T()

    def T(self):
        self.F()
        self.Tl()


    def Tl(self):
        self.token = self.lexico.proximoToken()
        if(self.token.text == '*' or self.token.text == '/' or self.token.text == '%'):
            print(self.token)
            self.F()
            
    def F(self):
        self.token = self.lexico.proximoToken()
        if(self.token.TK_STR[self.token.type] == 'NUMERO'):
            print(self.token)