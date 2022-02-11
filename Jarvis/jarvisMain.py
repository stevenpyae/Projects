import re
import pyttsx3
from Classes import friday

def main():
    print("Welcome to Jarvis Program")
    #Initialise the Jarvis program
    engine = pyttsx3.init()
    engine.setProperty('rate', 145)
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
    
    #Create Instance of Friday
    fridayInstance = friday.Friday()
    words = fridayInstance.listen()
    matches = re.search("Friday", words)

    if matches:
        #If Friday is called
        engine.say("Yes Sir!, I am listening")
        engine.runAndWait()
        newwords = fridayInstance.listen()
    else:
        engine.say("It is good to see you work Sir")
        engine.runAndWait()

    chromeInstance = re.search("Chrome", newwords)

    if chromeInstance:
        engine.say("Launching Chrome for you sir")
        engine.runAndWait()
    else:
        engine.say("I shall wait for your next instructions")
        engine.runAndWait()
    
if __name__ == "__main__":
    main()