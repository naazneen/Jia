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
import msvcrt
import ttk

 
#initialisation
r = sr.Recognizer()
engine = pyttsx.init()
engine.setProperty('rate', 120)
wakewords = ['jia jee','good morning','jiya','jai','hello','listen','hey jiya','computer maha shay']
byewords = ['bye','goodbye','good night','catch you later','see ya','siya'] 
greetwords = ['nice to see you back','good morning','welcome back','hi, I hope you are doing good','hi, how can I help you']
farewellwords = ['bye','see you soon','happy to helped you','good bye','good night','have a great day']
thankwords=["thank you","thanks jia", "thanks","thanks jiya","thank you jiya"]
thank_responses=["You're welcome","always welcome ","my pleasure ","most welcome,"]
nonetwork=["Make sure you have internet connection ","Seems like internet is not available ","Check Internet connection I won't be able to help you "]
notheardwords=["Sorry, I didn't hear you","I beg your pardon","Sorry, Will you please repeat that."]
passwordd=""
useraffix="Ma'am"
user=["Ma'am","Madam","Boss"]


def saybye():
    res=random.choice(farewellwords)
    res=res+random.choice(user)
    return res

def greet():
    res=random.choice(greetwords)
    res=res+random.choice(user)
    return res

def thanks():
    res=random.choice(thank_responses)
    res=res+random.choice(user)
    return res

def internetError():
    res=random.choice(nonetwork)
    res=res+random.choice(user)
    return res

def notheard():
    res=random.choice(notheardwords)
    res=res+random.choice(user)
    return res


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
            engine.say(greet())
            engine.runAndWait()
            while (True):
                print "inside while true"
                x=sun()
                if x in byewords:
                    engine.say(saybye())
                    engine.runAndWait()
                    print "goodbye"
                    break
                elif x in thankwords:
                    engine.say(thanks())
                    engine.runAndWait()
                    continue
                else:
                    logic(x)
                    #thread.start_new_thread(logic,(x,))
                    #this was sooooooooo unnecessary!!!
               

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
    except KeyboardInterrupt:
        print "hit"
        pass
    except:
        print "except"
        engine.say(internetError())
        lbl.unload()
        lbl.load('speak.gif')
        engine.runAndWait()
        lbl.unload()
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
        except KeyboardInterrupt:
            print "key pressed"
            break
        except IOError:
            x=notheard()
            response.configure(text=x)
            engine.say(x)
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
root.title("JIA")
#root.iconbitmap("jiaaa.jpg")
ttk.Style().configure("TButton", relief="flat",background="#ccc",height=50,width=50)


#main_window
frame1=tk.Frame(root,width=340,height=340,background="White")
frame1.grid(row=0,column=0,columnspan=3)
frame2=tk.Frame(root,width=80,height=200,background="White")
frame2.grid(row=0,column=3)
frame2.configure(height=frame1["height"])
frame2.grid_propagate(0)
frame1.configure(height=frame1["height"],width=frame1["width"])
frame1.grid_propagate(0)

img1 = ImageTk.PhotoImage(Image.open("settings.png"))  
b1 = ttk.Button(frame2,image=img1, command=showsetting, style="TButton")
b1.grid(row=1,column=0,padx=10,pady=13)
img2 = ImageTk.PhotoImage(Image.open("home.png"))  
b2 = ttk.Button(frame2,image=img2, command=showhome, style="TButton")
b2.grid(row=0,column=0,padx=10,pady=13)
img3 = ImageTk.PhotoImage(Image.open("notes.png"))  
b3 = ttk.Button(frame2,image=img3, command=callback, style="TButton")
b3.grid(row=2,column=0,padx=10,pady=13)
img4 = ImageTk.PhotoImage(Image.open("reports.png"))  
b4 = ttk.Button(frame2,image=img4, command=showreports,style="TButton")
b4.grid(row=3,column=0,padx=10,pady=13)

#home

lbl = f.ImageLabel(frame1)
lbl.grid(row=0,column=0,columnspan=3)
lbl.load('still1.jpg')

#request-response
response=tk.Label(root,text="Hey",justify=tk.LEFT,wraplength=200,width=42,height=3,fg="Black",bg="#909497",anchor=tk.W)
#response=ttk.Label(root,text="Hey",justify=tk.LEFT,wraplength=200,anchor=tk.W,style="TButton")
response.grid(row=1,column=0,columnspan=3)
request=tk.Label(root,text="",justify=tk.RIGHT,wraplength=200,width=42,height=3,fg="White",bg="Black",anchor=tk.E)
request.grid(row=2,column=1,columnspan=3)

#settings
frame3=tk.Frame(root,background="#909497",bd=4)
frame3.configure(height=frame1["height"],width=frame1["width"])
frame3.grid_propagate(0)

vi=0 #voice index

def voice_change():
    #print "voice"
    global vi
    print vi
    voices = engine.getProperty('voices')
    try:
        i=i+1
        print i
        engine.setProperty('voice',voices[vi].id)
        engine.say("voice changed.")
        engine.runAndWait()
        #i=i+1
    except:
        if vi > 0:
            print vi
            engine.say("i have these voices only.")
            engine.runAndWait()
        elif vi==0:
            print vi
            engine.say("I have this voice only.")
            engine.runAndWait()
        vi=0
        
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

   
sb1= tk.Button(frame3,text="Change Voice",command=voice_change,bg="Black",fg="White")
sb1.grid(row=0,column=0,padx=10,pady=10)

rvar=tk.IntVar()
rx = tk.Scale(frame3,label="Speech Rate",bd=1,bg="Black",fg="White",troughcolor="White",from_=0,to=200,orient=tk.HORIZONTAL,variable=rvar,resolution=10,length=250)
rx.grid(row=1,column=0,padx=10,pady=10)
sb2= tk.Button(frame3,text="Test",command=rate_changed,bg="Black",fg="White")
sb2.grid(row=1,column=1,padx=10,pady=10)

vvar=tk.DoubleVar()
vx = tk.Scale(frame3,label="Speech volume",bd=1,bg="Black",troughcolor="White",from_=1,to=10,orient=tk.HORIZONTAL,variable=vvar,resolution=1,length=250)
vx.grid(row=2,column=0,padx=10,pady=10)
sb3= tk.Button(frame3,text="Test",command=vol_changed,bg="Black",fg="White")
sb3.grid(row=2,column=1,padx=10,pady=10)

t=tk.StringVar()
t.set("set password")
sb4= tk.Button(frame3,textvariable=t,command=t_password,bg="Black",fg="White")
sb4.grid(row=3,column=0,padx=10,pady=10)

sb5= tk.Button(frame3,text="Remove password",command=rem_password,bg="#A7DAFE",fg="White")

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
    b.grid(row=i, column=j,sticky="W")
    report=tk.Button(frame4, text="report", command = partial(v_report,row[0]))
    report.grid(row=i,column=j+1)
    detail=tk.Button(frame4, text="details", command = partial(v_details,row[0]))
    detail.grid(row=i,column=j+2)
    i=i+1




APP = App(root)
root.mainloop()
    
