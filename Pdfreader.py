import speech_recognition as sr
import pyttsx3 as tts
import PyPDF2
# import docx

##### Recognizer is a class which captures the audio 
listener = sr.Recognizer()

engine = tts.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',100) # Slow down speech default is 200

def talk(msg):
    engine.say(msg)
    engine.runAndWait()

def takeCommandForPdf():
    try:
        with sr.Microphone() as source:
            print("Listening for file name...")

            spoked = listener.record(source, duration=5)
            filename = listener.recognize_google(spoked).lower()

            print(f"File {filename}")
            return filename
    except Exception as e:
        print(e)
        return None
    
    
def read_pdf(file_path):
    with open(file_path, "rb") as book:
        pdfreader = PyPDF2.PdfReader(book)
        for page in pdfreader.pages:
            text = page.extract_text()
            if text:
                engine.say(text)
                engine.runAndWait()

def read_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
        engine.say(text)
        engine.runAndWait()

# def read_docx(file_path):
#     doc = docx.Document(file_path)
#     text = "\n".join([para.text for para in doc.paragraphs])
#     engine.say(text)
#     engine.runAndWait()

def reader(file_path):
    if file_path.endswith(".pdf"):
        read_pdf(file_path)
    elif file_path.endswith(".txt") or file_path.endswith(".md"):
        read_txt(file_path)
    # elif file_path.endswith(".docx"):
    #     read_docx(file_path)
    else:
        print("Unsupported file format!")

# Example Usage
# from Main import 
# reader(file_path)