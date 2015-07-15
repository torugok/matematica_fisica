#Conversor de fração impropria para numero misto


def ParaMisto(a,b):
    misto = int(a/b)
    new_a = a % b
    return [misto,int(new_a),int(b)] if a>b and new_a != 0 else False

print '# Transforme uma fração impropria, em um numero misto, lembrando que "a/b".'

running = True
while(running):
        
    
    a = float(raw_input("\nInforme a: "))
    b = float(raw_input("Informe b: "))
 

    conj = ParaMisto(a,b)
    if conj !=False:
        print "A fração em numero misto:",conj[0],"|",conj[1],"/",conj[2]
    else:
        print "A fração tem de estar a>b e a divisão tem que ter resto."

    repeat_loop = str(raw_input("Deseja repetir? <y/n> "))
    if repeat_loop=="y":continue
    else: running=False
