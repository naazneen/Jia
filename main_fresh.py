#imported stuff
import pyttsx
from functools import partial
import sqlite3
import speech_recognition as sr
import functs as f
import Tkinter as tk
import thread
import threading
from PIL import ImageTk, Image
import random


 
#initialisation
r = sr.Recognizer()
engine = pyttsx.init()
engine.setProperty('rate', 120)
wakewords = ['jia jee','good morning','jiya','jai','hello','listen','hey jiya','computer maha shay']
byewords = ['bye','good bye','good night','catch you later','see ya'] 
greetwords = ['nice to see you back','good morning','welcome back','hi, I hope you are doing good','hi, how can I help you?']
farewellwords = ['bye','see you soon','happy to helped you','good bye','good night','have a great day']
passwordd=""

class App(threading.Thread):
    def __init__(self, tk_root):
        self.root = tk_root
        threading.Thread.__init__(self)
        self.start()
    def run(self):
        wake()

def wake():
    while (True):
        print "inside mainloop"
        x=sleepy()
        if x in wakewords:
            print "heard wakewords"
            engine.say(random.choice(greetwords))
            engine.runAndWait()
            while (True):
                print "inside while true"
                x=sun()
                if x in byewords:
                    engine.say(random.choice(farewellwords))
                    engine.runAndWait()
                    print "goodbye"
                    break
                else:
                    logic(x)
                    #thread.start_new_thread(logic,(x,)) this was so unnecessary
               

def sleepy():
    print "inside sleepy"
    lbl.unload()
    lbl.load('still1.jpg')
    try:
        with sr.Microphone() as source:
            print "listening"
            response.configure(text="I'm asleep")
            audio = r.listen(source)
            a = r.recognize_google(audio)
            print "heard"
            return a
    except:
        print "except"
        pass

def sun():
    print ("inside sun")
    lbl.unload()
    lbl.load('listen.gif')
    while True:
        try:
            with sr.Microphone() as source:
                response.configure(text="I'm Listening")
                print "I'm Listening"
                audio = r.listen(source)
                a = r.recognize_google(audio)
                #return a
        except:
            response.configure(text="Sorry. I didn't heard that.")
            engine.say("Sorry. I didn't heard that.")
            lbl.unload()
            lbl.load('speak.gif')
            engine.runAndWait()
            lbl.unload()
            lbl.load('listen.gif')
            print "inside except in sun"
            continue
        else:
            break
    return a

def logic(x):
    print ("inside logic")
    print x
    #lbl.unload()
    #x='hi'
    """while(True):
        x=sun()"""
    request.config(text=x)
    if (x=="who are you"):
        f.intro()   
    elif(x=="who is your best friend"):
        engine.say("you are my best friend, ma'am")
        #engine.runAndWait()
    elif (x=="name some fruits"):
        y=f.fruits()
        engine.say(y)
        response.config(text=y)
    elif (x=="read alphabets"):
        f.Alpha()
    elif (x=="what colours you know"):
        f.clr()
    elif (x=="days of the week"):
        f.wdays()
    elif (x=="hi"):
        f.intro()
    elif (x=="bye"):
        engine.say("Bye.")
        response.config(text="bye")
        lbl.load('still1.jpg')
        engine.runAndWait()
        wake()
    else:
        a=f.search(x)
        response.config(text=a)
        engine.say(a)
        #lbl.load('speak.gif')
        #engine.runAndWait()
    lbl.load('speak.gif')
    engine.runAndWait()

def callback():
    print "click!"

def showsetting():
    frame1.grid_remove()
    frame4.grid_remove()
    frame3.grid(row=0,column=0,columnspan=3)

def showhome():
    frame3.grid_remove()
    frame4.grid_remove()
    frame1.grid(row=0,column=0,columnspan=3)

def showreports():
    frame1.grid_remove() 
    frame3.grid_remove()
    frame4.grid(row=0,column=0,columnspan=3)
    
root = tk.Tk()
root.configure(background="white")
#main_window

frame1=tk.Frame(root,width=340,height=340,background="Blue")
frame1.grid(row=0,column=0,columnspan=3)
frame2=tk.Frame(root,width=80,height=200,background="#B0DEFF")
frame2.grid(row=0,column=3)
frame2.configure(height=frame1["height"])
frame2.grid_propagate(0)
frame1.configure(height=frame1["height"],width=frame1["width"])
frame1.grid_propagate(0)

img1 = ImageTk.PhotoImage(Image.open("settings.jpg"))  
b1 = tk.Button(frame2,image=img1, command=showsetting, height=50, width=50)
b1.grid(row=1,column=0,padx=10,pady=15)
img2 = ImageTk.PhotoImage(Image.open("home.jpg"))  
b2 = tk.Button(frame2,image=img2, command=showhome, height=50, width=50)
b2.grid(row=0,column=0,padx=10,pady=15)
img3 = ImageTk.PhotoImage(Image.open("notes.jpg"))  
b3 = tk.Button(frame2,image=img3, command=callback, height=50, width=50)
b3.grid(row=2,column=0,padx=10,pady=15)
img4 = ImageTk.PhotoImage(Image.open("reports.jpg"))  
b4 = tk.Button(frame2,image=img4, command=showreports, height=50, width=50)
b4.grid(row=3,column=0,padx=10,pady=15)

#home

lbl = f.ImageLabel(frame1)
lbl.grid(row=0,column=0,columnspan=3)
lbl.load('still1.jpg')

