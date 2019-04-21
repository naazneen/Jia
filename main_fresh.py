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
import os
import re
import datetime

 
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
notheardwords=["Sorry, I didn't hear you","I beg your pardon","Sorry, Can you please repeat that."]
nomicwords=["Microphone is not detected."]
yes=['yes','yeah','yess','yah','haa','sure']
no=['no','nah','not','never','nahi']
passwordd=""
useraffix="Ma'am"
user=["Ma'am","Madam","Boss"]

#database
conn = sqlite3.connect('dbva.db')
conn.text_factory = str

create_notes = """
create table if not exists notes(nid integer primary key autoincrement,
text varchar(150),date_created text,locked int);
"""
create_reminders = """
create table if not exists reminders(rid integer primary key autoincrement,
text varchar(150),issue_datetime text,reminder_datetime text, locked int);
"""

create_reports = """
create table if not exists reports(repid integer primary key autoincrement,
title varchar(150),length integer,issue_datetime text,
due_datetime text, status text,viewed int,locked int);
"""

create_user = """
create table if not exists user(key text,value text, locked int);
"""

#fun to create a table from the create_table_sql statement
def create_table(conn, create_table_sql):
    c = conn.cursor()
    c.execute(create_table_sql)
    print "table created"
    

create_table(conn,create_notes)
create_table(conn,create_reminders)
create_table(conn,create_reports)
create_table(conn,create_user)

#Functions

def saybye():
    res=random.choice(farewellwords)+" "
    res=res+random.choice(user)
    return res

def greet():
    res=random.choice(greetwords)+" "
    res=res+random.choice(user)
    return res

def thanks():
    res=random.choice(thank_responses)+" "
    res=res+random.choice(user)
    return res

def internetError():
    res=random.choice(nonetwork)+" "
    res=res+random.choice(user)
    return res

def notheard():
    res=random.choice(notheardwords)+" "
    res=res+random.choice(user)
    return res

def nomic():
    res=random.choice(nomicwords)+" "
    res=res+random.choice(user)+" "
    res=res+" Attach Microphone andtry again."
    return res

def what(x):
    what = re.search('that',x)
    if what==None:
        what = re.search('to',x)
    if what == None:
        engine.say("What is it about?")
        response.configure(text="What is it about?")
        engine.runAndWait()
        what = sun()
        return what  
    what = what.span()
    z1 = what[1]
    what = x[z1+1:]
    return what

def when(x):
    on = re.search(' on',x)
    if on != None:
        on = on.span()
        z1 = on[1]
        at = re.search(' at',x)
        after = re.search(' after',x)
        if at == None:   
            on = x[z1+1:]
        elif at:
            at = at.span()
            z2 = at[1]
            on = x[z1+1:z2-3]
            print on
        if after == None:   
            on = x[z1+1:]
        elif after:
            after = after.span()
            z2 = after[1]
            on = x[z1+1:z2-6]
            print on
        if (on.isdigit()==True):
            y = datetime.datetime.now().year
            m = datetime.datetime.now().month
            on = datetime.datetime.strptime(str(y)+"-"+str(m)+"-"+on,"%Y-%m-%d")
            print on
        else:
            print "error"
    if on == None:
        on = datetime.date.today()
    if re.search('tomorrow',x):
        on = datetime.date.today() + datetime.timedelta(days=1)
    
    at = re.search(' at',x)
    if at!=None:
        at = at.span()
        z2 = at[1]
        at = x[z2+1:]
     
        at2 = re.sub(' a.m.','AM',at)
    
        at2 = re.sub(' p.m.','PM',at)

        print at2
        
        at = datetime.datetime.strptime(at2,"%I:%M%p")
        at.strftime("%H:%M:%S")
        #print at
        
    elif (re.search('after',x)):
        at = re.search('after',x)
        at = at.span()
        z2 = at[1]
        at = x[z2+1:]
        h = re.search('hours',at)
        if h!=None:
            h = h.span()
            z3 = h[1]
            print z3
            h = at[:z3-5]
            h = int(h)
            at2 = datetime.datetime.now() + datetime.timedelta(hours=h)
            format(at2,"%H:%M:%S")
            """at2=str(at2)
            at2 = at2[:19]
            print at2"""
        m = re.search('minutes',at)
        if m!=None:
            m = m.span()
            z3 = m[1]
            print z3
            m = at[:z3-7]
            if (re.search('hours',at)):
                hi = re.search('hours',at)
                hi = hi.span()
                z4 = hi[1]
                m = at[z4+1:z3-7]
                m = int(m)
                at3 = at2 + datetime.timedelta(minutes=m)
                format(at3,"%H:%M:%S")
                at3=str(at3)
                at3 = at3[:19]
                at = at3
            else:
                m = int(m)
                at3 = datetime.datetime.now() + datetime.timedelta(minutes=m)
                format(at3,"%H:%M:%S")
                at3=str(at3)
                at3 = at3[:19]
                print at
                at=at3
    else:
        engine.say("When should I remind?")
        response.configure(text="When should I remind?")
        engine.runAndWait()
        whenq = sun()
        return when(whenq) 

    at=str(at)
    at = at[10:]
    on = str(on)
    on = on[:10]   
    on = on + at
    on = datetime.datetime.strptime(on,"%Y-%m-%d %H:%M:%S")
    return on.strftime("%Y-%m-%d %H:%M:%S")

