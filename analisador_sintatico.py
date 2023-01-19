from analisador_lexico import AnalisadorLexico
from token_ import *
from enum_token import TokenEnum


class AnalisadorSintatico:
    token: Token
    def __init__(self, lexico: AnalisadorLexico):
        self.lexico = lexico
        self.token = None
        self.lerToken()

    def lerToken(self):
        self.token = self.lexico.proximoToken()
        
    def aceitaToken(self, tipo: TokenEnum):
        if self.token.tipo == tipo:
            print(self.token)
            self.lerToken()
        else:
            print('Erro')
    
    #inicio: PRINCIPAL # listaDeclaracao escopo #
    def inicio(self):
        self.aceitaToken(TokenEnum.TK_PRINCIPAL)
        self.aceitaToken(TokenEnum.TK_CERQUILHA)
        self.listaDeclaracoes()
        self.escopo()
        self.aceitaToken(TokenEnum.TK_CERQUILHA)

    #listaDeclaracao: declaracao listaDeclaracao | ε
    def listaDeclaracoes(self):
        if self.token.tipo == TokenEnum.TK_TIPOVAR:
            self.declaracoes()
            self.listaDeclaracoes()
        else:
            print('vazio listadeclarações')
            pass
    
    #declaracoes: tipo variavel;
    def declaracoes(self):
        self.aceitaToken(TokenEnum.TK_TIPOVAR)
        self.aceitaToken(TokenEnum.TK_IDENTIFICADOR)
        self.aceitaToken(TokenEnum.TK_DELIMITADOR)
    
    #escopo: comando escopo | ε
    def escopo(self):
        if self.token.tipo == TokenEnum.TK_IDENTIFICADOR:
            print('dfff',self.token)
            self.atribuicao()
            self.escopo()
        elif self.token.tipo == TokenEnum.TK_SE:
        #    self.desvio()
            self.escopo()
        elif (self.token.tipo == TokenEnum.TK_PARA or self.token == TokenEnum.TK_ENQUANTO or self.token == TokenEnum.TK_RETORNE):
         #   self.laco()
            self.escopo()
        elif self.token.tipo == TokenEnum.TK_LEIA:
          #  self.entrada()
            self.escopo()
        elif self.token.tipo == TokenEnum.TK_ESCREVA:
           # self.saida()
            self.escopo()
        else:
            print('vazio')
            pass
    
    def atribuicao(self):
        self.aceitaToken(TokenEnum.TK_IDENTIFICADOR)
        self.aceitaToken(TokenEnum.TK_ATRIBUICAO)
        self.conteudo()
        self.aceitaToken(TokenEnum.TK_DELIMITADOR)
    
    def conteudo(self):
        if self.token.tipo == TokenEnum.TK_LITERAL:
            self.aceitaToken(TokenEnum.TK_LITERAL)
        

