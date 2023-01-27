from analisador_lexico import AnalisadorLexico
from analisador_sintatico import AnalisadorSintatico

scanner = AnalisadorLexico("file.txt")
#while(not scanner._ehEOF()):
#     print(scanner.proximoToken()) 

sintatico = AnalisadorSintatico(scanner)
sintatico.inicio()



for i in sintatico.erro_sintatico:
    print(i)

for j in sintatico.erro_semantico:
    print(j)

