import pyttsx
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import speech_recognition as sr
engine = pyttsx.init()
engine.setProperty('rate', 110)

#functions
def fruits():
    voices=('banana','apple','mango','Cherry ','Date' ,'Guava')
    engine.say("Fruits I know are")
    for f in voices:
        engine.say(f)
    engine.runAndWait()
def Alpha():
    engine.say("A B C D E F G H I J K L M")
    engine.say("N O P Q R S T U V W X Y Z")
    engine.runAndWait()
def wdays():
    engine.say("Sunday, Monday, Tuesday,Wednesday, Thursday, Friday, Saturday")
    engine.runAndWait()
def clr():
    engine.say("Violet, Indigo, Blue, Green, Yellow, Orange, Red")
    engine.runAndWait()


def search(x):
    browser = webdriver.Chrome('C:\Users\ABDUL\Downloads\chromedriver_win32\chromedriver')
    browser.get('http://google.co.in/')
    sbar = browser.find_element_by_id('lst-ib')
    sbar.send_keys(x)
    sbar.send_keys(Keys.ENTER)
