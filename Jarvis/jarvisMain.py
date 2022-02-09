import re
import pyttsx3
from Classes import friday

def main():
    print("Welcome to Jarvis Program")
    #Initialise the Jarvis program
    engine = pyttsx3.init()
    engine.setProperty('rate', 145)
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

    fridayInstance = friday()
    words = fridayInstance.listen()
    matches = re.search("Friday", words)
    if matches:
        engine.say("Yes Sir!, I am listening")
        engine.runAndWait()
    else:
        engine.say("It is good to see you work Sir")
        engine.runAndWait()

    

if __name__ == "__main__":
    main()