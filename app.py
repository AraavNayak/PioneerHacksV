# # import speech_recognition as sr
# # from os import path
# # from pydub import AudioSegment
# # import subprocess

# # # Initialize recognizer class
# # r = sr.Recognizer()
# # # audio object
# # path = '/content/New Recording 90.m4a'


# # if path[-3:] != 'wav':
# #   subprocess.call(['ffmpeg', '-i', path, 'audio.wav', '-y'])
# #   path = 'audio.wav'


# # audio = sr.AudioFile(path)
# # #read audio object and transcribe



# # with audio as source:
# #     audio = r.record(source)
# #     result = r.recognize_google(audio)

# # print(result)

# # # convert mp3 file to wav                                                       
# # sound = AudioSegment.from_mp3("transcript.mp3")
# # sound.export("transcript.wav", format="wav")


# # # transcribe audio file                                                         
# # AUDIO_FILE = "transcript.wav"

# # # use the audio file as the audio source                                        
# # r = sr.Recognizer()
# # with sr.AudioFile(AUDIO_FILE) as source:
# #         audio = r.record(source)  # read the entire audio file                  

# #         print("Transcription: " + r.recognize_google(audio))
# # # Function to analyze speech patterns
# # def analyze_speech(text):
# #     # You can use NLP libraries like spaCy, NLTK, or TextBlob for analyzing the transcribed text
# #     # Analyze vocabulary, fluency, volume, confidence, etc.
# #     # This part depends on your specific requirements and can involve various linguistic features and machine learning techniques.
# #     # For example, you could count unique words, measure the length of sentences, analyze sentiment, etc.
# #     # For simplicity, let's just return the transcribed text for demonstration purposes.
# #     return text

# # # Main function
# # def main():
# #     audio_file = "your_audio_file_path.wav"  # Provide the path to your audio file
# #     transcribed_text = sr.transcribe_audio(audio_file)
# #     if transcribed_text:
# #         analyzed_text = analyze_speech(transcribed_text)
# #         print("Transcribed Text:", transcribed_text)
# #         print("Analyzed Speech:", analyzed_text)

# # if __name__ == "__main__":
# #     main()


# import speech_recognition as sr
# import subprocess

# # Initialize recognizer class
# r = sr.Recognizer()
# # audio object
# path = '/content/New Recording 90.m4a'


# if path[-3:] != 'wav':
#   subprocess.call(['ffmpeg', '-i', path, 'audio.wav', '-y'])
#   path = 'audio.wav'


# audio = sr.AudioFile(path)
# #read audio object and transcribe



# with audio as source:
#     audio = r.record(source)
#     result = r.recognize_google(audio)

# print(result)


# import speech_recognition as sr
# from os import path
# from pydub import AudioSegment

# # convert mp3 file to wav                                                       
# sound = AudioSegment.from_mp3("transcript.mp3")
# sound.export("transcript.wav", format="wav")


# # transcribe audio file                                                         
# AUDIO_FILE = "transcript.wav"

# # use the audio file as the audio source                                        
# r = sr.Recognizer()
# with sr.AudioFile(AUDIO_FILE) as source:
#         audio = r.record(source)  # read the entire audio file                  

#         print("Transcription: " + r.recognize_google(audio))
# # Function to analyze speech patterns
# def analyze_speech(text):
#     # You can use NLP libraries like spaCy, NLTK, or TextBlob for analyzing the transcribed text
#     # Analyze vocabulary, fluency, volume, confidence, etc.
#     # This part depends on your specific requirements and can involve various linguistic features and machine learning techniques.
#     # For example, you could count unique words, measure the length of sentences, analyze sentiment, etc.
#     # For simplicity, let's just return the transcribed text for demonstration purposes.
#     return text

# # Main function
# def main():
#     audio_file = "your_audio_file_path.wav"  # Provide the path to your audio file
#     transcribed_text = sr.transcribe_audio(audio_file)
#     if transcribed_text:
#         analyzed_text = analyze_speech(transcribed_text)
#         print("Transcribed Text:", transcribed_text)
#         print("Analyzed Speech:", analyzed_text)

# if __name__ == "__main__":
#     main()

import speech_recognition as sr

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

def write_to_file(transcribed_text, analyzed_text, output_file):
    with open(output_file, "w") as file:
        file.write("Transcribed Text:\n")
        file.write(transcribed_text + "\n\n")
        file.write("Analyzed Speech:\n")
        file.write(analyzed_text + "\n")


# Main function
def main():
    audio_file = "test_audio.wav"  # Provide the path to your audio file
    transcribed_text = transcribe_audio(audio_file)
    if transcribed_text:
        analyzed_text = analyze_speech(transcribed_text)
        print("Transcribed Text:", transcribed_text)
        print("Analyzed Speech:", analyzed_text)

if __name__ == "__main__":
    main()
