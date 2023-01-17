<<<<<<< HEAD
from analisador_lexico import AnalisadorLexico
from analisador_sintatico import AnalisadorSintatico
=======
# from analisador_lexico import AnalisadorLexico
from erro import Erro
>>>>>>> main

# scanner = AnalisadorLexico("file.txt")

<<<<<<< HEAD


ana = AnalisadorSintatico(scanner)

ana.inicio()




#while(not scanner._ehEOF()):
 #   print(scanner.proximoToken())

#print(len(scanner._conteudo))
#scanner.token()
=======
# #print(len(scanner._conteudo))
# scanner.token()
>>>>>>> main


erro = Erro(10, 10)
erro.exibirErro()