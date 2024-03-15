import numpy as np 
import matplotlib.pyplot as plt
import coefs


"""========================================"""

def makeDTMF(N, freqStep, Fe, t, sig_s, sig_f): # t <=> sig_t

    sig_f = np.fft.fftshift(sig_f)      # middles the zero-point's axis
    sig_f = sig_f/N    # Normalization => ainsi le module ne dependra
                   
    freq = freqStep * np.arange(-N/2, N/2)  # ticks in frequency domain
    

    #=== Affichage console des valeurs des raies
    #for i,r in enumerate(list(sig_f)):
    #    print("Raie {} \t= \t{:.5g}".format(freq[i],r))

    # plot signal DTMF-------------------------------------------
    plt.figure(figsize=(8,8))
    plt.subplots_adjust(hspace=.6) # espace entre les figures

    plt.subplot(3,1,1)
    plt.plot(t, sig_s, '.-', label="N={}, fe={}".format(N,Fe))
    plt.grid(True)
    plt.legend()
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')
    plt.title('Signal DTMF')
    plt.axis('tight')

    # Plot spectral magnitude ------------------------------
    plt.subplot(3,1,2)
    plt.plot(freq, np.abs(sig_f), '.-b', label="freqStep={}".format(freqStep))
    plt.grid(True)
    plt.legend()
    plt.xlabel('Frequency')
    plt.ylabel('S(F) Magnitude (Linear)')   



def split_en_zeros(sig_f):

  sous_listes = []
  debut = 0
  for i, element in enumerate(sig_f):
    if element == 0:
      sous_listes.append(sig_f[debut:i])
      debut = i + 1
  # On ajoute la dernière sous-liste si elle n'est pas vide
  if debut < len(sig_f):
    sous_listes.append(sig_f[debut:])
  return sous_listes





    




"""========================================"""
if __name__ == '__main__':
    # lecture fichier phone.out
    sig_t, sig_s = np.loadtxt('phone.out')

    N = len(sig_t)
    Fe = 4000.
    
        
    freqStep = Fe/N




    
    
    # Calcul de la transformée de Fourier
    
    signal = split_en_zeros(sig_s)
    for digit in signal:
       for freq in digit:
            f_bas = np.min(digit)
            f_haut = np.min(digit)
            print(f"({f_bas},{f_haut})")

    
    
    sig_f = np.fft.fft(sig_s)
    
    

    
    
   

        

    makeDTMF(N, freqStep, Fe, sig_t, sig_s, sig_f) # affichage du signal DTMF

    plt.show()


