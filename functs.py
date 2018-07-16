import pyttsx
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import speech_recognition as sr
import sqlite3
import re

engine = pyttsx.init()
engine.setProperty('rate', 110)
con = sqlite3.connect('dbva.db')
con.text_factory = str
c = con.cursor()

#functions
def fruits():
    voices = ('banana','apple','mango','Cherry ','Date' ,'Guava')
    engine.say("Fruits I know are")
    for f in voices:
        engine.say(f)
    engine.runAndWait()
def Alpha():
    for row in c.execute("select letters from alpha"):
        engine.say(row)
    #engine.say("A B C D E F G H I J K L M")
    #engine.say("N O P Q R S T U V W X Y Z")
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
    
    chkwhen = re.match(r'when',x)
    if chkwhen:
        elem = browser.find_element_by_css_selector('div.MUxGbd.t51gnb.lyLwlc.lEBKkf')
    chkwhat = re.match(r'what',x)
    if chkwhat:
        elem = browser.find_element_by_css_selector('span.ILfuVd.yZ8quc')
    chkwho = re.match(r'who',x)
    if chkwho:
        elem = browser.find_element_by_css_selector('div.Z0LcW')
        
    engine.say(elem.text)
    engine.runAndWait()

