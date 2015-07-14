# -*- coding: cp1252 -*-
# Victor Hugo Viana @2015


#Funcao para descobrir a hora em que o movimento foi completado
def FuncAcel(Vo,Vf,t):
    Acel = (Vf-Vo)/t
    return Acel



running = True
while(running):
    print """# Calcule a aceleração de um corpo,
# sendo sua massa desprezivel,
# e estando em movimento retilíneo uniformemente variado."""

    Vo = float(raw_input("\n\n\nInforme a velocidade inicial em metros: "))
    Vf = float(raw_input("Informe a velocidade final em metros: "))
    t = float(raw_input("Informe o tempo decorrido em segundos: "))

    Acel = FuncAcel(Vo,Vf,t)
    print "O movimento está sendo acelerado em:",Acel,"m/s²"

    repeat_loop = str(raw_input("Deseja repetir? <y/n> "))
    if repeat_loop=="y":continue
    else: running=False
