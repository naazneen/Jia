#imported stuff
import datetime
import pyttsx
import speech_recognition as sr
import sqlite3
import functs as f

r = sr.Recognizer()
 
#few declarations
myname="JIyA"
x="hi"
time=datetime.datetime.now()
greet="Peace to you. Today it is " + time.strftime("%d %b")
engine = pyttsx.init()
engine.setProperty('rate', 110)

#introduction fn
def run():
    engine.say("Hi. My name is "+ myname)
    engine.say(greet)
    engine.runAndWait()

#listening fn (sun is hindi of - listen)
def sun():
    with sr.Microphone() as source:
            print ('Say Something!')
            audio = r.listen(source)
            print ('Heard!')
            a = r.recognize_google(audio)
            return a

run()
while(x!="bye"):
    x=sun()
    print(x)
    if (x=="name some fruits"):
        f.fruits()
    elif (x=="read alphabets"):
        f.Alpha()
    elif (x=="what colours you know"):
        f.clr()
    elif (x=="days of the week"):
        f.wdays()
    elif (x!='bye'):
        f.search(x)
        engine.runAndWait()
    else:
        engine.say("Bye.")


engine.runAndWait()
