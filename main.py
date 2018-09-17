#imported stuff
import pyttsx
import speech_recognition as sr
import functs as f
import Tkinter as tk
import thread
from PIL import ImageTk, Image
r = sr.Recognizer()

 
#initialisation
engine = pyttsx.init()
engine.setProperty('rate', 110)
x='h'





def sun():
    try:
        with sr.Microphone() as source:
            l1.configure(text="I'm Listening")
            audio = r.listen(source)
            a = r.recognize_google(audio)
            return a
    except:
        l1.configure(text="Sorry. I didn't heard that.")
        engine.say("Sorry. I didn't heard that.")
        engine.runAndWait()
        t2()

def bol():
    x='hi'
    while(True):
        x=sun()
        l2.config(text=x)
        if (x=="who are you"):
            f.intro()   
        elif(x=="who is your best friend"):
            engine.say("you are my best friend, ma'am")
            engine.runAndWait()
        elif (x=="name some fruits"):
            y=f.fruits()
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
            engine.runAndWait()
            return
        else:
            a=f.search(x)
            l1.config(text=a)
            engine.say(a)
            engine.runAndWait()
def t2():
    try:
        thread.start_new_thread(bol,())
    except:
        print("error occured")

#engine.runAndWait()
root = tk.Tk()
img = ImageTk.PhotoImage(Image.open("jiaaa.jpg"))
panel = tk.Label(root, image = img)
panel.pack()
b1=tk.Button(root,text="Ask Jia",command=t2, background="#ffb3d9", foreground="#99004d",font=('Century Gothic',10))
b1.pack()
l1=tk.Label(root,text="Hey")
l1.pack()
l2=tk.Label(root,text="")
l2.pack()
root.mainloop()

