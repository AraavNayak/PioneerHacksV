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
import pyaudioconvert as pac
import soundfile
import wave

UPLOAD_FOLDER = 'files'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to transcribe audio file
def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)  # Record the audio file
        try:
            text = recognizer.recognize_google(audio_data)  # Use Google Web Speech API for transcription
            return text
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand the audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")
            return None

# Function to analyze speech patterns
def analyze_speech(text):
    # You can use NLP libraries like spaCy, NLTK, or TextBlob for analyzing the transcribed text
    # Analyze vocabulary, fluency, volume, confidence, etc.
    # This part depends on your specific requirements and can involve various linguistic features and machine learning techniques.
    # For example, you could count unique words, measure the length of sentences, analyze sentiment, etc.
    # For simplicity, let's just return the transcribed text for demonstration purposes.
    return text

def write_to_file(transcribed_text, output_file):
    with open(output_file, "w") as file:
        file.write("Transcribed Text:\n")
        file.write(transcribed_text + "\n\n")
        file.write("Analyzed Speech:\n")

# Main function
def main():
    
   # audio_file = "files/8d2e5f6d-3181-47cb-b473-9d5b27344a2e.wav"  # Provide the path to your audio file
    audio_file = "audio_files/MinecraftAudio.wav"  # Provide the path to your audio file
    output_file = "output.txt"  # Provide the path for the output text file

    transcribed_text = transcribe_audio(audio_file)
    if transcribed_text:
        analyzed_text = analyze_speech(transcribed_text)
        print("Transcribed Text:", transcribed_text)
        write_to_file(transcribed_text, output_file)
        #print("Analyzed Speech:", analyzed_text)

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
    file_name = f"test{str(num)}.mp3" #shine chang here
    full_file_name = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
    print(full_file_name)
    file.save(full_file_name)
    #convert to .wav
    subprocess.run(["ffmpeg", "-i", full_file_name, os.path.join(app.config['UPLOAD_FOLDER'], "asdfasdf.wav")]) 
    return '<h1>Success</h1>'

def get_most_common_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Convert all words to lowercase and extract words using regular expression
    words = re.findall(r'\b\w+\b', text.lower())

    # Count the occurrences of each word
    word_counts = Counter(words)

    # Get the 10 most common words
    most_common_words = word_counts.most_common(10)

    return most_common_words

def visualize(path: str):
   
    # reading the audio file

    

    # Read and rewrite the file with soundfile
    data, samplerate = soundfile.read(path)



    soundfile.write(path, data, samplerate)

    # Now try to open the file with wave
    with wave.open(path) as raw:
        print('File opened!')
        # raw = wave.open(path)
        
        # reads all the frames 
        # -1 indicates all or max frames
        signal = raw.readframes(-1)
        signal = np.frombuffer(signal, dtype ="int16")
        
        # gets the frame rate
        f_rate = raw.getframerate()
    
        # to Plot the x-axis in seconds 
        # you need get the frame rate 
        # and divide by size of your signal
        # to create a Time Vector 
        # spaced linearly with the size 
        # of the audio file
        time = np.linspace(
            0, # start
            len(signal) / f_rate,
            num = len(signal)
        )
    
        # using matplotlib to plot
        # creates a new figure
        plt.figure(1)
        
        # title of the plot
        plt.title("Amplitude (dB)")
        
        # label of x-axis
        plt.xlabel("Time")
        
        # actual plotting
        plt.plot(time, signal)
        
        # shows the plot 
        # in new window
        plt.show()
    
        # you can also save
        # the plot using
        # plt.savefig('filename')

if __name__ == "__main__":
    file_path = 'output.txt'  # Replace with the path to your text file
    common_words = get_most_common_words(file_path)

    print("Top 10 most common words (case-insensitive):")
    for word, count in common_words:
        print(f"{word}: {count} times")
    
    grah = len(os.listdir('files'))
    print("LENGTH" + str(grah))
    # path = 'files/test.wav'
    path = 'files/asdfasdf.wav'
    visualize(path)

    #app.run()
    main()
