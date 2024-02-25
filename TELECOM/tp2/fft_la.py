import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import sys
from pathlib import Path
import os

sys.path.append("~/Desktop/projet_l2_miage/TELECOM/tp2")

import gui_fft
#==============================================







if __name__ == '__main__':
    filename1 = "La3diapason.wav"
    filename2 =  "La3guitare.wav"
    filename3 =  "La3piano.wav"


    
    Fe,s_t = wavfile.read(filename3, mmap=False)

    # on ne fait la FFT que des N premiers samples
    N = 1024
    freqStep = Fe/N
    t = np.arange(N)/Fe
    s_t = s_t[0:N]
    s_f = np.fft.fft(s_t)   # Spectrum

    gui_fft.plot_fft(N, freqStep, Fe, t, s_t, s_f)
    plt.savefig("fft_example{}.png".format(N))
    plt.show()
