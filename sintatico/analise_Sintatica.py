import re

arq = open("codigo.txt","r")
erro = 0
chaves = []
parenteses = []
posiP = -1
posi = -1
tokensIni = []
funcoes = []
variaveisDeclarada = []
operadores = ["+","-","*","/"]
atribuicao = ["=","+=","-=","*=","/=","%=","<<=",">>=","&=","|=","^="]
reservadas = ["#include","<stdio.h>","main()","return","int","{","}",";","const","while","if","float","double"]

for x in arq:
    print()
    print("Linha: ")
    print(x.strip("\n"))


    ##Tokens
    tokensIni = []
    z = x.strip()
    lista = z.split()
    for y in lista:
        y = y.strip()
        if(";" in y):
            y = y.split(";")
            tokensIni.append(y[0])
            tokensIni.append(";")
        else:
            tokensIni.append(y)
    ##Analise sem tokenização
    if "#include" in x:
        x = x.strip()
        x = x.split()
        tam = len(x)
        if(tam == 2):
            tam2 = len(x[1])
            if((x[0]=="#include") and x[1][0]=="<" and x[1][tam2-1]==">" and x[1][tam2-2]=="h" and x[1][tam2-3]=="." ):
                a = 1
            else:
                erro = 1
        else:
            erro = 1
        if(erro):
            print("código invalido")
            
    if "int" in x:
        x = x.strip()
        y = x.split()
        if(y[0]=="int" or y[0]=="float" or y[0]=="double"):
            if(y[2][0]=="(" or y[1][len(y[1])-2]=="("):
                if(y[2][len(y[2])-1]==")" or y[1][len(y[1])-1]==")"):
                    if("main" in y[1]):
                        print("função principal")
                    else:
                        print("função")
                    funcoes.append(1)
                else: 
                    print("erro, sem fechar parenteses")
            if(x[len(x)-1] == ';'):
                variaveisDeclarada.append(tokensIni[1])
                print("criação")
                if(tokensIni[1] in variaveisDeclarada):
                    if(tokensIni[2] in atribuicao):
                        print("atribuicao de valor")
                        for t in range(len(tokensIni)-1):
                            if(tokensIni[t] in operadores):
                                if ((tokensIni[t-1] in variaveisDeclarada) or (tokensIni[t-1] in funcoes) or (re.search(r"\d+.+\d",tokensIni[t-1]) or re.search(r"\d",tokensIni[t-1]))) and ((tokensIni[t+1] in variaveisDeclarada) or (tokensIni[t+1] in funcoes) or (re.search(r"\d+.+\d",tokensIni[t+1]) or re.search(r"\d",tokensIni[t+1]))):
                                    print("operacao")
                                else:
                                    print("formulacao de operacao errada")
                    else:
                        print("ERROR")
    else:
        if (tokensIni[len(tokensIni)-1]==';'):
            if(tokensIni[0] in variaveisDeclarada):
                if(tokensIni[1] in atribuicao):
                    for t in range(len(tokensIni)-1):
                        if(tokensIni[t] in operadores):
                            if ((tokensIni[t-1] in variaveisDeclarada) or (tokensIni[t-1] in funcoes) or (re.search(r"\d+.+\d",tokensIni[t-1]) or re.search(r"\d",tokensIni[t-1]))) and ((tokensIni[t+1] in variaveisDeclarada) or (tokensIni[t+1] in funcoes) or (re.search(r"\d+.+\d",tokensIni[t+1]) or re.search(r"\d",tokensIni[t+1]))):
                                print("atribuicao de valor")
                            else:
                                print("formulacao de operacao errada")
                else:
                    print("ERROR")
            elif (tokensIni[0] == "return"):
                print("retorno final")
            else:
                print("variavel nao declarada")




    ##Parenteses e chaves, erros
    if "{" in x:
        chaves.append(1)
    if "}" in x:
        posi +=1
        if(posi+1 > len(chaves)):
            print("ERROR: Fechando chaves a mais")
        else:
            chaves[posi] = 0
    if "(" in x:
        parenteses.append(1)
    if ")" in x:
        posiP +=1
        if(posiP+1 > len(parenteses)):
            print("ERROR: Fechando parenteses a mais")
        else:
            parenteses[posiP] = 0
for teste in chaves:
    if(teste == 1):                             
        print("ERROR: Não Fechando chaves")
for teste in parenteses:
    if(teste == 1):                             
        print("ERROR: Não Fechando parenteses")