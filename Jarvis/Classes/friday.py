import speech_recognition

class Friday:
    def __init__(self):
        self.name = "friday"
        self.recognizer = speech_recognition.Recognizer()
    
    def listen(self):
        with speech_recognition.Microphone() as source:
            print("Friday is Listening: ")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
        #Recognize speech using Google Speech Recognition
        words = self.recognizer.recognize_google(audio)

        print(words)
        return words
