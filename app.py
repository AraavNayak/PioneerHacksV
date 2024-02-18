import speech_recognition as sr
import subprocess
import os
import uuid
from collections import Counter
import re
from flask import Flask, flash, request, redirect, render_template
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
import speech_recognition as sr
import wave
from pydub import AudioSegment
import subprocess
import soundfile
import wave
import numpy as np
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from tone import get_tone_graph
import librosa
import librosa.display
            
x = np.arange(0, 2*np.pi, 0.1)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Sinusoid')

fig.savefig('static/cosine.png')

# html = '<html>' + '<img src=\'data:image/png;base64,{}\'>'.format(encoded) + '</html>'

# with open('templates/index.html','w') as f:
#     f.write(html)

UPLOAD_FOLDER = 'files'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    file_path = 'output.txt'  # Replace with the path to your text file
    common_words = get_most_common_words(file_path)
    return render_template('index.html', list_to_send=common_words)


@app.route('/save-record', methods=['POST'])
def save_record():
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    num = len(os.listdir('files'))
    u = "test" + str(num)
    file_name = u + ".mp3" #shine chang here
    full_file_name = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
    print(full_file_name)
    file.save(full_file_name)
    subprocess.run(["ffmpeg", "-i", full_file_name, os.path.join(app.config['UPLOAD_FOLDER'], u + ".wav")])
    main(u + ".wav")
    return '<h1>Success</h1>'

def get_most_common_words(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        text = file.read()

    # Convert all words to lowercase and extract words using regular expression
    words = re.findall(r'\b\w+\b', text.lower())

    # Count the occurrences of each word
    word_counts = Counter(words)

    # Get the 10 most common words
    most_common_words = word_counts.most_common(10)

    return most_common_words

# def visualize(path: str):
   
#     # reading the audio file

    

#     # Read and rewrite the file with soundfile
#     data, samplerate = soundfile.read(path)



#     soundfile.write(path, data, samplerate)

#     # Now try to open the file with wave
#     with wave.open(path) as raw:
#         print('File opened!')
#         # raw = wave.open(path)
        
#         # reads all the frames 
#         # -1 indicates all or max frames
#         signal = raw.readframes(-1)
#         signal = np.frombuffer(signal, dtype ="int16")
        
#         # gets the frame rate
#         f_rate = raw.getframerate()
    
#         # to Plot the x-axis in seconds 
#         # you need get the frame rate 
#         # and divide by size of your signal
#         # to create a Time Vector 
#         # spaced linearly with the size 
#         # of the audio file
#         time = np.linspace(
#             0, # start
#             len(signal) / f_rate,
#             num = len(signal)
#         )
    
#         # using matplotlib to plot
#         # creates a new figure
#         plt.figure(1)
        
#         # title of the plot
#         plt.title("Amplitude (dB)")
        
#         # label of x-axis
#         plt.xlabel("Time")
        
#         # actual plotting
#         plt.plot(time, signal)
        
#         # shows the plot 
#         # in new window
#         plt.savefig('static/amplitude.png')
    
#         # you can also save
#         # the plot using
#         # plt.savefig('filename')

if __name__ == "__main__":
    file_path = 'output.txt'  # Replace with the path to your text file
    common_words = get_most_common_words(file_path)

    print("Top 10 most common words (case-insensitive):")
    for word, count in common_words:
        print(f"{word}: {count} times")
    
    # path = 'files/test.wav'
 
    # visualize(path)
        


# # Function to get audio duration
def get_audio_duration(audio_file):
    with wave.open(audio_file, 'rb') as wf:
        return wf.getnframes() / float(wf.getframerate())

# # Function to transcribe audio file along with timestamps
def transcribe_audio_with_timestamp(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)  # Record the audio file
        audio_duration = get_audio_duration(audio_file)
        try:
            # Use Google Web Speech API for transcription
            transcribed_text = recognizer.recognize_google(audio_data)
            
            # Calculate timestamps
            transcribed_text_with_timestamp = ""
            current_timestamp = 0
            words_count = 0
            
            for word in transcribed_text.split():
                transcribed_text_with_timestamp += f"{word} "
                words_count += 1
                if words_count % 3 == 0:  # Add timestamp after every 3 words
                    transcribed_text_with_timestamp += f"[{int(current_timestamp)}] "
                current_timestamp += audio_duration / len(transcribed_text.split())  # Increment timestamp based on audio duration
            
            # Add the final timestamp if the last set of words is not perfectly divisible by 3
            if words_count % 3 != 0:
                transcribed_text_with_timestamp += f"[{int(current_timestamp)}] "
            
            return transcribed_text_with_timestamp.strip()
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand the audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")
            return None

# # Function to analyze speech patterns
# def analyze_speech(text):
#     # Placeholder for speech analysis
#     return text

# Function to write transcribed and analyzed speech to a text file
def write_to_file(transcribed_text, analyzed_text, output_file):
    with open(output_file, "w") as file:
        file.write("Transcribed Text with Timestamps:\n")
        file.write(transcribed_text + "\n")
        # file.write("\nAnalyzed Speech:\n")
        # file.write(analyzed_text + "\n")

# # Main function
def main(file_name):
    audio_file = "files/"+file_name  # Provide the path to your audio file
    output_file = "output_files/output.txt"  # Provide the path for the output text file
    transcribed_text = transcribe_audio_with_timestamp(audio_file)
    if transcribed_text:
        # analyzed_text = analyze_speech(transcribed_text)
        print("Transcribed Text with Timestamps:")
        print(transcribed_text)
        # print("Analyzed Speech:", analyzed_text)
        write_to_file(transcribed_text, "", output_file)
        print("Output written to", output_file)
    get_most_common_words(audio_file)  
    print(audio_file)
    pause_segments, y, sr, energy_smoothed = detect_pauses(audio_file)
    if pause_segments:
        print("Pauses detected in the following intervals:")
        for segment in pause_segments:
            print(f"- From {segment[0]:.2f} to {segment[1]:.2f} seconds")
    else:
        print("No pauses detected.")

    plot_waveform_with_pauses(y, sr, pause_segments, energy_smoothed)

def detect_pauses(audio_file, threshold=0.01, min_pause_duration=0.2):
    # Load the audio file
    y, sr = librosa.load(audio_file)

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
    plt.savefig('static/amplitude.png')
    

if __name__ == "__main__":
    #main()

    app.run()
