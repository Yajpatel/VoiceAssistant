import speech_recognition as sr
import pyttsx3 as tts
import pywhatkit as yt
import datetime
import wikipedia as book
import time
from Pdfreader import reader

import os
import pyautogui #for play pause mute   

import asyncio

#####3 Recognizer is a class which captures the audio 
listener = sr.Recognizer()

##### to start the text to speech library 
engine = tts.init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',150) # Slow down speech default is 200
# engine.say("hello")
# engine.runAndWait()
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
                talk("I am just a virtual assistant, so I don't have a gender. But you can call me whatever you like!")
                print("I am just a virtual assistant, so I don't have a gender. But you can call me whatever you like!")
            elif "open" in command or "launch":
                command = command.replace('open', "").strip()
                pyautogui.press('super')
                time.sleep(1)
                pyautogui.typewrite(command)
                time.sleep(2)
                pyautogui.press('enter')
            elif "youtube" in command:
                command = command.replace('youtube', "").strip()
                command = command.replace('play', "").strip()
                command = command.replace('search',"").strip()
                command = command.replace(' on ', "").strip()
                talk("Searching for..." + command)
                yt.playonyt(command)
                
                # input("press Enter to continue..")
            elif "google" in command:
                command = command.replace('on google',"").strip()
                command = command.replace('google',"").strip()
                command = command.replace('search',"").strip()
                command = command.replace('on', "").strip()
                yt.search(command)
            elif "whatsapp" in command:
                try:
                    phone_number = input("enter Time with starting with +91 than 10 digits:")  # Replace with recipient's number
                    message = input("enter message you want to send")
                    target_time = input("Enter time to send message in HH:MM format: ")
                    print("your message will be sent at ",target_time)
                    
                    while True:
                        current_time = datetime.datetime.now().strftime("%H:%M")
                        if current_time == target_time:
                            os.system("start whatsapp://send?phone=" + phone_number)

                            # Wait for WhatsApp to open
                            time.sleep(5)

                            # Type the message
                            pyautogui.write(message)

                            time.sleep(2)
                            # Press 'Enter' to send
                            pyautogui.press("enter")
                            break
                        time.sleep(1)
                except Exception as e:
                    print("msg not send ",e)
                
                
            elif 'time' in command:
                currtime = datetime.datetime.now().strftime('%I:%M %p')
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
            elif "set" in command or "set alarm" in command or "set alaram" in command:
                # from setTimer
                from Alarm import setAlarm
                setAlarm()
            elif "read pdf" in command or "pdf" in command or "text" in command or "file" in command or "read" in command:
                from Pdfreader import takeCommandForPdf
                talk("i will read for you. just Name the File you want to read")
                filename = takeCommandForPdf()
                # filename = filename.replace(" dot", ".")   # Edge case for "dot" at the end
                # filename = "".join(filename.split())  # Remove spaces
                # filename = "demo.txt"
                if filename:
                    file_path = f"VoiceAssistant\{filename}"
                    reader(file_path)
                else:
                    talk("i could not able to listen file name")
            elif "volume up" in command or "increase volume" in command:
                from Volume import volumeup
                volumeup()
                talk("volume increased")
            elif "volume down" in command or "decrease volume" in command:
                from Volume import volumedown
                volumedown()
                talk("volume decreased")
            elif "pause" in command or "stop" in command:
                pyautogui.press("k")
                talk("vedio paused")
            elif "play" in command:
                pyautogui.press("k")
                talk("vedio played")
            elif "mute" in command:
                pyautogui.press("m")
                talk("vedio muted")
            elif "unmute" in command:
                pyautogui.press("m")
                talk("vedio unmuted")
            elif "shutdown" in command:
                os.system("shutdown /s /t 3")
            elif "translate" in command:
                from Translate import translate
                asyncio.run(translate()) 
            elif "screenshot" in command:
                image = pyautogui.screenshot()
                image.save("ss.png")
            else:
                print("this functionality yet not added")
            
        except Exception as e:
            print(e)
    else:
        print("I didn't catch that! Please try again!!") 
        # talk("I didn't catch that! Please try again!!")
        print("Please repeat the command.")
        # talk(kk"Please repeat the command.")
        
while True:
    run_alexa()
    
    