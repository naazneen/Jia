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
engine.setProperty('rate', 110)
x='h'

class App(threading.Thread):

    def __init__(self, tk_root):
        self.root = tk_root
        threading.Thread.__init__(self)
        self.start()

    def run(self):
        wake()




def sun1():
    lbl.unload()
    lbl.load('still1.jpg')
    try:
        with sr.Microphone() as source:
            l1.configure(text="I'm asleep")
            audio = r.listen(source)
            a = r.recognize_google(audio)
            return a
    except:
        pass


def sun():
    print "inside sun"
    lbl.unload()
    lbl.load('listen.gif')
    while True:
        try:
            with sr.Microphone() as source:
                l1.configure(text="I'm Listening")
                audio = r.listen(source)
                a = r.recognize_google(audio)
                #return a
        except:
            l1.configure(text="Sorry. I didn't heard that.")
            engine.say("Sorry. I didn't heard that.")
            lbl.unload()
            lbl.load('speak.gif')
            engine.runAndWait()
            print "inside except in sun"
            continue
        else:
            break
    return a
        #t2()
        #bol()
    #return a

def bol(x):
    print ("inside bol")
    #lbl.unload()
    #x='hi'
    """while(True):
        x=sun()"""
    l2.config(text=x)
    if (x=="who are you"):
        f.intro()   
    elif(x=="who is your best friend"):
        engine.say("you are my best friend, ma'am")
        #engine.runAndWait()
    elif (x=="name some fruits"):
        y=f.fruits()
        engine.say(y)
        l1.config(text=y)
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
        l1.config(text="bye")
        lbl.load('still1.jpg')
        engine.runAndWait()
        wake()
    else:
        a=f.search(x)
        l1.config(text=a)
        engine.say(a)
        #lbl.load('speak.gif')
        #engine.runAndWait()
    lbl.load('speak.gif')
    engine.runAndWait()

def t2():
    print "inside t2"
    while(True):
        x=sun()
        if (x=="bye"):
            engine.say("Good Bye")
            engine.runAndWait()
            break
        else:
            #thread.start_new_thread(bol,(x,))
            try:
                thread.start_new_thread(bol,(x,))
            except:
                print("error occured in threat creation")
        

wakewords = ['jia jee','good morning','jiya','jai','hello','listen','hey jiya','computer maha shay']

def wake():
    while (True):
        x=sun1()
        if x in wakewords:
            engine.say("Nice to see you back.")
            engine.runAndWait()
            while True:
                x=sun()
                if (x=="bye"):
                    engine.say("Good Bye")
                    engine.runAndWait()
                    break
                else:
                    #thread.start_new_thread(bol,(x,))
                    try:
                        thread.start_new_thread(bol,(x,))
                    except:
                        print("error occured in threat creation")
        print "in main loop"
        
        

    
def ok():
    for i in range(0,2):
        engine.say("Hey")
        engine.runAndWait()


#engine.runAndWait()
root = tk.Tk()
#img = ImageTk.PhotoImage(Image.open("listen.jpg"))
#panel = tk.Label(root, image = img)
#panel.pack()
lbl = f.ImageLabel(root)
lbl.pack()
lbl.load('still1.jpg')

b1=tk.Button(root,text="Ask Jia",command=t2, background="#ffb3d9", foreground="#99004d",font=('Century Gothic',10))
b1.pack()
l1=tk.Label(root,text="Hey")
l1.pack()
l2=tk.Label(root,text="")
l2.pack()

APP = App(root)
root.mainloop()

