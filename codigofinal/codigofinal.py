from dataclasses import replace
import re
tiposlaco = ["for", "if", "else", "while"]
arq = open("codigofinal/codigo1.txt","r")
laco = False
cont = -1
tokensIni = []
funcoes = []
tiposfuncoes = []
parametrosfuncoes = []
codigofuncao = []
linhacodigo = []
variaveisDeclarada = []
tiposvariaveis = []
func = False
defvar = ["int","double","float"]
tipos = ["float ","double ","int ","char ","string ","(float)","(double)","(int)"]
reservadas = ["#include","<stdio.h>","main()","return","int","{","}",";","const","while","if","float","double","(",")"]
for x in arq:
    print(x)
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
    if(laco):
        x = "\t"+x
    for t in tiposlaco:
        if(t in x):
            x = x.replace("{",":")
            laco =  True
    if(x[len(x)-1] == ';' and tokensIni[0] in defvar):
        variaveisDeclarada.append(tokensIni[1])
        tiposvariaveis.append(y[0])
        for t in range(len(y)):
            if(y[t] == ','):
                variaveisDeclarada.append(y[t+1])
                tiposvariaveis.append(y[0])
    if "cin >> " in x:
        x = x.replace("cin >> ","")
        retorno = variaveisDeclarada.index(tokensIni[2])
        x = x+" = "+tiposvariaveis[retorno]+"(input(''))"
    if "cout << " in x:
        x = x.replace("cout << ","print(")
        x = x.replace(";",")")
    if(laco and "}" in x):
        laco = False
    elif("}" in x and func and not laco):
        codigofuncao.append(linhacodigo)
        linhacodigo = []
        func = False    
    elif(func and not "{" in x):
        tipoA = ""
        for z in tipos:
            if(z in x):
                x = x.replace(z,"")
                tipoA = z
        if("double" in tipoA or "float" in tipoA or "int" in tipoA):
            if(not "=" in x):
                x = x.replace(", ","= 0\n\t")
                x = x+" = 0"
        if("char" in tipoA or "string" in tipoA):
            x = x.replace(", ","=''\n\t")
            x = x+"''"
        linhacodigo.append(x)
    elif(y[0]=="int" or y[0]=="float" or y[0]=="double"):
        if(y[2]=="(" and y[len(y)-1]==")"):
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
            parametrosfuncoes.append(parametros)

arq = open("codigoIntermediario.py","w")
for i in range(len(funcoes)):
    #arq.write("def"+ funcoes+"()")
    escrita = "def "+funcoes[i]+"("
    for j in range(len(parametrosfuncoes[i])):
        escrita = escrita+str(parametrosfuncoes[i][j][1])
        if (j+1 !=len(parametrosfuncoes[i])):
            escrita = escrita+","
    escrita = escrita+"):\n"
    arq.write(escrita)
    for j in codigofuncao[i]:
        j=j.replace(";","")
        arq.write("\t"+str(j)+"\n")
arq.write("main()")
print(tiposvariaveis)
    #print(funcoes[i], tiposfuncoes[i],parametrosfuncoes[i],codigofuncao[i])