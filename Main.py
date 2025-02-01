import speech_recognition as sr
import pyttsx3 as tts
import pywhatkit as yt
import datetime as time
import wikipedia as book
import time
#####3 Recognizer is a class which captures the audio 
listener = sr.Recognizer()

##### to start the text to speech library
engine = tts.init()
engine.say("hello")
engine.runAndWait()
##### Flag to check if it's the first time running
first_run = True

def talk(msg):
    engine.say(msg)
    engine.runAndWait()
    
def take_command():
    global first_run
    try:
        with sr.Microphone() as source:
            ##### Only says once if it's the first run
            if first_run:
                engine.say("Hi, I am your personal assistant")
                engine.runAndWait()
                first_run = False

            print("Say Anything........")

            # listen is a method of recognizer class which is used to capture audio
            ####### it captures audio until it detect silence or until provided time
            # listener.energy_threshold = 200
            spoked = listener.record(source,duration=10)
            text = listener.recognize_google(spoked).lower()
            if "alexa" in text:
                print("Processing...")
                text = text.replace('alexa', "").strip()
                talk(text)
                return text
            else:
                print("Sorry, I could not get that.")
                return None
    except Exception as e:
        print(e)


def run_alexa():
    command = take_command()
    if command:
        try:
            if "snakegame" or "game" in command:
                # import game
                pass
            elif "youtube" in command:
                command = command.replace('youtube', "").strip()
                command = command.replace('play', "").strip()
                talk("Searching for..." + command)
                yt.playonyt(command)
                
                input("press Enter to continue..")
            elif "google" in command:
                command = command.replace('google',"").strip()
                yt.search(command)
                
                input("press Enter to continue..")
            elif 'time' in command:
                currtime = time.datetime.now().strftime('%I:%M %p')
                talk(currtime)
                print(currtime)
            elif 'who is' in command:
                command = command.replace("who is", "").strip()
                info = book.summary(command, 2)
                print(info)
                talk(info)
            elif 'what is' in command:
                command = command.replace("what is", "").strip()
                info = book.summary(command, 2)
                print(info)
                talk(info)
            elif 'exit' or 'stop' or 'bye' in command:
                talk("see you soon")
                exit()
        except Exception as e:
            print(e)
    else:
        print("I didn't catch that! Please try again!!")
        talk("I didn't catch that! Please try again!!")
        print("Please repeat the command.")
        talk("Please repeat the command.")

while True:
    run_alexa()