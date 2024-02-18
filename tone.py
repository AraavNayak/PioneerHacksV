import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

def get_tone_graph(file_name):
    plt.rcParams['figure.dpi'] = 100
    plt.rcParams['figure.figsize'] = (9, 7)

    # input the recorded wav file
    sampFreq, sound = wavfile.read(file_name);

    # sampling rate for MinecraftAudio.wav = 48000 (samples per second)
    # print(sound.dtype, sampFreq)

    # making a nice range for our own use
    print(len(sound))

    length_in_s = sound.shape[0] / sampFreq
    time = np.arange(sound.shape[0]) / sound.shape[0] * length_in_s

    dom_freq = []

    samp_range = int(sampFreq/10)
    count = 0

    while count < len(sound):
        
        if (count+samp_range > len(sound)):
            break
        sample = sound[count: int(count+samp_range) ]
        fft_spectrum = np.fft.rfft(sample)
        freq = np.fft.rfftfreq(sample.size, d=1./samp_range)
        

        fft_spectrum_abs = np.abs(fft_spectrum)
        # plt.plot(freq[count:int(count + samp_range)], fft_spectrum_abs[count:int(count + samp_range)])
        # plt.xlabel("frequency, Hz")
        # plt.ylabel("Amplitude, units")
        # plt.show()

        fft_data = np.fft.fft(sample)
        freqs = np.fft.fftfreq(len(sample))
        
        peak_coefficient = np.argmax(np.abs(fft_data))
        peak_freq = freqs[peak_coefficient]
        
        dom_freq.append(abs(peak_freq * sampFreq))
        # g = 0
        # g_freq = 0
        # index = 0
        # for i,f in enumerate(fft_spectrum_abs[count:int(count + samp_range)]):
        #     if (np.round(f) > g):
        #         g = f
        #         g_freq = freq[i]
        #         print(freq[i])

        # dom_freq.append(g_freq)
        
        count += samp_range
    new_time = []
    t = 0
    for i in range(len(dom_freq)):
        new_time.append(t)
        t += 0.1

    dom_freq = np.divide(dom_freq, 10)

    plt.plot(new_time, dom_freq)
    plt.title("Tone (Frequency) Analysis")
    plt.xlabel("time (s)")
    plt.ylabel("dominant frequency - tone in Hz (adjusted)")
    plt.savefig('static/tone.png')


    
    





