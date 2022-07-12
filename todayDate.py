from datetime import date
from datetime import datetime
from speak import Speak
def timedate():
    today = date.today()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    Speak(f" The today's date is {today} and ")
    Speak(f"Current Time is{current_time}.")
# 

