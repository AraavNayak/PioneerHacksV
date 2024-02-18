import speech_recognition as sr
import subprocess
import ffmpeg

# Initialize recognizer class                                       
r = sr.Recognizer()
# audio object
path = '/Users/AraavNayak/Documents/GitHub/PioneerHacksV/files/055d6158-f16e-47f1-b2e2-53c07a6e30e2.mp3'    


if path[-3:] != 'wav':
  subprocess.call(['ffmpeg', '-i', path, 'audio.wav', '-y'])
  path = 'audio.wav'


audio = sr.AudioFile(path)
#read audio object and transcribe



with audio as source:
    audio = r.record(source)                  
    result = r.recognize_google(audio)
    
print(result)
print('Done?')