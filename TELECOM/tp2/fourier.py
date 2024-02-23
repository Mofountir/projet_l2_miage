import math
import matplotlib.pyplot as plt
import numpy as np
import sys

sys.path.append("/users/etudiant/f/fm306941/l2_miage/TELECOM/tp1")

import tp1_0_stud

# Accédez aux fonctions et variables du fichier importé via l'alias `tp1`
# ...



"""=============================================
"""


def an(n,A):
    if n % 2== 0:
        return 0
    return 8*A/((math.pi*n)**2)

def bn():
    return 0

def make_st(A=1.0, f=440.0, fe=8000.0, nmax=0, d=1.0):
    """
        Creer un signal s(t) de fourier
    """
    
    N = int(d*fe)
    te = 1.0/fe
    sig_t = [0.0]*N
    sig_s = [0.0]*N
    
    
    lan = [0.0]
    lbn = [0.0]
    n = 1 
    while n < nmax:         # pour chaque harmonique... on ajoute sa contribution 
        lan.append(an(n,A))
        lbn.append(bn())
        n+=1

    for i in range(N): # pour chaque sample i
        t = i*te    #instant correspondant 
        sig_t[i] = t
        n = 1 #calcul de la valeur sample 
        while n < nmax:         # pour chaque harmonique... on ajoute sa contribution 
            sig_s[i] += lan[n] * math.cos(2*math.pi*n*f*t) + lbn[n] * math.sin(2*math.pi*n*f*t)
            n+=1


    return sig_t, sig_s, lan, lbn










if __name__ == '__main__':
    #paramètre signal

    a=1.5
    f=750.0
    fe=8000
    nmax=32
    d=3*1/f 

    

    # Generation du signal fourier

    x1,yS,lan,lbn = make_st(a,f,fe,nmax,d) #signaux
    n_array = [i for i in range(nmax)] # les harmoniques
    
    # Representation graphique

    fig,ax = plt.subplots(3)

    tp1_0_stud.plot_on_ax(ax[0],x1,yS,f"Sin Wave1 : a={a}, f={f}, fe={fe}, nmax={nmax}, d={d}", format="bo-")
    tp1_0_stud.decorate_ax(ax[0],"S(kte)")
    
    tp1_0_stud.plot_on_ax(ax[1],n_array,lan,f"an de S(kte): a={a}, f={f}, fe={fe}, nmax={nmax}, d={d}", format="go-")
    tp1_0_stud.decorate_ax(ax[1],"an de S(kte)")

    tp1_0_stud.plot_on_ax(ax[2],n_array,lbn,f"bn de S(kte): a={a}, f={f}, fe={fe}, nmax={nmax}, d={d}", format="go-")
    tp1_0_stud.decorate_ax(ax[2],"bn de S(kte)")
    

    plt.savefig("./basic_sin.png")
    plt.show()



    







    




