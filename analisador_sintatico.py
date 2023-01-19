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
            self.atribuicao()
            self.escopo()
        elif self.token.tipo == TokenEnum.TK_SE:
            self.desvio()
            self.escopo()
        elif (self.token.tipo == TokenEnum.TK_PARA or self.token == TokenEnum.TK_ENQUANTO or self.token == TokenEnum.TK_RETORNE):
         #   self.laco()
            self.escopo()
        elif self.token.tipo == TokenEnum.TK_LEIA:
            self.entrada()
            self.escopo()
        elif self.token.tipo == TokenEnum.TK_ESCREVA:
            self.saida()
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
        elif self.token.tipo == TokenEnum.TK_ABPARENTESE or self.token.tipo == TokenEnum.TK_IDENTIFICADOR or self.token.tipo == TokenEnum.TK_NUMERO:
            self.expressaoAritmetica()
        else: 
            pass
    def expressaoAritmetica(self):
        self.termo()
        self.expressao()

    def termo(self):
        self.fator()
        self.termo2()
    
    def expressao(self):
        if(self.token.tipo == TokenEnum.TK_MAISMENOS):
            self.aceitaToken(TokenEnum.TK_MAISMENOS)
            self.termo()
            self.expressao()
        else:
            pass 
    
    def termo2(self):
        if(self.token.tipo == TokenEnum.TK_MULTDIVISAO):
            self.aceitaToken(TokenEnum.TK_MULTDIVISAO)
            self.fator()
            self.termo2()
        elif(self.token.tipo == TokenEnum.TK_MOD):
            self.aceitaToken(TokenEnum.TK_MOD)
            self.fator()
            self.termo2()
        else: 
            pass
    def fator(self):
        if(self.token.tipo == TokenEnum.TK_ABPARENTESE):
            self.aceitaToken(TokenEnum.TK_ABPARENTESE)
            self.expressaoAritmetica()
            self.aceitaToken(TokenEnum.TK_FCHPARENTESE)
        elif(self.token.tipo == TokenEnum.TK_IDENTIFICADOR):
            self.aceitaToken(TokenEnum.TK_IDENTIFICADOR)
        elif(self.token.tipo == TokenEnum.TK_NUMERO):
            self.aceitaToken(TokenEnum.TK_NUMERO)
        else:
            print("ERRO no Fator")

    def entrada(self):
        self.aceitaToken(TokenEnum.TK_LEIA)
        self.aceitaToken(TokenEnum.TK_ABPARENTESE)
        self.aceitaToken(TokenEnum.TK_IDENTIFICADOR)
        self.aceitaToken(TokenEnum.TK_FCHPARENTESE)
        self.aceitaToken(TokenEnum.TK_DELIMITADOR)
    
    def saida(self):
        self.aceitaToken(TokenEnum.TK_ESCREVA)
        self.aceitaToken(TokenEnum.TK_ABPARENTESE)
        if(self.token.tipo == TokenEnum.TK_ABPARENTESE or self.token.tipo == TokenEnum.TK_IDENTIFICADOR or self.token.tipo == TokenEnum.TK_NUMERO):
            self.expressaoAritmetica()
        elif (self.token.tipo == TokenEnum.TK_LITERAL):
            self.aceitaToken(TokenEnum.TK_LITERAL)

        self.aceitaToken(TokenEnum.TK_FCHPARENTESE)
        self.aceitaToken(TokenEnum.TK_DELIMITADOR)

    def desvio(self):
        self.aceitaToken(TokenEnum.TK_SE)
        self.aceitaToken(TokenEnum.TK_ABPARENTESE)
        self.exp()
        self.aceitaToken(TokenEnum.TK_FCHPARENTESE)
        self.aceitaToken(TokenEnum.TK_CERQUILHA)
        self.escopo()
        self.desvio2()
        self.aceitaToken(TokenEnum.TK_CERQUILHA)

    def desvio2(self):
        if(self.token.tipo == TokenEnum.TK_SENAO):
            self.aceitaToken(TokenEnum.TK_SENAO)
            self.desvio3()
        else:
            pass

    def desvio3(self):
        if(self.token.tipo == TokenEnum.TK_CERQUILHA):
            self.aceitaToken(TokenEnum.TK_CERQUILHA)
            self.escopo()
            self.aceitaToken(TokenEnum.TK_CERQUILHA)
        else:
            self.desvio()

    def exp(self):
        if(self.token.tipo == TokenEnum.TK_VALORBOOL):
            self.aceitaToken(TokenEnum.TK_VALORBOOL)
        elif(self.token.tipo == TokenEnum.TK_NAO):
            self.aceitaToken(TokenEnum.TK_NAO)
        elif(self.token.tipo == TokenEnum.TK_E):
            self.aceitaToken(TokenEnum.TK_E)
        elif(self.token.tipo == TokenEnum.TK_OU):
            self.aceitaToken(TokenEnum.TK_OU)