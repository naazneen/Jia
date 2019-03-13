import Tkinter as tk
import pyttsx
engine = pyttsx.init()
engine.setProperty('rate', 120)


root = tk.Tk()
frame3=tk.Frame(root,background="#B0DEFF")
frame3.grid(row=0,column=0,columnspan=3)


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
        
def rate_changed(r):
    #global var
    p = int(r)
    print p+50
    engine.setProperty('rate', p)
    engine.say("This is new speed")
    engine.runAndWait()

i=0   
b1= tk.Button(frame3,text="Change Voice",command=voice_change)
b1.grid(row=0,column=0)

var=tk.IntVar()
x = tk.Scale(frame3,from_=50,to=250,orient=tk.HORIZONTAL,variable=var,resolution=10,length=350,command=rate_changed)
x.grid(row=1,column=0)

root.mainloop()
