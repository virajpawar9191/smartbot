# @viraj_pawar Voice Assistant with python



import webbrowser
import pyttsx3
import pywhatkit
from userinput import takecommand
import requests
from ss import takeSS
import pyjokes
import playsound
from temp import temp
import os
from note import note
import json
import wolframalpha
import datetime
from speak import Speak 
from datetime import date
from datetime import datetime
from todayDate import timedate
Assistant = pyttsx3.init('sapi5')

voices = Assistant.getProperty('voices')
rate = Assistant.getProperty('rate')
Assistant.setProperty('rate', 170)


# def call(text):
#     action_call = ""
#     text = text.lower()
#     if action_call in text:
#         return True

#     return False

def taskExecution():
    while True:
        query = takecommand()

        # Greetings
        if "hello" in query:
            Speak("Hello Sir, How can I help You !")

        # elif "how are you" in query:
            # Speak("I am fine.")
            # Speak("What's about you?")

        # elif "fine" or "good" in query:
            Speak("It's good to know that you are fine !")    

        elif "who are you" in query:
            Speak("i am an assistant your assistant i am here to make your life easier you can command me to perform various tasks such as solving mathematical questions and opening applications etc")

        elif "your name" in query:
            Speak("My name is assistant")

        elif "who am I" in query:
            Speak("You are probably be a human")

        #  temperature
        elif "temperature" in query:
            temp()
        elif "date" in query or "today's date" in query  or "what is time" in query or "time" in query:
            
            timedate()
            break
        elif "what is time" or "time" in query:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("Current Time =", current_time)
            Speak(f"Current Time is{current_time}.")
        # Taking Screenshots
        elif "screenshot" in query:
            takeSS()
           
        elif "open" in query.lower():
            if "chrome" in query.lower():
                Speak("Opening Google Chrome")
                os.startfile(
                    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
                )
            elif "vs code" in query.lower():
                Speak("Opening V S Code")
                os.startfile(
                    r"C:\Users\Admin\AppData\Local\Programs\Microsoft VS Code\Code.exe"
                )

            elif "vs code" in query.lower():
                Speak("Opening V S Code")
                os.startfile(
                    r"C:\Users\Admin\AppData\Local\Programs\Microsoft VS Code\Code.exe"
                )

            elif "youtube" in query.lower():
                Speak("Opening Youtube")
                webbrowser.open("https://youtube.com/")

            elif "google" in query.lower():
                Speak("Opening Google")
                webbrowser.open("https://google.com/")

            elif "facebook" in query.lower():
                Speak("Opening Facebook")
                webbrowser.open("https://facebook.com/")

            elif "instagram" in query.lower():
                Speak("Opening Instagram")
                webbrowser.open("https://instagram.com/")
            else:
                Speak("Application not available.")

        elif "youtube" in query:
            query = query.replace("Assistant","")
            query = query.replace("youtube search","")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            Speak(f"Opening {query} on youtube")

        elif "search" in query:
            query = query.replace("Assistant","")
            query = query.replace("google search","")
            pywhatkit.search(query)
            Speak(f"Opening {query} on Google")

        elif "google" in query:
            query = query.replace("Assistant","")
            query = query.replace("search","")
            pywhatkit.search(query)
            Speak(f"Opening {query} on Google")


        elif "note" in query or "remember this" in query:
            Speak("What would you like me to write down ?")
            note_text = takecommand()
            note(note_text)
            Speak("I have a made note of that")

        elif "where is" in query:
            query = query.replace("Assistant","")
            query = query.replace("where is","")
            web = 'https://www.google.com/maps/place/' + query
            webbrowser.open(web)
            Speak(f"Here is {query} situated")

        elif "news" in query:
            apikey = "9c969167df9b47c2965cc884d38f8d77"

            url = ('https://newsapi.org/v2/top-headlines?'
            'country=in&'
            'apiKey=9c969167df9b47c2965cc884d38f8d77')
            try:
                result = requests.get(url)
            except:
                Speak("Check your connection")

            news = json.loads(result.text)

            for new in news["articles"]:
                print(str(new["title"]),"\n")
                Speak(str(new["title"]))
                Assistant.runAndWait()

                print(str(new["description"]),"\n")
                Speak(str(new["description"]))
                Assistant.runAndWait()

        # wolfram alfa api
        elif "calculate" in query:
            app_id ="Y57WQJ-L2RWWPLYQU"
            client = wolframalpha.Client(app_id)
            query = query.replace("calculate the","")
            query = query.replace("is","")
            query = query.replace("Assistant","")
            res = client.query(query)
            answer = next(res.results).text
            # print(answer)
            Speak(f"the answer is {answer}")

        elif "who is" in query or "what is" in query:
            app_id ="Y57WQJ-L2RWWPLYQU"
            client = wolframalpha.Client(app_id)
            # ind = query.lower().split.index("is")
            # query = query.split()[ind + 1:]
            # res = client.query(" ".join(query))

            res = client.query(query)
            answer = next(res.results).text
            print(answer)
            Speak(f"the answer is {next(res.results).text}")





        # Jokes
        elif "joke" in query:
            get = pyjokes.get_joke()
            Speak(get)

        elif 'alarm' in query:
            Speak("Enter the time !")
            time = input(" : Enter the time : ")

            while True:
                time_al = datetime.datetime.now()
                now = time_al.strftime("%H:%M:%S")

                if now == time:
                    Speak("Time to wake up sir !")
                    playsound('Alarm.mp3')
                    Speak("Alarm Closed !")

                elif now > time:
                    break
            
        elif "don't listen" in query or "stop listening" in query or "do not listen" in query:
            Speak("For how many seconds do you want me to sleep")
            a = int(takecommand())
            time.sleep(a)
            Speak(f"{a} seconds are completed, Now ypu can ask me anything")
        # Close the bot
        elif "bye" or "close" or "break" or "exit" or "quite" in query:
            Speak("Okay Boss, Bye!")
            # Speak("Just say Wake up Assistant!")
            exit()


# To execute the bot
taskExecution()
