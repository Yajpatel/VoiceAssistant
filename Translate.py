import speech_recognition as sr
import pyttsx3 as tts
import googletrans
# from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import time

from deep_translator import GoogleTranslator

from translator import translator
#####Recognizer is a class which captures the audio 
listener = sr.Recognizer()

##### to start the text to speech library
engine = tts.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(msg):
    engine.say(msg)
    engine.runAndWait()


async def translate_text(translator, query, toconvert):
    result = await translator.translate(query, src="auto", dest=toconvert)
    return result.text

def translate():
    try:
        with sr.Microphone() as source:
            print("Speak what you want to translate....")
            talk("Speak what you want to translate....")

            #Listen for sentence to translate
            spoken = listener.record(source, duration=10)
            query = listener.recognize_google(spoken).lower()

            print("############################## Languages available ######################################")
            print(googletrans.LANGUAGES)
            ##########################################################
            print(f"to translate: {query}")
            print("In which Language You want to translate")
            
            
            
            toconvert = input("enter code: ") 
            translated_text = GoogleTranslator(source='auto', target=toconvert).translate(query)
            print(translated_text)
            # translated_text = text_to_translate.text
            try:
                speakgl = gTTS(text=translated_text,lang=toconvert,slow=True)
                speakgl.save("voice.mp3")
                playsound("voice.mp3")
                # time.sleep(5)
            except Exception as e:
                print("unable to translate")
                print(e)
    except Exception as e:
        print(e)
        return None
    
    
    