def makenote(x):
    conn = sqlite3.connect('dbva.db')
    conn.text_factory = str
    item=[]
    item.insert(0,what(x))
    datecreated=datetime.datetime.now()
    item.insert(1,datecreated.strftime("%Y-%m-%d %H:%M:%S"))
    engine.say("Would you like to keep it private?")
    response.configure(text="Would you like to keep it private?")
    engine.runAndWait()
    islocked = sun()
    if islocked in yes:
        islocked = 1
    elif islocked in no:
        islocked = 0
    item.insert(2,islocked)
    c = conn.cursor()
    c.execute("insert into notes(text,date_created,locked) values(?,?,?)",item)
    conn.commit()
    conn.close()
    engine.say("Note is created")
    response.configure(text="Note is created")
    engine.runAndWait()

def makereminder(x):
    conn = sqlite3.connect('dbva.db')
    conn.text_factory = str
    item=[]
    item.insert(0,what(x))
    datecreated=datetime.datetime.now()
    item.insert(1,datecreated.strftime("%Y-%m-%d %H:%M:%S"))
    item.insert(2,when(x))
    engine.say("Would you like to keep it private?")
    response.configure(text="Would you like to keep it private?")
    engine.runAndWait()
    islocked = sun()
    if islocked in yes:
        islocked = 1
    elif islocked in no:
        islocked = 0
    item.insert(2,islocked)
    c = conn.cursor()
    c.execute("insert into reminders(text,issue_datetime,reminder_datetime,locked) values(?,?,?,?)",item)
    conn.commit()
    conn.close()
    engine.say("Reminder is created")
    response.configure(text="Reminder is created")
    engine.runAndWait()
    

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
        if (x==False):
            break
        elif x in wakewords:
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
                    ex = logic(x)
                    if ex == True:
                        break
                    #thread.start_new_thread(logic,(x,))
                    #this was sooooooooo unnecessary!!!
        """elif (re.search('jiya',x)):
            y = re.search('jiya',x).span()
            z = y[1]
            x = x[z+1:]
            logic(x)"""
            

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
    except IOError:
        x=nomic()
        response.configure(text=x)
        engine.say(x)
        lbl.unload()
        lbl.load('speak.gif')
        engine.runAndWait()
        lbl.unload()
        lbl.load('still1.jpg')
        print "inside except"
        return False
    except:
        pass
        """
        ierror=internetError()
        response.configure(text=ierror)
        engine.say(ierror)
        lbl.unload()
        lbl.load('speak.gif')
        engine.runAndWait()
        lbl.unload()"""
    

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
            x=nomic()
            response.configure(text=x)
            engine.say(x)
            lbl.unload()
            lbl.load('speak.gif')
            engine.runAndWait()
            lbl.unload()
            lbl.load('still1.jpg')
            print "inside except in sun"
            return False
        except:
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
    x=str(x)
    x=x.lower()
    print x
    #lbl.unload()
    #x='hi'
    """while(True):
        x=sun()"""
    request.config(text=x)
    if (re.search('play',x)):
        threading.Thread(target=f.play,args=(x,)).start()
        return True
    elif (re.search('find',x)):
        y=f.find(x)
        engine.say(y)
        response.config(text=y)
    elif (re.search('open',x)):
        y=f.find(x)
        os.startfile(y[0])
        engine.say("Here it is.")
        #engine.runAndWait()
    elif (re.search('note',x)):
        threading.Thread(target=makenote,args=(x,)).start()
        return True
    elif (re.search('remind',x) or re.search('reminder',x)):
        threading.Thread(target=makereminder,args=(x,)).start()
        return True
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
    frame5.grid_remove()
    frame3.grid(row=0,column=0,columnspan=3)

