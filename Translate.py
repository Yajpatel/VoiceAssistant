import speech_recognition as sr
import pyttsx3 as tts
import googletrans
import time
import asyncio
import gtts
import playsound
import os

print(googletrans.LANGUAGES)
#####Recognizer is a class which captures the audio 
listener = sr.Recognizer()

##### to start the text to speech library
engine = tts.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(msg):
    engine.say(msg)
    engine.runAndWait()


async def translate():
    try:
        with sr.Microphone() as source:
            print("Speak what you want to translate....")
            talk("Speak what you want to translate....")
            ##################################################
            spoken = listener.record(source,duration=5)
            query = listener.recognize_google(spoken,language="en")
            
            ############################################
            print(query)
            toconvert = input("enter code: ") 
            #########################################################
            translator = googletrans.Translator()
            translated_text = await translator.translate(query,dest=toconvert)
            time.sleep(3)
            print(translated_text.text)
            
            ######################################################
            convertedaudio = gtts.gTTS(translated_text.text,lang=toconvert)
            convertedaudio.save("hello.mp3")
            
            time.sleep(3)
            playsound.playsound("hello.mp3")
            time.sleep(3)
            os.remove("hello.mp3")
    except Exception as e:
        print(e)
        








#############################################################################
#############################################################################

            # for example
            # query = "bonjour comment allez-vous" toconvert = "en" #### Good morning, how are you doing
            # query = "hello how are you"
            # toconvert = input("enter code: ") 













































# import speech_recognition as sr
# import pyttsx3 as tts
# import googletrans
# # from googletrans import Translator
# from gtts import gTTS
# from playsound import playsound
# import time

# from deep_translator import GoogleTranslator

# from translator import translator
# #####Recognizer is a class which captures the audio 
# listener = sr.Recognizer()

# ##### to start the text to speech library
# engine = tts.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice',voices[1].id)

# def talk(msg):
#     engine.say(msg)
#     engine.runAndWait()


# def translate():
#     try:
#         with sr.Microphone() as source:
#             print("Speak what you want to translate....")
#             talk("Speak what you want to translate....")

#             #Listen for sentence to translate
#             spoken = listener.record(source, duration=10)
#             query = listener.recognize_google(spoken).lower()

#             print("############################## Languages available ######################################")
#             print(googletrans.LANGUAGES)
#             ##########################################################
#             print(f"to translate: {query}")
#             print("In which Language You want to translate")
            
            
            
#             toconvert = input("enter code: ") 
#             translated_text = GoogleTranslator(source='auto', target=toconvert).translate(query)
#             print(translated_text)
#             # translated_text = text_to_translate.text
#             try:
#                 speakgl = gTTS(text=translated_text,lang=toconvert,slow=True)
#                 speakgl.save("voice.mp3")
#                 playsound("voice.mp3")
#                 # time.sleep(5)
#             except Exception as e:
#                 print("unable to translate")
#                 print(e)
#     except Exception as e:
#         print(e)
#         return None
    
    
