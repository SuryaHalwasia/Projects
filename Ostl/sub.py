import time
from twilio.rest import Client 
accountSID='ACe66b77535ede54f3e2a7bcf5efb49b91'
from tkinter import *
root=Tk()
root.state('zoomed')
ok=PhotoImage(file="ok.png")
def click2():
        msg=t1.get(0.0,END)
        message=twilioCli.messages.create(body=msg,from_=myTwilioNumber,to=myCellPhone)
        a3=Label(root,height=500,width=400,bg="#ffffff")
        a3.place(x=0,y=0)
        l2=Label(a3,text="Message Sent!",bg="#ffdbac",height=2,width=20,font=("Arial","8"))
        l2.place(x=170,y=140)
def click1():
        myTwilioNumber="+12014307514"
        global t1
        myCellPhone=no.get()
        a2=Label(root,height=600,width=700,bg="#ffffff")
        a2.place(x=0,y=0)
        t1=Text(a2,height=20,width=40,wrap=WORD)
        t1.place(x=470,y=140)
        b2=Button(a2,image=ok,command=click2,height=50,width=50)
        b2.place(x=330,y=360)

def click():
        authToken=auth.get()
        twilioCli=Client(accountSID, authToken)
        l1.config(text="Number")
        e2=Entry(a1,text=no,width=40)
        e2.place(x=470,y=140)
        b1.config(command=click1)

myTwilioNumber="+12014307514"
myCellPhone="+919320372678"
t1=Text()       
a1=Label(root,height=500,width=400,bg="#ffffff")
a1.place(x=0,y=0)
auth=StringVar()
no=StringVar()
l1=Label(a1,text="Auth Number",bg="#ffdbac",height=2,width=20,font=("Arial","8"))
l1.place(x=170,y=140)
e1=Entry(a1,text=auth,width=40,show="*")
e1.place(x=470,y=140)
b1=Button(a1,image=ok,command=click,height=50,width=50)
b1.place(x=330,y=360)
twilioCli=Client(accountSID, '129e510e19dc45f44102f1c96291b614')
#message=twilioCli.messages.create(body="hi shreeya! Surya here",from_=myTwilioNumber,to=myCellPhone)
