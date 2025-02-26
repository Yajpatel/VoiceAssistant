import speech_recognition as sr
import pyttsx3 as tts
import pywhatkit as yt
import datetime as t
import wikipedia as book
import time
from Pdfreader import reader
# import requests
# from bs4 import BeautifulSoup

#####3 Recognizer is a class which captures the audio 
listener = sr.Recognizer()

##### to start the text to speech library 
engine = tts.init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',130) # Slow down speech default is 200
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
            spoked = listener.record(source,duration=5)
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
    print(command)
    if command:
        try:
            if "what is your name" in command or "who are you" in command:
                talk("I am Personal Voice Assistant coded by Yaj")
                print("I am Personal Voice Assistant coded by Yaj")
            elif "what is your gender" in command or "are you male or female" in command:
                pass
            elif "youtube" in command:
                command = command.replace('youtube', "").strip()
                command = command.replace('play', "").strip()
                command = command.replace('search',"").strip()
                command = command.replace('on', "").strip()
                talk("Searching for..." + command)
                yt.playonyt(command)
                
                input("press Enter to continue..")
            elif "google" in command:
                command = command.replace('on google',"").strip()
                command = command.replace('google',"").strip()
                command = command.replace('search',"").strip()
                command = command.replace('on', "").strip()
                yt.search(command)

                input("press Enter to continue..")
            elif 'time' in command:
                currtime = t.datetime.now().strftime('%I:%M %p')
                talk(currtime)
                print(currtime)
            elif 'who is' in command:
                command = command.replace("who is", "").strip()
                info = book.summary(command, 2)
                print(info)
                talk(info)
            elif "weather forecast" in command or "temperature" in command or "weather" in command:
                talk("Please tell me the city or state name. of which you want to know weather forecast")
                from Temperature import take_command_for_temperature,get_temperature
                city = take_command_for_temperature()
                if city:
                    get_temperature(city)  # Fetch the temperature for the city
            elif 'what is' in command:
                command = command.replace("what is", "").strip()
                info = book.summary(command, 1)
                print(info)
                talk(info)
            elif "set" in command or "set alaram" in command:
                # from setTimer
                talk("for how long do you want to set Timer")
                from setTimer import settime,take_command_for_setTimer
                command = take_command_for_setTimer()
                if command:
                    settime(time)
            elif "read pdf" in command or "pdf" in command or "text" in command or "file" in command or "read" in command:
                from Pdfreader import takeCommandForPdf
                talk("i will read for you. just Name the File you want to read")
                filename = takeCommandForPdf()
                filename = filename.replace(" dot", ".")   # Edge case for "dot" at the end
                filename = "".join(filename.split())  # Remove spaces
                # filename = "demo.txt"
                if filename:
                    file_path = f"VoiceAssistant\{filename}"
                    reader(file_path)
                else:
                    talk("i could not able to listen file name")
            else:
                print("this functionality yet not added")
        except Exception as e:
            print(e)
    else:
        print("I didn't catch that! Please try again!!")
        talk("I didn't catch that! Please try again!!")
        print("Please repeat the command.")
        talk("Please repeat the command.")
    
while True:
    run_alexa()