def showhome():
    frame3.grid_remove()
    frame4.grid_remove()
    frame5.grid_remove()
    frame1.grid(row=0,column=0,columnspan=3)

def showreports():
    frame1.grid_remove() 
    frame3.grid_remove()
    frame5.grid_remove()
    frame4.grid(row=0,column=0,columnspan=3)
    
    frame41=tk.Frame(frame4,width=frame1["width"],height=267)
    frame41.grid(row=0,column=0)
    frame41.grid_propagate(0)

    frame42=tk.Frame(frame4,width=frame1["width"])
    frame42.grid(row=1,column=0,sticky="SW")

    f4title=tk.Label(frame41,text="Reports",font=('Comic Sans',16))
    f4title.grid(row=0,column=0,columnspan=2)

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
            dlabel=tk.Label(frame42,text=t,justify="left")
            dlabel.grid(row=0,column=0)
        

    for row in cursor:
        c = row[1]
        b = tk.Label(frame41,relief="ridge", text=c,width=30,bg="white",padx=5,anchor="w")
        b.grid(row=i, column=j,sticky="W",padx=5,pady=3)
        report=tk.Button(frame41, text="report",bg="white", command = partial(v_report,row[0]))
        report.grid(row=i,column=j+1,padx=5,pady=3)
        detail=tk.Button(frame41, text="details",bg="white", command = partial(v_details,row[0]))
        detail.grid(row=i,column=j+2,padx=5,pady=3)
        i=i+1


def shownotes():
    frame1.grid_remove() 
    frame3.grid_remove()
    frame4.grid_remove()
    frame5.grid(row=0,column=0,columnspan=3)
    f5title=tk.Label(frame5,text="Notes",font=('Comic Sans',16),anchor="center")
    f5title.grid(row=0,column=0,columnspan=3)
    ncursor = conn.execute("SELECT * from notes")

    def v_note(x):
        response.configure(text="speak password")
        engine.say("speak password")
        engine.runAndWait()
        global passwordd
        p = sun()
        if p == passwordd:
            vnote= conn.execute("select text from notes where nid="+str(x))
            for row in vnote:
                t = row[0]
                response.configure(text=t)
                engine.say("Here is the note")
                engine.runAndWait()
        else:
            response.configure(text="incorrect password")
            engine.say("incorrect password")
            engine.runAndWait()
    ni=1
    nj=-1
    for row in ncursor:
        nj+=1
        if row[3]==1:
            nc="Protected. Click to View"
            nb = tk.Button(frame5,relief="ridge",wraplength=67,command = partial(v_note,row[0]),justify="left",text=nc,width=10,height=5,anchor="nw",bg="white") 
        elif row[3]==0:    
            nc = row[1]
            nb = tk.Label(frame5,relief="ridge",wraplength=67,justify="left",text=nc,width=10,height=5,anchor="nw",bg="white")
        if nj==3:
            ni+=1
            nj=0
        nb.grid(row=ni, column=nj,sticky="W",padx=5,pady=3)
    
root = tk.Tk()
root.configure(background="#f2f2f2")
root.title("JIA")
#root.iconbitmap("jiaaa.jpg")
ttk.Style().configure("TButton", relief="flat",background="#ccc",height=50,width=50)


