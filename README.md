# VoiceAssistant

###### pyttsx3 key methods
pyttsx3.init(): Initializes the TTS engine.
engine.setProperty('rate', rate): Adjusts the speed of the speech.
engine.setProperty('volume', volume): Adjusts the volume of the speech.
engine.getProperty('voices'): Lists available voices.   
engine.setProperty('voice', voice): Sets the desired voice (e.g., male or female).
engine.say(text): Queues the text to be spoken.
engine.runAndWait(): Processes the commands and speaks the text.
    : Saves the speech to an audio file.


# for i, voice in enumerate(voices):
#     print(f"Voice {i + 1}:")
#     print(f" - Name: {voice.name}")
#     print(f" - ID: {voice.id}")
#     print(f" - Languages: {voice.languages}")
#     print(f" - Gender: {voice.gender}")
#     print(f" - Age: {voice.age}")
# engine.setProperty('voices',voices[1].id)

%Y: 4-digit year (e.g., 2025).
%m: 2-digit month (e.g., 01 for January).
%d: Day of the month (e.g., 17).
%H: Hour (24-hour clock, e.g., 15).
%I: Hour (12-hour clock, e.g., 03).
%M: Minutes (e.g., 45).
%S: Seconds (e.g., 30).
%p: AM/PM.