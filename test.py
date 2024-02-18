import assemblyai as aai
import pyaudio

aai.settings.api_key = "71ef0a9574644b27b45cca1a8c8a86d6"

# Audio settings
CHUNK = 1024  # Number of frames per audio chunk
FORMAT = pyaudio.paInt16  # Audio format
CHANNELS = 1  # Number of channels (mono)
RATE = 16000  # Sample rate

# instance of PyAudio to access audio input
p = pyaudio.PyAudio()

# opening stream to record audio from the microphone
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# creating a transcriber object
transcriber = aai.Transcriber()

# start real-time transcription stream

stream_id = transcriber.start_stream(config=aai.TranscriptionConfig(speaker_labels=True))

try:
    while True:
        # Read a chunk of audio data from the microphone
        data = stream.read(CHUNK)

        # Send the audio data to AssemblyAI for transcription
        transcriber.send_audio(stream_id, audio_data=data)

        # Check for transcription results
        results = transcriber.get_stream_results(stream_id)

        # Print the transcribed text in real-time
        for utterance in results.utterances:
            print(f"Speaker {utterance.speaker}: {utterance.text}")

except KeyboardInterrupt:
    # Stop the stream and close the audio stream
    transcriber.stop_stream(stream_id)
    stream.stop_stream()
    stream.close()
    p.terminate()
