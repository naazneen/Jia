import pyttsx
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import speech_recognition as sr
import sqlite3
import re
from Tkinter import *
import datetime
import Tkinter as tk
from PIL import Image, ImageTk
from itertools import count
import os,fnmatch
import re
import threading

engine = pyttsx.init()
engine.setProperty('rate', 110)
con = sqlite3.connect('dbva.db')
con.text_factory = str
c = con.cursor()


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome('C:\Users\ABDUL\Downloads\chromedriver_win32\chromedriver',chrome_options = chrome_options)

"""
browser = webdriver.Chrome('C:\Users\ABDUL\Downloads\chromedriver_win32\chromedriver')
browser.minimize_window()
   """ 
 


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
    #engine.runAndWait()
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
    print "in search"
    driver.get('http://google.co.in/')
    print "got google"
    sbar = driver.find_element_by_css_selector('input.gLFyf.gsfi')
    print "found input"
    sbar.send_keys(x)
    print "sent keys"
    sbar.send_keys(Keys.ENTER)
    print "sent enter"
    try:
        elem = driver.find_element_by_css_selector('span.ILfuVd')
    except:
        pass
    try:
        elem = driver.find_element_by_css_selector('div.vk_bk.dDoNo')
    except:
        pass
    try:
        elem=driver.find_element_by_css_selector('div.MUxGbd.t51gnb.lyLwlc.lEBKkf')
    except:
        pass
    try:
        elem = driver.find_element_by_css_selector('span.ILfuVd.yZ8quc')
    except:
        pass
    try:
        elem = driver.find_element_by_css_selector('div.Z0LcW')
    except:
        pass
    try:
        elem = driver.find_element_by_css_selector('div.title')
    except:
        pass
    try:
        elem = driver.find_element_by_css_selector('div.BbbuR.uc9Qxb.uE1RRc')
    except:
        pass
    try:
        elem = driver.find_element_by_css_selector('span.vk_gy.vk_sh')
    except:
        pass
    try:
        elem = driver.find_element_by_css_selector('h.bNg8Rb')
    except:
        pass    
    e = elem.text
    print e
    return e
    #print (elem)
    
    

def my(a):
    r=c.execute("select value from MyData where key=a")
    engine.say(r)

#gifanimator
class ImageLabel(tk.Label):
    """a label that displays images, and plays them if they are gifs"""
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)

def playonline(s):
    browser = webdriver.Chrome('C:\Users\ABDUL\Downloads\chromedriver_win32\chromedriver')
    print "in search"
    browser.get('https://www.youtube.com/results?search_query='+s)  
    try:
        vid = browser.find_element_by_css_selector('a.yt-simple-endpoint.style-scope.ytd-video-renderer')
        print "found"
    except:
        pass
    vid.click()
    print "clicked"


#find
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result

def findpattern(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

def play(song):
    mp3=".mp3"
    mp4=".mp4"
    y = re.search('play',song).span()
    #print y
    z=y[1]
    #print z
    #print "success"
    s=song[z+1:]
    print s
    p=findpattern(s+mp4,'E:')
    try:
        os.startfile(p[0])
        return
    except:
        pass
    try:
        p=findpattern(s+mp3,'E:')
        os.startfile(p[0])
        return
    except:
        pass
    try:
        print "else"
        playonline(s)
        #threading.Thread(target=playonline, args=(s,)).start()
    except:
        pass

#play("jia play jogi")

def makenote(x):
    t = re.search('that',x).span()
    z = t[1]
