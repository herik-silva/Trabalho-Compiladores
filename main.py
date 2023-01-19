from analisador_lexico import AnalisadorLexico
from analisador_sintatico import AnalisadorSintatico

scanner = AnalisadorLexico("file.txt")
""" while(not scanner._ehEOF()):
    print(scanner.proximoToken()) """

sintatico = AnalisadorSintatico(scanner)
sintatico.olhar_adiante(1)
sintatico.conteudo()
print('tabela', scanner.tabela_identificador)

