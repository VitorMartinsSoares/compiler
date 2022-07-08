import re
arq = open("codigo.c","r")
tokensIni = []
operadores = ["+","-","*","/","="]
reservadas = ["#include","<stdio.h>","main()","return","int","{","}",";","const","while","if","float","double"]
numeros = ["0","1","2","3","4","5","6","7","8","9"]

for x in arq:
    x = x.strip()
    lista = x.split()
    for y in lista:
        y = y.strip()
        if(";" in y):
            y = y.split(";")
            tokensIni.append(y[0])
            tokensIni.append(";")
        else:
            tokensIni.append(y)

for x in tokensIni:
    if x in operadores:
        print(x+" - Operador")
    elif x in reservadas:
        print(x+" - Reservada")
    elif re.search(r"\d+.+\d",x) or re.search(r"\d",x):
        print(x+" - Numero")
    else:
        print(x+" - Variavel") 