import speech_recognition as sr

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        command.energy_threshold = 1000
        command.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            # print("Recognizing...")
            query = command.recognize_google(audio, language='en-in')
            print(f"You Said : {query}")

        except:
            return "none"

        return query.lower()

# takecommand()
