import re
arq = open("codigofinal/codigo1.txt","r")
cont = -1
tokensIni = []
funcoes = []
tiposfuncoes = []
parametrosfuncoes = []
codigofuncao = []
linhacodigo = []
variaveisDeclarada = []
tiposvariaveis = []
valoresvariaveis = []
func = False
atribuicao = ["=","+=","-=","*=","/=","%=","<<=",">>=","&=","|=","^="]
operadores = ["+","-","*","/"]
reservadas = ["#include","<stdio.h>","main()","return","int","{","}",";","const","while","if","float","double","(",")"]
for x in arq:
    tokensIni = []
    cont+=1
    ##Tokens
    if("//" in x):
        aux = x.split("//")
        x = aux[0]
    x = x.strip()
    lista = x.split()
    for y in lista:
        if(";" in y):
            y = y.split(";")
            tokensIni.append(y[0])
            tokensIni.append(";")
        else:
            tokensIni.append(y)
    y = tokensIni
    if("}" in x):
        linhacodigo = []
        codigofuncao.append(linhacodigo)
        func = False        
    if(func and not "{" in x):
        linhacodigo.append(x)
    elif(y[0]=="int" or y[0]=="float" or y[0]=="double"):
        if(y[2]=="(" and y[len(y)-1]==")"):
            if y[1] != "main":
                func = True
            parametros = []
            funcoes.append(y[1])
            tiposfuncoes.append(y[0])
            for t in range(3,len(y)-1):
                var = []
                if(y[t]!=',' and not y[t] in reservadas):
                    var.append(y[t-1])
                    var.append(y[t])
                parametros.append(var)
            parametrosfuncoes.append(var)
        if(y[len(y)-1] == ';'):
            variaveisDeclarada.append(tokensIni[1])
            tiposvariaveis.append(y[0])
            for t in range(len(y)):
                if(y[t] == ','):
                    variaveisDeclarada.append(y[t+1])
                    tiposvariaveis.append(y[0])

print(codigofuncao)