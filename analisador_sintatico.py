from analisador_lexico import AnalisadorLexico
from token_ import Token


class AnalisadorSintatico:
    token: Token
    def __init__(self, lexico: AnalisadorLexico):
        self.lexico = lexico
        self.token = None


    def inicio(self):
        self.token = self.lexico.proximoToken()
        if(self.token.text == 'PRINCIPAL'):
            print(self.token, 'OK')
            self.token = self.lexico.proximoToken()
            if(self.token.text == '#'):
                print(self.token, 'ok')
                self.listaComandos()

    def listaComandos(self):
        self.token = self.lexico.proximoToken()
        if(self.token.TK_STR[self.token.type] == 'PALAVRA RESERVADA'
            or self.token.TK_STR[self.token.type] == 'IDENTIFICADOR'
            or self.token.TK_STR[self.token.type] == 'NUMERO'
            or self.token.TK_STR[self.token.type] == 'PONTUACAO'):
                self.comando()
                self.listaComandosl()

    def listaComandosl(self):
        self.listaComandos()

    def comando(self):
        if(self.token.TK_STR[self.token.type] == 'PALAVRA RESERVADA'):
            if(self.token.text == 'INTEIRO' or self.token.text == 'TEXTO'
                or self.token.text == 'CONSTANTE'):
                self.declaracao()
        if(self.token.TK_STR[self.token.type] == 'IDENTIFICADOR'):
            self.atribuicao()
    
    def declaracao(self):
        self.tipo()
        self.variavel()
        self.declaracaol()

    def declaracaol(self):
        self.token = self.lexico.proximoToken()
        if(self.token.TK_STR[self.token.type] == 'ATRIBUICAO'):
            print(self.token)
            self.conteudo()

    def conteudo(self):
        self.token = self.lexico.proximoToken()
        if(self.token.TK_STR[self.token.type] == 'LITERAL'):
            print(self.token)

    def atribuicao(self):
        if(self.token.TK_STR[self.token.type] == 'PALAVRA RESERVADA'):
            if(self.token.text == 'INTEIRO' or self.token.text == 'TEXTO'
                or self.token.text == 'CONSTANTE'):
                self.declaracao()

    def tipo(self):
        print(self.token)
    
    def variavel(self):
        self.token = self.lexico.proximoToken()
        if(self.token.TK_STR[self.token.type] == 'IDENTIFICADOR'):
            print(print(self.token))

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