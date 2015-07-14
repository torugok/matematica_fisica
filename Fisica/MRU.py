# -*- coding: cp1252 -*-
# Victor Hugo Viana @2015


#Funcao para descobrir o tempo em que o movimento foi completado
def FuncTempo(DeltaPos,posIn,Vm):
    T = (DeltaPos+(-posIn))/Vm
    return T


running = True
while(running):
    DeltaPos = float(raw_input("Informe o espa�o decorrido em metros: "))
    posIn = float(raw_input("Informe a posi��o inicial em metros: "))
    Vm = float(raw_input("Informe a velocidade em m/s: "))

    T = FuncTempo(DeltaPos,posIn,Vm)
    print "O percurso ser� completado em ",T," segundos."

    repeat_loop = str(raw_input("Deseja repetir? <y/n> "))
    if repeat_loop=="y":continue
    else: running=False
