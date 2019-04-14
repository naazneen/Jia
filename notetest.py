import re
import datetime

x = "make a note that i have class tomo at 830 pm"
item=[]
that = re.search('that',x)
if that:
    that = that.span()
    z1 = that[1]
    that = x[z1+1:]
   
#print x

at = re.search(' at',x)
if at:
    at = at.span()
    z2 = at[1]
    at = x[z2+1:]
    

to = re.search('to',x)
if to:
    to = to.span()
    z3 = to[1]
    to = x[z3+1:]
    
        
datecreated=datetime.datetime.now()
item.insert(0,that)
item.insert(1,datecreated.strftime("%Y-%m-%d %H:%M:%S"))
item.insert(2,at)

print item

