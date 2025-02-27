import speech_recognition as sr
import pyttsx3 as tts
import datetime as t
import os
import time
#####3 Recognizer is a class which captures the audio 
listener = sr.Recognizer()

##### to start the text to speech library 
engine = tts.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',130) # Slow down speech default is 200

def talk(msg):
    engine.say(msg)
    engine.runAndWait()

def setAlarm(): 
    talk("type time in given format")
    alarm_time = input("Enter alarm time in HH:MM format: ")
    try:
        alarm_hour, alarm_minute = map(int, alarm_time.split(":"))  # Convert to integers
        talk(f"Alarm set for {alarm_hour}:{alarm_minute}.")
        while True:
            now = t.datetime.now()
            print(now)
            if now.hour == alarm_hour and now.minute == alarm_minute:
                talk("Alaram ringing,sir")
                os.startfile("D:\Python-Project Sem-3\Individual\VoiceAssistant\Alarm.mp3")
                break
            time.sleep(10)  # Check every 30 seconds
    except Exception as e:
        print("Invalid time format. Please enter in HH:MM format.")