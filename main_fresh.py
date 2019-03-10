#imported stuff
import pyttsx
import speech_recognition as sr
import functs as f
import Tkinter as tk
import thread
import threading
from PIL import ImageTk, Image
r = sr.Recognizer()

 
#initialisation
engine = pyttsx.init()
engine.setProperty('rate', 120)
wakewords = ['jia jee','good morning','jiya','jai','hello','listen','hey jiya','computer maha shay']
byewords = ['bye','good bye','good night','catch you later','see ya'] 
greetwords = ['nice to see you back','good morning','welcome back','hi, I hope you are doing good','hi, how can I help you?']
farewellwords = ['bye','see you soon','happy to helped you','good bye','good night','have a great day']

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
            while (True):
                print "inside while true"
                x=sun()
                if (x!="bye"):
                    logic(x)
                    #thread.start_new_thread(logic,(x,)) this was so unnecessary
                else:
                    engine.say("Good bye")
                    engine.runAndWait()
                    print "goodbye"
                    break

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
    frame3.grid(row=0,column=0,columnspan=3)

def showhome():
    frame3.grid_remove()
    frame1.grid(row=0,column=0,columnspan=3)

root = tk.Tk()


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
b4 = tk.Button(frame2,image=img4, command=callback, height=50, width=50)
b4.grid(row=3,column=0,padx=10,pady=15)



lbl = f.ImageLabel(frame1)
lbl.grid(row=0,column=0,columnspan=3)
lbl.load('still1.jpg')

response=tk.Label(root,text="Hey",justify=tk.LEFT,wraplength=200,width=40,height=3,bg="#B0DEFF",anchor=tk.NW)
response.grid(row=1,column=0,columnspan=3)
request=tk.Label(root,text="",justify=tk.RIGHT,wraplength=200,width=40,height=3,bg="#B0DEFF",anchor=tk.NE)
request.grid(row=2,column=2,columnspan=3)

frame3=tk.Frame(root,background="#B0DEFF")
frame3.configure(height=frame1["height"],width=frame1["width"])
frame3.grid_propagate(0)
passb=tk.Button(frame3,text="in settings")
passb.grid(row=0,column=0)



APP = App(root)
root.mainloop()
    
