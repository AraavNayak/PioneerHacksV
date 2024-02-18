# required libs: numpy, matplotlib, scipy
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

plt.rcParams['figure.dpi'] = 100
plt.rcParams['figure.figsize'] = (9, 7)

sampFreq, sound = wavfile.read('data/noise_a3s.wav')