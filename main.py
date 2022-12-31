from scanner import Scanner
from token_ import Token

scanner = Scanner("file.txt")

arquivo =  scanner._content
print(arquivo)
valores = []  
bloco = ""
aux = 0
while 1:
    if(aux < arquivo.__len__()):
        char = arquivo[aux]
        print(char)
        if not scanner.isSpace(char):
            bloco +=  char
        elif(bloco.__len__()>0):  
            valores.append(bloco)
            bloco = ""
        aux += 1
    else:
        if(bloco.__len__()>0):
            valores.append(bloco)

        break

 
print(valores)
# print('tipos', set(valores) & set(tipos))
# print('simbolos', set(valores) & set(simbolos))
# print('numerais', set(valores) & set(numerais))