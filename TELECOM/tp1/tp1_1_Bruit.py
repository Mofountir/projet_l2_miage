"""Ce code sert à:
    - céer un sinal bruit guaussien et impulsif 
    - les rajouter à une sinusoide pour avoir un signal bruité
"""

"""================================================"""

import tp1_0_stud
import math
import matplotlib.pyplot as plt
import numpy as np

"""================================================"""

def noise_white(x,m,e):
    bruit = np.random.normal(m,e,len(x))
    return x, bruit


def noise_impulse(nbi,di,x,m,e):
    # positions des impulsions
    positions = np.random.randint(0, len(x), nbi)
  
    # valeurs des impulsions
    valeurs = np.random.normal(m, e, nbi)
  
    bruit = np.zeros(len(x))

    for i in range(nbi):
        bruit[positions[i]:positions[i]+di+1] = valeurs[i]

    return x, bruit


def signal_add(x1,y1,x2,y2):
    if len(x1) != len(x2) or len(x2) != len(y2):
        raise ValueError("les tableau d'échantion doivent avoir la même taille")
    x = x1
    y  = y1 + y2
    
    return x, y


"""================================================"""

if __name__ == '__main__':
    #paramètre signal

    a=2
    f=50.0
    fe=1000
    ph=0
    d=0.08

    #paramètre bruit gaussien

    m=0
    e=0.2

    #paramètre bruit impulse

    m1=0
    e1=2*a
    nbi=2
    di=2

    # Generation du signal et du bruit

    x1,yS,yC,yCF,yDS,yTR=tp1_0_stud.make_signal(a,f,fe,ph,d) #signaux
    x2,yNW = noise_white(x1,m,e) #bruit gaussien
    x3,yNImp = noise_impulse(nbi, di, x1, m1, e1) #bruit impulse

    #Generation du signal bruité

    x4,ySBw = signal_add(x1,yS,x2,yNW)
    x4,ySB = signal_add(x4,ySBw,x3,yNImp)
    
    # Representation graphique

    fig,ax = plt.subplots(4)

    tp1_0_stud.plot_on_ax(ax[0],x1,yS,f"Sin Wave1 : a={a}, f={f}, fe={fe}, ph={ph}, d={d}", format="bo-")
    tp1_0_stud.decorate_ax(ax[0],"Une sinusoide")

    tp1_0_stud.plot_on_ax(ax[1],x2,yNW,f"Bruit blanc : Moyenne {m}, Ecart Type {e}", format = "g.-")
    tp1_0_stud.decorate_ax(ax[1],"Bruit gaussien")

    tp1_0_stud.plot_on_ax(ax[2],x3,yNImp,f"Bruit impulsif : Moyenne {m1}, Ecart Type {e1}", format="g.-")
    tp1_0_stud.decorate_ax(ax[2],"Bruit impulse")

    tp1_0_stud.plot_on_ax(ax[3],x4,ySB,"Sin Wave bruité","r.-")
    tp1_0_stud.decorate_ax(ax[3],"Une sinusoide bruité")






    plt.savefig("./basic_sin.png")
    plt.show()