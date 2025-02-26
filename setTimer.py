import speech_recognition as sr
import pyttsx3 as tts
import requests
#####3 Recognizer is a class which captures the audio 
listener = sr.Recognizer()

##### to start the text to speech library 
engine = tts.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(msg):
    engine.say(msg)
    engine.runAndWait()

def take_command_for_setTimer():
    try:
        with sr.Microphone() as source:
            print("Listening to set Timer...")

            # Listen for the city name after "Please tell me the city name" prompt
            spoked = listener.record(source, duration=10)
            time = listener.recognize_google(spoked).lower()
            return time
    except Exception as e:
        print(e)
        return None
    
def settime(time):
    pass
