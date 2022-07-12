from sympy import im
from speak import Speak
from userinput import takecommand
import pyautogui

# 3. Taking Screenshot


def takeSS():
    Speak("Ok Boss , what should I name that file")
    path = takecommand()
    pathname = path + ".png"
    path1 = "D:\\Final Project\\Screenshot\\" + pathname
    kk = pyautogui.screenshot()
    kk.save(path1)
    Speak("Screenshot has been captured.!")