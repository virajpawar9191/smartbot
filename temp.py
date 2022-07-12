from speak import Speak
from userinput import takecommand
import requests
from bs4 import BeautifulSoup
# 2. TEMPERATURE


def temp():
    Speak("Tell me the city name !")
    city = takecommand()
    search = "temperature in" + city
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temperature = data.find("div", class_="BNeawe").text
    Speak(f"The temperature in {city} is {temperature} ")