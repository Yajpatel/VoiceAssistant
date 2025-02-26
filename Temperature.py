import speech_recognition as sr
import pyttsx3 as tts
import requests
#####Recognizer is a class which captures the audio 
listener = sr.Recognizer()

##### to start the text to speech library
engine = tts.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(msg):
    engine.say(msg)
    engine.runAndWait()

def take_command_for_temperature():
    try:
        with sr.Microphone() as source:
            print("Listening for the city name...")

            # Listen for the city name after "Please tell me the city name" prompt
            spoked = listener.record(source, duration=10)
            city = listener.recognize_google(spoked).lower()

            print(f"City: {city}")
            return city
    except Exception as e:
        print(e)
        return None
def get_temperature(city):
    api_key = "32a8b860433f2447f0c1efd616975d47"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temperature = data["main"]["temp"]
        talk(f"The current temperature in {city} is {temperature}°C.")
        print(temperature)
    else:
        talk(f"Sorry, I couldn't fetch the temperature for {city}. Please check the city name.")
