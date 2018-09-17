import pyttsx
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import speech_recognition as sr
import sqlite3
import re
from Tkinter import *
import datetime

engine = pyttsx.init()
engine.setProperty('rate', 110)
con = sqlite3.connect('dbva.db')
con.text_factory = str
c = con.cursor()
 


#functions
def intro():
    myname="JIyA"
    time=datetime.datetime.now()
    greet="Peace unto you."
    engine.say("My name is "+myname+greet)
    engine.say("Today it is " + time.strftime("%d %b"))
    engine.runAndWait()
    
def fruits():
    voices = ('banana','apple','mango','Cherry ','Date' ,'Guava')
    engine.say("Fruits I know are")
    for f in voices:
        engine.say(f)
    engine.runAndWait()
    return voices
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
    browser.minimize_window()
    browser.get('http://google.co.in/')
    sbar = browser.find_element_by_id('lst-ib')
    sbar.send_keys(x)
    sbar.send_keys(Keys.ENTER)
    
    try:
        elem=browser.find_element_by_css_selector('div.MUxGbd.t51gnb.lyLwlc.lEBKkf')
    except:
        pass
    try:
        elem = browser.find_element_by_css_selector('span.ILfuVd.yZ8quc')
    except:
        pass
    try:
        elem = browser.find_element_by_css_selector('div.Z0LcW')
    except:
        pass
    try:
        elem = browser.find_element_by_css_selector('div.title')
    except:
        pass
    try:
        elem = browser.find_element_by_css_selector('div.BbbuR.uc9Qxb.uE1RRc')
    except:
        pass
    try:
        elem = browser.find_element_by_css_selector('span.vk_gy.vk_sh')
    except:
        pass
    
        
    elem = elem.text
    elem = elem[:47]
    return elem
    #print (elem)
    
    

def my(a):
    r=c.execute("select value from MyData where key=a")
    engine.say(r)


