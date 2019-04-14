import Tkinter as tk
import sqlite3

root=tk.Tk()
frame5=tk.Frame(root,width=340,height=340,background="White")
frame5.grid(row=0,column=0,columnspan=3)


conn = sqlite3.connect('C:\Users\ABDUL\Downloads\sqlite-tools-win32-x86-3240000\sqlite-tools-win32-x86-3240000\dbva.db')
print "Opened database successfully";
cursor = conn.execute("SELECT * from notes")

i=1
j=0

def v_note(x):
    print "note"
    print x
    

def v_notedetails(x):
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
    b = tk.Label(frame5, text=c)
    b.grid(row=i, column=j,sticky="W")
    notel=tk.Label(frame5, text="report",height=20,width=10,bg="Black",fg="White")
    i=i+1



root.mainloop()

