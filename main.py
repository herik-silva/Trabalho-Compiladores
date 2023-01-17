from analisador_lexico import AnalisadorLexico
from analisador_sintatico import AnalisadorSintatico

scanner = AnalisadorLexico("file.txt")



ana = AnalisadorSintatico(scanner)

ana.inicio()




#while(not scanner._ehEOF()):
 #   print(scanner.proximoToken())

#print(len(scanner._conteudo))
#scanner.token()


