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
        #comando: atribuicao 
        if self.token.tipo == TokenEnum.TK_IDENTIFICADOR:
            self.atribuicao()
            self.escopo()
        #comando: desvio 
        elif self.token.tipo == TokenEnum.TK_SE:
            self.desvio()
            self.escopo()
        #comando: laco 
        elif (self.token.tipo == TokenEnum.TK_PARA or self.token.tipo == TokenEnum.TK_ENQUANTO or self.token.tipo == TokenEnum.TK_RETORNE):
            self.laco()
            self.escopo()
        #comando: entrada 
        elif self.token.tipo == TokenEnum.TK_LEIA:
            self.entrada()
            self.escopo()
        #comando: saida
        elif self.token.tipo == TokenEnum.TK_ESCREVA:
            self.saida()
            self.escopo()
        else:
            print('vazio')
            pass
    
    #atribuicao: variavel <= conteudo; | ε
    def atribuicao(self):
        self.aceitaToken(TokenEnum.TK_IDENTIFICADOR)
        self.aceitaToken(TokenEnum.TK_ATRIBUICAO)
        self.conteudo()
        self.aceitaToken(TokenEnum.TK_DELIMITADOR)
    
    #conteudo: palavra | expressaoAritmetica
    def conteudo(self):
        if self.token.tipo == TokenEnum.TK_LITERAL:
            self.aceitaToken(TokenEnum.TK_LITERAL)
        elif self.token.tipo == TokenEnum.TK_ABPARENTESE or self.token.tipo == TokenEnum.TK_IDENTIFICADOR or self.token.tipo == TokenEnum.TK_NUMERO:
            self.expressaoAritmetica()
        else: 
            pass
    
    #expressaoAritmetica: termo expressao
    def expressaoAritmetica(self):
        self.termo()
        self.expressao()

    #termo: fator termo2
    def termo(self):
        self.fator()
        self.termo2()
    
    #expressao: +termo expressao | -termo expressao |  ε
    def expressao(self):
        if(self.token.tipo == TokenEnum.TK_MAISMENOS):
            self.aceitaToken(TokenEnum.TK_MAISMENOS)
            self.termo()
            self.expressao()
        else:
            pass 
    
    #termo2: * fator termo2 | / fator termo2 | % fator termo2 | ε
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
    
    #fator: (expressaoAritimetica) | variavel | numero
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

    #entrada: LEIA( variavel );
    def entrada(self):
        self.aceitaToken(TokenEnum.TK_LEIA)
        self.aceitaToken(TokenEnum.TK_ABPARENTESE)
        self.aceitaToken(TokenEnum.TK_IDENTIFICADOR)
        self.aceitaToken(TokenEnum.TK_FCHPARENTESE)
        self.aceitaToken(TokenEnum.TK_DELIMITADOR)
    
    #saida: ESCREVA(expressaoAritmetica | palavra);
    def saida(self):
        self.aceitaToken(TokenEnum.TK_ESCREVA)
        self.aceitaToken(TokenEnum.TK_ABPARENTESE)
        if(self.token.tipo == TokenEnum.TK_ABPARENTESE or self.token.tipo == TokenEnum.TK_IDENTIFICADOR or self.token.tipo == TokenEnum.TK_NUMERO):
            self.expressaoAritmetica()
        elif (self.token.tipo == TokenEnum.TK_LITERAL):
            self.aceitaToken(TokenEnum.TK_LITERAL)

        self.aceitaToken(TokenEnum.TK_FCHPARENTESE)
        self.aceitaToken(TokenEnum.TK_DELIMITADOR)

    #desvio: SE (exp) # escopo # desvio2
    def desvio(self):
        self.aceitaToken(TokenEnum.TK_SE)
        self.aceitaToken(TokenEnum.TK_ABPARENTESE)
        print("OK ABRE PARENTESE!!!")
        self.exp()
        self.aceitaToken(TokenEnum.TK_FCHPARENTESE)
        print("OK FECHOU PARENTESE!!!")
        self.aceitaToken(TokenEnum.TK_CERQUILHA)
        self.escopo()
        self.aceitaToken(TokenEnum.TK_CERQUILHA)
        self.desvio2()
    
    #desvio2: SENAO # escopo # | SENAOSE(exp) # escopo # desvio2 | ε
    def desvio2(self):
        if(self.token.tipo == TokenEnum.TK_SENAO):
            self.aceitaToken(TokenEnum.TK_SENAO)
            self.aceitaToken(TokenEnum.TK_CERQUILHA)
            self.escopo()
            self.aceitaToken(TokenEnum.TK_CERQUILHA)
        elif(self.token.tipo == TokenEnum.TK_SENAOSE):
            self.aceitaToken(TokenEnum.TK_SENAOSE)
            self.aceitaToken(TokenEnum.TK_ABPARENTESE)
            self.exp()
            self.aceitaToken(TokenEnum.TK_FCHPARENTESE)
            self.aceitaToken(TokenEnum.TK_CERQUILHA)
            self.escopo()
            self.aceitaToken(TokenEnum.TK_CERQUILHA)
            self.desvio2()
        else:
            pass
    
    #exp: logico | VERDADEIRO | FALSO
    def exp(self):
        if(self.token.tipo == TokenEnum.TK_VALORBOOL):
            self.aceitaToken(TokenEnum.TK_VALORBOOL)
        else:
            print("DE EXP FUI PARA O LOGICO!!")
            self.logico()
       
    def logico(self):
        self.expressaoLogica()
        self.termoLogico()

    def termoLogico(self):
        if self.token.tipo == TokenEnum.TK_OU:
            self.aceitaToken(TokenEnum.TK_OU)
            self.expressaoLogica()
            self.termoLogico()
        else:
            pass

    def expressaoLogica(self):
        self.expressaoLogica3()
        self.expressaoLogica2()
    
    def expressaoLogica2(self):
        if self.token.tipo == TokenEnum.TK_E:
            self.aceitaToken(TokenEnum.TK_E)
            self.expressaoLogica3()
            self.expressaoLogica2()
        else:
            pass

    def expressaoLogica3(self):
        if self.token.tipo == TokenEnum.TK_NAO:
            self.aceitaToken(TokenEnum.TK_NAO)
            self.relacional()
        else:
            self.relacional()
            
    def relacional(self):
        if self.token.tipo == TokenEnum.TK_ABCOLCHETE:
            self.aceitaToken(TokenEnum.TK_ABCOLCHETE)
            self.logico()
            self.aceitaToken(TokenEnum.TK_FCHCOLCHETE)
        else:
            self.termoRelacional()

    def termoRelacional(self):
        self.conteudo()
        self.termoRelacional2()

    def termoRelacional2(self):
        if self.token.tipo == TokenEnum.TK_RELACIONAL:
            self.aceitaToken(TokenEnum.TK_RELACIONAL)
            self.conteudo()
        else:
            pass

   # laco: PARA (atribuicao conteudo simb_rel conteudo; identificado <= expressaoAritmetica) # escopo # | ENQUANTO( exp ) # escopo # | RETORNE
    def laco(self):
        if self.token.tipo == TokenEnum.TK_PARA:
            self.aceitaToken(TokenEnum.TK_PARA)
            self.aceitaToken(TokenEnum.TK_ABPARENTESE)
            self.atribuicao()
            self.conteudo()
            self.aceitaToken(TokenEnum.TK_RELACIONAL)
            self.conteudo()
            self.aceitaToken(TokenEnum.TK_DELIMITADOR)
            self.aceitaToken(TokenEnum.TK_IDENTIFICADOR)
            self.aceitaToken(TokenEnum.TK_ATRIBUICAO)
            self.expressaoAritmetica()
            self.aceitaToken(TokenEnum.TK_FCHPARENTESE)
            self.aceitaToken(TokenEnum.TK_CERQUILHA)
            self.escopo()
            self.aceitaToken(TokenEnum.TK_CERQUILHA)
        elif self.token.tipo == TokenEnum.TK_ENQUANTO:
            self.aceitaToken(TokenEnum.TK_ENQUANTO)
            self.aceitaToken(TokenEnum.TK_ABPARENTESE)
            self.exp()
            self.aceitaToken(TokenEnum.TK_FCHPARENTESE)
            self.aceitaToken(TokenEnum.TK_CERQUILHA)
            self.escopo()
            self.aceitaToken(TokenEnum.TK_CERQUILHA)
        elif self.token.tipo == TokenEnum.TK_RETORNE:
            self.aceitaToken(TokenEnum.TK_RETORNE)
        else:
            print("ERRO!")