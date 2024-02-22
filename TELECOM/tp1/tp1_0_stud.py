'''
File : tp1_0_stud.py

Creer un signal numerique et l'afficher
RMQ : On utilise ici le B,A,BA de Python. 

     Si vous savez faire mieux : objets ?, numpy ? ... SURTOUT lachez vous !!!!!
     car la solution "pythonique" n'est pas là :-( 
'''

import math
import matplotlib.pyplot as plt 

#---------------------------------------

def make_signal(a=1.0, f=440.0, fe=8000.0, ph=0, d=1.0):
    """
    Create a synthetic 'sine wave'
    """
    omega = 2*math.pi*f
    N = int(d*fe)
    te = 1.0/fe
     
    
    
    sig_t = [] 
    sig_s = []
    sig_sc = []
    sig_scf = []
    sig_ds = []
    sig_tr = []


    for i in range(N):
        t = te*i
        sig_t.append(t)
        sig_s.append(a*math.sin((omega*t)+ph)) # Signal sinisoïde
        sig_sc.append(sgn(math.sin((omega*t)+ph))) # Signal carré
        sig_scf.append(2*(2*math.floor(f*t)-math.floor(2*f*t))+1) # Signal carrée avec la formule Floor
        sig_ds.append(2*a*((f*t)-math.floor(f*t)-0.5)) # Signal dent de scie
        sig_tr.append(a*(4*(abs((f*t)-math.floor((f*t)+0.5)))-1.0)) # Signal triangle

    return sig_t, sig_s, sig_sc, sig_scf, sig_ds, sig_tr

#---------------------------------------
def sgn(x):
    res = -1 
    if x >= 0:
        res = 1
    return res
#---------------------------------------

#---------------------------------------

def plot_on_ax(ax, inx, iny, label, format='bo'):
    ax.plot(inx,iny,format,label=label)
    ax.set_xlabel('time (s)')
    ax.set_ylabel('voltage (V)')

#---------------------------------------

def decorate_ax(ax, title):
    ax.set_title(title)
    ax.grid(True)
    ax.legend()

#----------------------------------------

#=======================================

if __name__ == '__main__':
    a=3
    f=50
    fe=800
    ph=0
    d=0.08



    # Generation du signal
    x1,yS,yC,yCF,yDS,yTR=make_signal(a,f,fe,ph,d)
    
    # Representation graphique
    fig,ax = plt.subplots()
    plot_on_ax(ax,x1,yDS,f"Sin Wave1 : a={a}, f={f}, fe={fe}, ph={ph}, d={d}", format="-bo")
    
    decorate_ax(ax,"Une sinusoide")

    plt.savefig("./basic_sin.png")
    plt.show()
    
#=======================================
