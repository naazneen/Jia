import re
import datetime
import speech_recognition as sr
import pyttsx
import sqlite3

con = sqlite3.connect('C:\Users\ABDUL\Downloads\sqlite-tools-win32-x86-3240000\sqlite-tools-win32-x86-3240000\dbva.db')
con.text_factory = str
c = con.cursor()

engine = pyttsx.init()
engine.setProperty('rate', 120)
r = sr.Recognizer()
def sun():
    try:
        with sr.Microphone() as source:
            print "listening"
            #response.configure(text="I'm asleep")
            audio = r.listen(source)
            a = r.recognize_google(audio)
            print "heard"
            print a
            x = str(a)
    except:
        pass
    return x

x="make a note that I have to write on 26"
"""
try:
    with sr.Microphone() as source:
        print "listening"
        #response.configure(text="I'm asleep")
        audio = r.listen(source)
        a = r.recognize_google(audio)
        print "heard"
        print a
        x = str(a)
except:
    print "error"
    """

item=[]

def what():
    what = re.search('that',x)
    if what==None:
        what = re.search('to',x)
    if what == None:
        engine.say("What would you want to make note about?")
        engine.runAndWait()
        what = sun()
        return what  
    what = what.span()
    z1 = what[1]
    what = x[z1+1:]
    return what

    

   
#print x
def when():
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
        at = datetime.datetime.strptime("00:00:00","%H:%M:%S")
        at.strftime("%Y-%m-%d %H:%M:%S")
        
    at=str(at)
    at = at[10:]
    on = str(on)
    on = on[:10]   
    on = on + at
    on = datetime.datetime.strptime(on,"%Y-%m-%d %H:%M:%S")
    return on.strftime("%Y-%m-%d %H:%M:%S")
    


    
        
datecreated=datetime.datetime.now()
item.insert(0,what())
item.insert(1,when())
#item.insert(2,when())
item.insert(2,'0')

print item
t=[6,'note 6',datetime.datetime.now(),0]
c.execute("insert into notes(text,date_created,locked) values(?,?,?)",item)
con.commit()
#con.close()
print "enetered"

c=con.cursor()
vnote= c.execute("select text from notes where nid=2")
for row in vnote:
    print row[0]
