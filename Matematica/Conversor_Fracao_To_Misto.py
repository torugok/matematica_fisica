#Conversor de fra��o impropria para numero misto


def ParaMisto(a,b):
    misto = int(a/b)
    new_a = a % b
    return [misto,int(new_a),int(b)] if a>b and new_a != 0 else False

print '# Transforme uma fra��o impropria, em um numero misto, lembrando que "a/b".'

running = True
while(running):
        
    
    a = float(raw_input("\nInforme a: "))
    b = float(raw_input("Informe b: "))
 

    conj = ParaMisto(a,b)
    if conj !=False:
        print "A fra��o em numero misto:",conj[0],"|",conj[1],"/",conj[2]
    else:
        print "A fra��o tem de estar a>b e a divis�o tem que ter resto."

    repeat_loop = str(raw_input("Deseja repetir? <y/n> "))
    if repeat_loop=="y":continue
    else: running=False
