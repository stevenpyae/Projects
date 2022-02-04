import re
import pyttsx3
import speech_recognition

def main():
    print("Welcome to Jarvis Program")
    #Initialise the Jarvis program
    engine = pyttsx3.init()
    engine.setProperty('rate', 145)
    engine.say("Welcome to Jarvis Program")

    #Initialise Listening
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Jarvis is Listening: ")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    #Recognize speech using Google Speech Recognition
    print(recognizer.recognize_google(audio))
    

if __name__ == "__main__":
    main()