#request-response
response=tk.Label(root,text="Hey",justify=tk.LEFT,wraplength=200,width=42,height=3,bg="#B0DEFF",anchor=tk.W)
response.grid(row=1,column=0,columnspan=3)
request=tk.Label(root,text="",justify=tk.RIGHT,wraplength=200,width=42,height=3,bg="#B0DEFF",anchor=tk.E)
request.grid(row=2,column=1,columnspan=3)

#settings
frame3=tk.Frame(root,background="white",bd=4)
frame3.configure(height=frame1["height"],width=frame1["width"])
frame3.grid_propagate(0)

def voice_change():
    #print "voice"
    global i
    voices = engine.getProperty('voices')
    try:
        i=i+1
        #print i
        engine.setProperty('voice',voices[i].id)
        engine.say("voice changed.")
        engine.runAndWait()
    except:
        if i > 1:
            #print i
            engine.say("i have these voices only.")
            engine.runAndWait()
        elif i==1:
            #print i
            engine.say("I have this voice only.")
            engine.runAndWait()
        i=0
        
def rate_changed():
    #global var
    p = int(rvar.get())
    print p+50
    rate = engine.getProperty('rate')
    engine.setProperty('rate', p+50)
    engine.say("This is new speed")
    engine.runAndWait()

def vol_changed():
    #global var
    p = float(vvar.get())
    print p/10
    volume = engine.getProperty('volume')
    engine.setProperty('volume', p)
    engine.say("This is new volume")
    engine.runAndWait()


def setpass():
    global passwordd
    engine.say("what will be new password?")
    engine.runAndWait()
    pass1=sun()
    engine.say("speak password again.")
    engine.runAndWait()
    pass2=sun()
    if pass1==pass2:
        engine.say("password set successfully")
        passwordd=pass1
        print passwordd
        engine.runAndWait()
        sb5.grid(row=4,column=0,padx=10,pady=10)
        return 1
    else:
        engine.say("password does not match.")
        engine.runAndWait()
        return 0
    
def changepass():
    global passwordd
    engine.say("speak old password.")
    print passwordd
    engine.runAndWait()
    pass1=sun()
    if pass1==passwordd:
        v=setpass()
        if v==1:
            return 1
        else:
            return 0
    else:
        engine.say("Sorry. This is incorrect password.")
        engine.runAndWait()
        return 0
        

def password():
    text=sb4['text']
    print text
    #t.set("I am clicked")
    if text=="set password":
        valid=setpass()
        if valid==1:
            t.set("change password")
        elif valid==0:
            t.set("set password")
    else:
        valid=changepass()
        if valid==1 or valid==0:
            t.set("change password")

def rem_password():
    t.set("set password")
    engine.say("Password removed successfully.")
    engine.runAndWait() 
    sb5.grid_remove()

def t_password():
    thread.start_new_thread(password,())

i=0   
sb1= tk.Button(frame3,text="Change Voice",command=voice_change,bg="#A7DAFE")
sb1.grid(row=0,column=0,padx=10,pady=10)

rvar=tk.IntVar()
rx = tk.Scale(frame3,label="Speech Rate",bd=1,bg="#B0DEFF",troughcolor="#A7DAFE",from_=0,to=200,orient=tk.HORIZONTAL,variable=rvar,resolution=10,length=250)
rx.grid(row=1,column=0,padx=10,pady=10)
sb2= tk.Button(frame3,text="Test",command=rate_changed,bg="#A7DAFE")
sb2.grid(row=1,column=1,padx=10,pady=10)

vvar=tk.DoubleVar()
vx = tk.Scale(frame3,label="Speech volume",bd=1,bg="#B0DEFF",troughcolor="#A7DAFE",from_=1,to=10,orient=tk.HORIZONTAL,variable=vvar,resolution=1,length=250)
vx.grid(row=2,column=0,padx=10,pady=10)
sb3= tk.Button(frame3,text="Test",command=vol_changed,bg="#A7DAFE")
sb3.grid(row=2,column=1,padx=10,pady=10)

t=tk.StringVar()
t.set("set password")
sb4= tk.Button(frame3,textvariable=t,command=t_password,bg="#A7DAFE")
sb4.grid(row=3,column=0,padx=10,pady=10)

sb5= tk.Button(frame3,text="Remove password",command=rem_password,bg="#A7DAFE")

#reports
frame4=tk.Frame(root,background="#B0DEFF",bd=4)
frame4.configure(height=frame1["height"],width=frame1["width"])
frame4.grid_propagate(0)

conn = sqlite3.connect('C:\Users\ABDUL\Downloads\sqlite-tools-win32-x86-3240000\sqlite-tools-win32-x86-3240000\dbva.db')
print "Opened database successfully";
cursor = conn.execute("SELECT * from reports")

i=1
j=0

def v_report(x):
    print "report"
    print x
    

def v_details(x):
    print "details"
    x=str(x)
    viewdetails = conn.execute("select * from reports where repid="+x)
    for row in viewdetails:
        r1=str(row[1])
        r2=str(row[3])
        r3=str(row[4])
        r4=str(row[5])
        t="Title : "+r1+"\nIssue Date : "+r2+"\nDue Date : "+r3+"\nStatus : "+r4
        print t
        dlabel=tk.Label(frame4,text=t)
        dlabel.grid(row=3,column=0)
    

for row in cursor:
    c = row[1]
    b = tk.Label(frame4, text=c)
    b.grid(row=i, column=j)
    report=tk.Button(frame4, text="report", command = partial(v_report,row[0]))
    report.grid(row=i,column=j+1)
    detail=tk.Button(frame4, text="details", command = partial(v_details,row[0]))
    detail.grid(row=i,column=j+2)
    i=i+1



APP = App(root)
root.mainloop()
    
