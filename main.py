# Import dependencies
import speech_recognition as sr

# Create a listener
listener = sr.Recognizer()

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
except:
    pass
