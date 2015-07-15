# Distancia entre dois Objetos (Geometria analitica)
# Victor Hugo Viana @2015
from math import sqrt

def Dist(X_a,Y_a,X_b,Y_b):
    dist = sqrt(((X_a-X_b)**2)+((Y_a-Y_b)**2))
    return dist


running = True
while(running):
    Obj_A = [0,0]
    Obj_B = [0,0]
    for i in range(2):
        #Objeto A
        if i == 0:
            Obj_A[0] = float(raw_input("Informe a posicao X do primeiro objeto: "))
            Obj_A[1] = float(raw_input("Informe a posicao Y do primeiro objeto: "))
        #Objeto B
        else:
            Obj_B[0] = float(raw_input("\nInforme a posicao X do segundo objeto: "))
            Obj_B[1] = float(raw_input("Informe a posicao Y do segundo objeto: "))

    Dist = Dist(Objeto_A[0],Objeto_A[1],Objeto_B[0],Objeto_B[1])
    print "\nDistância entre os dois objetos:",Dist,"u.a"

    repeat_loop = str(raw_input("\nDeseja repetir? <y/n> "))
    if repeat_loop=="y":continue
    else: running=False

