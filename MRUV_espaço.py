# -*- coding: cp1252 -*-
# Victor Hugo Viana @2015


#Funcao para descobrir a velocidade em que,
#o movimento em função do tempo foi completado
def FuncEspaco(So,Vo,t,Acel):
    Sf=So+Vo*t+(Acel*(t**2))/2
    return Sf

running = True
while(running):
    print """# Calcule o espaço percorrido por um corpo,
# sendo sua massa desprezivel,
# e estamdp em movimento retilíneo uniformemente variado."""
    
    So = float(raw_input("\n\n\nInforme a posição inicial em metros: "))
    Vo = float(raw_input("Informe a velocidade inicial em metros: "))
    Acel = float(raw_input("Informe a aceleração em m/s²: "))
    t = float(raw_input("Informe o tempo decorrido em segundos: "))

    Delta_S = FuncEspaco(So,Vo,Acel,t)
    print "O espaço percorrido em",t,"segundo(s), é igual a:",Delta_S,"metros."
    
    repeat_loop = str(raw_input("Deseja repetir? <y/n> "))
    if repeat_loop=="y":continue
    else: running=False
