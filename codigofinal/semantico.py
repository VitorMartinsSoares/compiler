import re
arq = open("codigofinal/codigo1.txt","r")
cont = -1
tokensIni = []
funcoes = []
tiposfuncoes = []
variaveisDeclarada = []
tiposvariaveis = []
atribuicao = ["=","+=","-=","*=","/=","%=","<<=",">>=","&=","|=","^="]
operadores = ["+","-","*","/"]
reservadas = ["#include","<stdio.h>","main()","return","int","{","}",";","const","while","if","float","double","(",")"]
for x in arq:
    cont+=1
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
    if("//" in x):
        aux = x.split("//")
        x = aux[0]
    print(x)
    ##Analise sem tokenização
    if "int" in x or "float" in x or "double" in x:
        x = x.strip()
        y = x.split()
        if(y[0]=="int" or y[0]=="float" or y[0]=="double"):
            if(y[2][0]=="(" or y[1][len(y[1])-2]=="("):
                if(y[2][len(y[2])-1]==")" or y[1][len(y[1])-1]==")"):
                    funcoes.append(y[1])
                    tiposfuncoes.append(y[0])
            if(x[len(x)-1] == ';'):
                variaveisDeclarada.append(tokensIni[1])
                tiposvariaveis.append(y[0])
                for t in range(len(y)):
                    if(y[t] == ','):
                        variaveisDeclarada.append(y[t+1])
                        tiposvariaveis.append(y[0])
                if(tokensIni[1] in variaveisDeclarada):
                    if(tokensIni[2] in atribuicao):
                        for t in range(3,len(tokensIni)-1):
                            if (tokensIni[t] in variaveisDeclarada):
                                if(tiposvariaveis[variaveisDeclarada.index(tokensIni[t])]==tiposvariaveis[variaveisDeclarada.index(tokensIni[1])]):
                                    print(tokensIni[t]+" : \nMesmo tipo de Variavel")
                                else:
                                    print("ERROR:")
                                    print(tokensIni[t]+" : \nTipos diferentes!!!")
                            elif (tokensIni[t] in funcoes):
                                if(tiposfuncoes[funcoes.index(tokensIni[t])]==tiposvariaveis[variaveisDeclarada.index(tokensIni[1])]):
                                    print(tokensIni[t]+" : \nMesmo tipo de Variavel")
                                else:
                                    print("ERROR:")
                                    print(tokensIni[t]+" : \nTipos diferentes!!!")
                            elif (re.search(r"\d+.+\d",tokensIni[t]) and tiposvariaveis[variaveisDeclarada.index(tokensIni[1])]=="int"):
                                print("ERROR:")
                                print(tokensIni[t]+" : \nTipos diferentes!!!")
                            elif (re.search(r"\d",tokensIni[t])):
                                print(tokensIni[t]+" : \nMesmo tipo de Variavel")

    else:
        if (tokensIni[len(tokensIni)-1]==';'):
            if(tokensIni[0] in variaveisDeclarada):
                if(tokensIni[1] in atribuicao):
                    for t in range(2 ,len(tokensIni)-1):
                        if (tokensIni[t] in variaveisDeclarada):
                            if(tiposvariaveis[variaveisDeclarada.index(tokensIni[t])]==tiposvariaveis[variaveisDeclarada.index(tokensIni[0])]):
                                print(tokensIni[t]+" : \nMesmo tipo de Variavel")
                            else:
                                print("ERROR:")
                                print(tokensIni[t]+" : \nTipos diferentes!!!")
                        elif (tokensIni[t] in funcoes):
                            if(tiposfuncoes[funcoes.index(tokensIni[t])]==tiposvariaveis[variaveisDeclarada.index(tokensIni[0])]):
                                print(tokensIni[t]+" : \nMesmo tipo de Variavel")
                            else:
                                print("ERROR:")
                                print(tokensIni[t]+" : \nTipos diferentes!!!")
                        elif (re.search(r"\d+.+\d",tokensIni[t]) and tiposvariaveis[variaveisDeclarada.index(tokensIni[0])]=="int"):
                            print("ERROR:")
                            print(tokensIni[t]+" : \nTipos diferentes!!!")
                        elif (re.search(r"\d",tokensIni[t])):
                            print(tokensIni[t]+" : \nMesmo tipo de Variavel")
                        elif (not(tokensIni[t] in operadores or tokensIni[t] in reservadas)):
                            print("ERROR:")
                            print(tokensIni[t]+" : \nVariaveis invalida!!!")
            elif (tokensIni[0] == "return"):
                print("")
print(variaveisDeclarada)