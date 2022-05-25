# Import dependencies
import speech_recognition as sr
import pyttsx3 as tts

# Create a listener
listener = sr.Recognizer()
engine = tts.init()

# Create a text to speech engine and configure the voice

# Speech rate
engine.setProperty('rate', 200)

# Speech volume (between 0 and 1)
engine.setProperty('volume',1.0)

# Speech voice (0 for male, 1 for female)
voices = engine.getProperty('voices')
print(len(voices))
engine.setProperty('voice', voices[0].id)

# Main process
try:
    with sr.Microphone() as source:
        # Capture the voice
        print("Listening...")
        voice = listener.listen(source)
        # Use the Google API to interpretate the voice command
        command = listener.recognize_google(voice)
        command = command.lower()
        print(command)
        engine.say("Recibido")
        engine.runAndWait()
except:
    pass
