import pyttsx3

Assistant = pyttsx3.init('sapi5')

voices = Assistant.getProperty('voices')
rate = Assistant.getProperty('rate')
Assistant.setProperty('rate', 170)

#  Speak function which helps bot to communicate with user

def Speak(audio):
    Assistant.say(audio)
    print(f" : {audio} ")
    print("     ")
    Assistant.runAndWait()

# Speak("Hello Viraj")

#  takecommand function for taking users command

