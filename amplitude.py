import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt

def detect_pauses(audio_file, threshold=0.01, min_pause_duration=0.2):
    # Load the audio file
    y, sr = librosa.load("files/test54.wav")

    # Apply aggressive noise reduction if needed
    y = librosa.effects.preemphasis(y)

    # Compute the root mean square (RMS) energy of the audio signal
    energy = librosa.feature.rms(y=y)

    # Smooth the energy curve with a moving average filter
    energy_smoothed = np.convolve(energy[0], np.ones(3)/3, mode='same')

    # Find segments with energy below the threshold (likely pauses)
    pause_segments = []
    is_pause = False
    segment_start = 0
    for i in range(len(energy_smoothed)):
        if energy_smoothed[i] < threshold:
            if not is_pause:
                segment_start = i
                is_pause = True
        else:
            if is_pause:
                if (i - segment_start) / sr >= min_pause_duration:
                    pause_segments.append((segment_start / sr, i / sr))
                is_pause = False

    return pause_segments, y, sr, energy_smoothed

def plot_waveform_with_pauses(y, sr, pause_segments, energy_smoothed):
    plt.figure(figsize=(12, 8))

    # Plot waveform
    plt.subplot(2, 1, 1)
    librosa.display.waveshow(y, sr=sr, alpha=0.5)
    for segment in pause_segments:
        plt.axvspan(segment[0], segment[1], color='r', alpha=0.3)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Waveform with Pauses')

    # Convert energy to decibels (dB)
    energy_dB = librosa.amplitude_to_db(energy_smoothed, ref=np.max)

    # Plot volume vs time graph in decibels
    plt.subplot(2, 1, 2)
    times = np.linspace(0, len(y) / sr, len(energy_dB))
    plt.plot(times, energy_dB + 45)
    plt.ylim(0, 50)  # Set y-axis range
    plt.xlabel('Time (s)')
    plt.ylabel('Volume (dB)')
    plt.title('Volume vs Time (|dB|)')

    plt.tight_layout()
    plt.show()

#  usage
audio_file = "files/test19.wav"
pause_segments, y, sr, energy_smoothed = detect_pauses(audio_file)
if pause_segments:
    print("Pauses detected in the following intervals:")
    for segment in pause_segments:
        print(f"- From {segment[0]:.2f} to {segment[1]:.2f} seconds")
else:
    print("No pauses detected.")

plot_waveform_with_pauses(y, sr, pause_segments, energy_smoothed)