# -*- coding: cp1252 -*-
# Victor Hugo Viana @2015


#Funcao para descobrir a velocidade em que,
#o movimento em função do tempo foi completado
def FuncVel(Vo,Acel,t):
    Vf=Vo+Acel*t
    return Vf

running = True
while(running):

    Vo = float(raw_input("Informe a velocidade inicial em metros: "))
    Acel = float(raw_input("Informe a aceleração em m/s²: "))
    t = float(raw_input("Informe o tempo decorrido em segundos: "))
    
    print "A velocidade final no momento",t,"segundo(s), é igual a:",FuncVel(Vo,Acel,t),"m/s."
    
    repeat_loop = str(raw_input("Deseja repetir? <y/n> "))
    if repeat_loop=="y":continue
    else: running=False
