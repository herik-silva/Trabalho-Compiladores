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
            print(self.token)
            self.token = self.lexico.proximoToken()
            if(self.token.text == '#'):
                print(self.token)
                self.listaComandos()

    def listaComandos(self):
        self.comando()

    def comando(self):
        self.calMatematico()
    
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