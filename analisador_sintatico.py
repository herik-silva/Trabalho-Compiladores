from analisador_lexico import AnalisadorLexico
from token_ import *
from enum_token import TokenEnum
from erro import ErroSintatico


class AnalisadorSintatico:
    token: Token
    def __init__(self, lexico: AnalisadorLexico):
        self.lexico = lexico
        self.token = None
        self.erro = []
        self.lerToken()

    def lerToken(self):
        if not self.lexico._ehEOF():
            self.token = self.lexico.proximoToken()
        
    def aceitaToken(self, tipo: TokenEnum):
        if self.token.tipo == tipo:
            #print(self.token)
            self.lerToken()
            return True
        return False
    
    def instanciarErro(self, tk):
        self.erro.append(ErroSintatico('Erro sintático: Era esperado o TOKEN "{}", foi encontrado "{}".'.format(tk, self.token.texto),
                            'Erro na linha {}'.format(self.token.linha)))
        self.lerToken()
    
    #inicio: PRINCIPAL # listaDeclaracao escopo #
    def inicio(self):
        if not self.aceitaToken(TokenEnum.TK_PRINCIPAL):
            self.instanciarErro('PRINCIPAL')
        if not self.aceitaToken(TokenEnum.TK_CERQUILHA):
            self.instanciarErro('#')

        self.listaDeclaracoes()
        self.escopo()

        if not self.aceitaToken(TokenEnum.TK_CERQUILHA):
            self.instanciarErro('#')

    #listaDeclaracao: declaracao listaDeclaracao | ε
    def listaDeclaracoes(self):
        if self.token.tipo == TokenEnum.TK_TIPOVAR:
            self.declaracoes()
            self.listaDeclaracoes()
     
    #declaracoes: tipo variavel;
    def declaracoes(self):
        if not self.aceitaToken(TokenEnum.TK_TIPOVAR):
            self.instanciarErro('INTEIRO OU TEXTO')
        if not self.aceitaToken(TokenEnum.TK_IDENTIFICADOR):
            self.instanciarErro('IDENTIFICADOR')
        if not self.aceitaToken(TokenEnum.TK_DELIMITADOR):
            self.instanciarErro(';')
    
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
    
    #atribuicao: variavel <= conteudo;
    def atribuicao(self):
        self.aceitaToken(TokenEnum.TK_IDENTIFICADOR)
        if not self.aceitaToken(TokenEnum.TK_ATRIBUICAO):
            self.instanciarErro('ATRIBUIÇAO (<=)')
        self.conteudo()
        if not self.aceitaToken(TokenEnum.TK_DELIMITADOR):
            self.instanciarErro(';')
    
    #conteudo: palavra | expressaoAritmetica
    def conteudo(self):
        if self.token.tipo == TokenEnum.TK_LITERAL:
            self.aceitaToken(TokenEnum.TK_LITERAL)
        elif self.token.tipo == TokenEnum.TK_ABPARENTESE or self.token.tipo == TokenEnum.TK_IDENTIFICADOR or self.token.tipo == TokenEnum.TK_NUMERO:
            self.expressaoAritmetica()
        else:
            self.instanciarErro('LITERAL, (, IDENTIFICADOR OU NUMERO')
       
    
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
    
    #fator: (expressaoAritimetica) | variavel | numero
    def fator(self):
        if(self.token.tipo == TokenEnum.TK_ABPARENTESE):
            self.aceitaToken(TokenEnum.TK_ABPARENTESE)
            self.expressaoAritmetica()
            if not self.aceitaToken(TokenEnum.TK_FCHPARENTESE):
                self.instanciarErro(')')
        elif(self.token.tipo == TokenEnum.TK_IDENTIFICADOR):
            self.aceitaToken(TokenEnum.TK_IDENTIFICADOR)
        elif(self.token.tipo == TokenEnum.TK_NUMERO):
            self.aceitaToken(TokenEnum.TK_NUMERO)
        else:
            self.instanciarErro('(, IDENTIFICADOR ou NUMERO')

    #entrada: LEIA( variavel );
    def entrada(self):
        self.aceitaToken(TokenEnum.TK_LEIA)
        if not self.aceitaToken(TokenEnum.TK_ABPARENTESE):
            self.instanciarErro('(')
        if not self.aceitaToken(TokenEnum.TK_IDENTIFICADOR):
            self.instanciarErro('IDENTIFICADOR')
        if not self.aceitaToken(TokenEnum.TK_FCHPARENTESE):
            self.instanciarErro(')')
        if not self.aceitaToken(TokenEnum.TK_DELIMITADOR):
            self.instanciarErro(';')
    
    #saida: ESCREVA(expressaoAritmetica | palavra);
    def saida(self):
        self.aceitaToken(TokenEnum.TK_ESCREVA)
        if not self.aceitaToken(TokenEnum.TK_ABPARENTESE):
            self.instanciarErro('(')
        if(self.token.tipo == TokenEnum.TK_ABPARENTESE or self.token.tipo == TokenEnum.TK_IDENTIFICADOR or self.token.tipo == TokenEnum.TK_NUMERO):
            self.expressaoAritmetica()
        elif (self.token.tipo == TokenEnum.TK_LITERAL):
            self.aceitaToken(TokenEnum.TK_LITERAL)
        else:
            self.instanciarErro('Algum símbolo')

        if not self.aceitaToken(TokenEnum.TK_FCHPARENTESE):
            self.instanciarErro(')')
        if not self.aceitaToken(TokenEnum.TK_DELIMITADOR):
            self.instanciarErro(';')

    #desvio: SE (exp) # escopo # desvio2
    def desvio(self):
        self.aceitaToken(TokenEnum.TK_SE)
        if not self.aceitaToken(TokenEnum.TK_ABPARENTESE):
            self.instanciarErro('(')
      
        self.exp()
        if not self.aceitaToken(TokenEnum.TK_FCHPARENTESE):
            self.instanciarErro(')')

        if not self.aceitaToken(TokenEnum.TK_CERQUILHA):
            self.instanciarErro('#')

        self.escopo()
        if not self.aceitaToken(TokenEnum.TK_CERQUILHA):
            self.instanciarErro('#')
        self.desvio2()
    
    #desvio2: SENAO # escopo # | SENAOSE(exp) # escopo # desvio2 | ε
    def desvio2(self):
        if(self.token.tipo == TokenEnum.TK_SENAO):
            self.aceitaToken(TokenEnum.TK_SENAO)
            if not self.aceitaToken(TokenEnum.TK_CERQUILHA):
                self.instanciarErro('#')
            self.escopo()
            if not self.aceitaToken(TokenEnum.TK_CERQUILHA):
                self.instanciarErro('#')
        elif(self.token.tipo == TokenEnum.TK_SENAOSE):
            self.aceitaToken(TokenEnum.TK_SENAOSE)
            if not self.aceitaToken(TokenEnum.TK_ABPARENTESE):
                self.instanciarErro('(')
            self.exp()
            if not self.aceitaToken(TokenEnum.TK_FCHPARENTESE):
                self.instanciarErro(')')
            if not self.aceitaToken(TokenEnum.TK_CERQUILHA):
                self.instanciarErro('#')
            self.escopo()
            if not self.aceitaToken(TokenEnum.TK_CERQUILHA):
                self.instanciarErro('#')
            self.desvio2()
    
    #exp: logico | VERDADEIRO | FALSO
    def exp(self):
        if(self.token.tipo == TokenEnum.TK_VALORBOOL):
            self.aceitaToken(TokenEnum.TK_VALORBOOL)
        elif(self.token.tipo == TokenEnum.TK_NAO or self.token.tipo == TokenEnum.TK_ABPARENTESE or
                self.token.tipo == TokenEnum.TK_LITERAL or self.token.tipo == TokenEnum.TK_IDENTIFICADOR or self.token.tipo == TokenEnum.TK_NUMERO):
            self.logico()
        else:
            self.instanciarErro('NAO, (, LITERAL, IDENTIFICADOR ou NUMERO')
       
    def logico(self):
        self.expressaoLogica()
        self.termoLogico()

    def termoLogico(self):
        if self.token.tipo == TokenEnum.TK_OU:
            self.aceitaToken(TokenEnum.TK_OU)
            self.expressaoLogica()
            self.termoLogico()
       

    def expressaoLogica(self):
        self.expressaoLogica3()
        self.expressaoLogica2()
    
    def expressaoLogica2(self):
        if self.token.tipo == TokenEnum.TK_E:
            self.aceitaToken(TokenEnum.TK_E)
            self.expressaoLogica3()
            self.expressaoLogica2()
       

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
            if not self.aceitaToken(TokenEnum.TK_FCHCOLCHETE):
                self.instanciarErro(')')
        else:
            self.termoRelacional()


    def termoRelacional(self):
        self.conteudo()
        self.termoRelacional2()

    def termoRelacional2(self):
        if self.token.tipo == TokenEnum.TK_RELACIONAL:
            self.aceitaToken(TokenEnum.TK_RELACIONAL)
            self.conteudo()

   # laco: PARA (atribuicao conteudo simb_rel conteudo; identificado <= expressaoAritmetica) # escopo # | ENQUANTO( exp ) # escopo # | RETORNE
    def laco(self):
        if self.token.tipo == TokenEnum.TK_PARA:
            self.aceitaToken(TokenEnum.TK_PARA)
            if not self.aceitaToken(TokenEnum.TK_ABPARENTESE):
                self.instanciarErro('(')

            self.atribuicao()
            self.conteudo()

            if not self.aceitaToken(TokenEnum.TK_RELACIONAL):
                self.instanciarErro('RELACIONAL')

            self.conteudo()
            if not self.aceitaToken(TokenEnum.TK_DELIMITADOR):
                self.instanciarErro(';')
            if not self.aceitaToken(TokenEnum.TK_IDENTIFICADOR):
                self.instanciarErro('IDENTIFICADOR')
            if not self.aceitaToken(TokenEnum.TK_ATRIBUICAO):
                self.instanciarErro('ATRIBUIÇAÕ (<=)')
            self.expressaoAritmetica()
            if not self.aceitaToken(TokenEnum.TK_FCHPARENTESE):
                self.instanciarErro(')')
            if not self.aceitaToken(TokenEnum.TK_CERQUILHA):
                self.instanciarErro('#')
            self.escopo()
            if not self.aceitaToken(TokenEnum.TK_CERQUILHA):
                self.instanciarErro('#')
        elif self.token.tipo == TokenEnum.TK_ENQUANTO:
            self.aceitaToken(TokenEnum.TK_ENQUANTO)
            if not self.aceitaToken(TokenEnum.TK_ABPARENTESE):
                self.instanciarErro('(')
            self.exp()
            if not self.aceitaToken(TokenEnum.TK_FCHPARENTESE):
                self.instanciarErro(')')
            if not self.aceitaToken(TokenEnum.TK_CERQUILHA):
                self.instanciarErro('#')
            self.escopo()
            if not self.aceitaToken(TokenEnum.TK_CERQUILHA):
                self.instanciarErro('#')
        elif self.token.tipo == TokenEnum.TK_RETORNE:
            self.aceitaToken(TokenEnum.TK_RETORNE)
            