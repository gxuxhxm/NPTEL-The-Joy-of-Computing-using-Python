import speech_recognition as sr

# Step 1: Create an audio file and convert it to .wav
# In this example, you need to have an audio file named "kangal-irandal.wav".

# Step 2: Import Speech Recognition and Initialize the Program
recognizer = sr.Recognizer()

# Step 3: Process the Audio File
audio_file = "Listening and reading practice (320  wav file.wav"  # Provide the path to your .wav audio file
with sr.AudioFile(audio_file) as source:
    try:
        # Recognize the audio using Google's speech recognition
        audio_data = recognizer.record(source)  # Record the audio data from the source
        audio_recognized = recognizer.recognize_google(audio_data)
        print("Recognized Text: " + audio_recognized)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition; {0}".format(e))
