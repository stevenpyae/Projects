import re
import pyttsx3
import speech_recognition

def main():
    print("Welcome to Jarvis Program")
    #Initialise the Jarvis program
    engine = pyttsx3.init()
    engine.setProperty('rate', 145)
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

    #Initialise Listening
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Jarvis is Listening: ")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    #Recognize speech using Google Speech Recognition
    words = recognizer.recognize_google(audio)

    matches = re.search("Friday", words)
    if matches:
        engine.say("Yes Sir!, I am listening")
        engine.runAndWait()
    else:
        engine.say("It is good to see you work Sir")
        engine.runAndWait()

    

if __name__ == "__main__":
    main()