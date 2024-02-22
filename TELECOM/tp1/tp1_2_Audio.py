"""Ce code sert à:
    - convertir le signal en un son dans un fichier son.wav
"""

"""================================================"""

import struct, wave, math
import tp1_0_stud, tp1_1_Bruit

"""================================================"""
def write_a_wave_file(x,y,fn="son.wav"):

    nbcanal = 2 # Stério
    nbOctet = 1 # taille d'un échantillona, 1 octet = 8 bits
    fe = 44100 # fréquence d'échantillonnage
    nbEchantillon = len(x) # nombre d'echantillon

    wave_file = wave.open(fn, 'w')
    parametre = (nbcanal,nbOctet,fe,nbEchantillon,"NONE","not compressed") # tuple
    wave_file.setparams(parametre)

    # niveau max dans l’onde positive : +1 -> 255 (0xFF)    
    # niveau max dans l’onde negative : -1 -> 0 (0x00)
    # niveau sonore nul : 0 -> 127.5 (0x80 en valeur arrondi)

    print("La sinusoide devient un son ... ")

    for i in range(0,nbEchantillon):
        val = y[i]
        if val > 1.0:
            val = 1.0
        elif val < -1.0:
            val = -1.0

        val = int(127.5 + 127.5 * val)
        try:
            fr = struct.pack("BB", val, val) # unsigned int
        except struct.error as err:
            print(err)
            print("Sample {} = {}/{}".format(i,y[i],val))
        else:
            wave_file.writeframes(fr) # ecriture de la frame

    wave_file.close()




#---------------------------------------

def make_anoisysignal(a,f,fe,ph,d):

  #paramètre bruit gaussien

    m=0.0
    e=0.05

    #paramètre bruit impulse

    m1=0.0
    e1=1.6*a
    nbi=2
    di=1000

    # Generation du signal et du bruit

    x1,yS,yC,yCF,yDS,yTR=tp1_0_stud.make_signal(a,f,fe,ph,d) #signaux
    x2,yNW = tp1_1_Bruit.noise_white(x1,m,e) #bruit gaussien
    x3,yNImp = tp1_1_Bruit.noise_impulse(nbi, di, x1, m1, e1) #bruit impulse

    #Generation du signal bruité

    x4,ySBw = tp1_1_Bruit.signal_add(x1,yS,x2,yNW)
    x4,ySB = tp1_1_Bruit.signal_add(x4,ySBw,x3,yNImp)

    return x4,ySB

#=======================================

if __name__ == '__main__':


    # Generation du signal
    x,y = make_anoisysignal(a=100,f=200.0,fe=44100.0,ph=0,d=5)

    write_a_wave_file(x,y)

