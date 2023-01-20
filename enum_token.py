from enum import Enum

class TokenEnum(Enum):
    TK_IDENTIFICADOR = 1   
    TK_NUMERO        = 2                       
    TK_LITERAL       = 3                       
    TK_PRINCIPAL     = 4               
    TK_TIPOVAR       = 5           
    TK_SE            = 6       
    TK_SENAO         = 7           
    TK_SENAOSE       = 8           
    TK_ENQUANTO      = 9               
    TK_PARA          = 10       
    TK_LEIA          = 11       
    TK_ESCREVA       = 12           
    TK_RETORNE       = 13           
    TK_DELIMITADOR   = 14               
    TK_ABPARENTESE   = 15               
    TK_FCHPARENTESE  = 16               
    TK_CERQUILHA     = 17               
    TK_MAISMENOS     = 18               
    TK_MULTDIVISAO   = 19               
    TK_MOD           = 20       
    TK_ATRIBUICAO    = 21               
    TK_E             = 22       
    TK_OU            = 23       
    TK_NAO           = 24       
    TK_VALORBOOL     = 25               
    TK_RELACIONAL    = 26     
    TK_ABCOLCHETE    = 27
    TK_FCHCOLCHETE   = 28          