#main_window
frame1=tk.Frame(root,width=340,height=340,background="#f2f2f2")
frame1.grid(row=0,column=0,columnspan=3)
frame2=tk.Frame(root,width=80,height=200,background="#f2f2f2")
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
b3 = ttk.Button(frame2,image=img3, command=shownotes, style="TButton")
b3.grid(row=2,column=0,padx=10,pady=13)
img4 = ImageTk.PhotoImage(Image.open("reports.png"))  
b4 = ttk.Button(frame2,image=img4, command=showreports,style="TButton")
b4.grid(row=3,column=0,padx=10,pady=13)

#home

lbl = f.ImageLabel(frame1)
lbl.grid(row=0,column=0,columnspan=3)
lbl.load('still1.jpg')

#request-response
response=tk.Label(root,text="Hey",relief="solid",justify=tk.LEFT,wraplength=200,width=48,height=4,fg="Black",bg="white",anchor=tk.W)
#response=ttk.Label(root,text="Hey",justify=tk.LEFT,wraplength=200,anchor=tk.W,style="TButton")
response.grid(row=1,column=0,columnspan=3)
request=tk.Label(root,text="",relief="solid",justify=tk.RIGHT,wraplength=200,width=45,height=4,fg="White",bg="white",anchor=tk.E)
request.grid(row=2,column=1,columnspan=3)

#settings
frame3=tk.Frame(root,background="#f2f2f2",bd=4)
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
    if pass1==False:
        return 0  
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
    if text=="Set Password":
        valid=setpass()
        if valid==1:
            t.set("Change Password")
        elif valid==0:
            t.set("Set Password")
    else:
        valid=changepass()
        if valid==1 or valid==0:
            t.set("Change Password")

def rem_password():
    t.set("Set Password")
    engine.say("Password removed successfully.")
    engine.runAndWait() 
    sb5.grid_remove()

def t_password():
    thread.start_new_thread(password,())

   
sb1= tk.Button(frame3,relief="raised",text="Change Voice",command=voice_change,bg="White",fg="Black")
sb1.grid(row=0,column=0,padx=10,pady=10)

rvar=tk.IntVar()
rx = tk.Scale(frame3,relief="solid",label="Speech Rate",bd=1,bg="White",fg="Black",troughcolor="White",from_=0,to=200,orient=tk.HORIZONTAL,variable=rvar,resolution=10,length=250)
rx.grid(row=1,column=0,padx=10,pady=10)
sb2= tk.Button(frame3,relief="raised",text="Test",command=rate_changed,bg="White",fg="Black")
sb2.grid(row=1,column=1,padx=10,pady=10)

vvar=tk.DoubleVar()
vx = tk.Scale(frame3,relief="solid",label="Speech volume",bd=1,bg="White",fg="Black",troughcolor="White",from_=1,to=10,orient=tk.HORIZONTAL,variable=vvar,resolution=1,length=250)
vx.grid(row=2,column=0,padx=10,pady=10)
sb3= tk.Button(frame3,relief="raised",text="Test",command=vol_changed,bg="White",fg="Black")
sb3.grid(row=2,column=1,padx=10,pady=10)

t=tk.StringVar()
t.set("Set Password")
sb4= tk.Button(frame3,relief="raised",textvariable=t,command=t_password,bg="White",fg="Black")
sb4.grid(row=3,column=0,padx=10,pady=10)

sb5= tk.Button(frame3,relief="raised",text="Remove Password",command=rem_password,bg="White",fg="Black")




#reports
frame4=tk.Frame(root,background="#f2f2f2",bd=4)
frame4.configure(height=frame1["height"],width=frame1["width"])
frame4.grid_propagate(0)

#notes
frame5=tk.Frame(root,background="#f2f2f2",bd=4)
frame5.configure(height=frame1["height"],width=frame1["width"])
frame5.grid_propagate(0)


    
    
"""nd=row[2]
ne = tk.Label(frame5,relief="ridge", text=nd,width=30,bg="white",padx=5,anchor="w")
ne.grid(row=i+1, column=j,sticky="W",padx=5,pady=3)"""
    


APP = App(root)
root.mainloop()
