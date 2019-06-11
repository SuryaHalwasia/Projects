import datetime,time,threading
import pygame
from tkinter import *
file = 'alarm.mp3'
root=Tk()
root.geometry("900x700")
imag=PhotoImage(file="alarm.png")
imag1=PhotoImage(file="cal.png")
img=PhotoImage(file="images6.png")
ok=PhotoImage(file="ok.png")
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
n=1
n1=2
n2=0
label="a"
hr=IntVar()
mins=IntVar()
year=IntVar()
month=IntVar()
day=IntVar()
lab=StringVar() 
def click():
    global n
    global n1
    n=hr.get()
    n1=mins.get()
    threadObj=threading.Thread(target=org)
    threadObj.start()
def click1():
    global n
    global n1
    global n2
    global label
    n=year.get()
    n1=month.get()
    n2=day.get()
    label=lab.get()
    threadObj=threading.Thread(target=org1)
    threadObj.start()
def cmd():
    a1=Label(f1,height=500,width=400,bg="#ffffff")
    a1.place(x=0,y=230)
    l1=Label(a1,text="Hour",bg="#ffdbac",height=2,width=5,font=("Arial","8"))
    l1.place(x=170,y=120)
    e1=Spinbox(a1,from_=0, to=23, textvariable=hr,width=10)
    e1.place(x=470,y=120)
    l2=Label(a1,text="Minutes",bg="#ffdbac",height=2,width=5,font=("Arial","8"))
    l2.place(x=170,y=240)
    e2=Spinbox(a1,from_=0, to=59, textvariable=mins,width=10)
    e2.place(x=470, y=240)
    b1=Button(a1,image=ok,command=click,height=50,width=50)
    b1.place(x=330,y=360)
def cmd1():
    a1=Label(f1,height=500,width=400,bg="#ffffff")
    a1.place(x=0,y=230)
    l1=Label(a1,text="Year",bg="#ffdbac",height=2,width=5,font=("Arial","8"))
    l1.place(x=170,y=50)
    e1=Spinbox(a1,from_=2019, to=2100, textvariable=year,width=10)
    e1.place(x=470,y=50)
    l2=Label(a1,text="Month",bg="#ffdbac",height=2,width=5,font=("Arial","8"))
    l2.place(x=170,y=110)
    e2=Spinbox(a1,from_=1,to=12,textvariable=month,width=10)
    e2.place(x=470, y=110)
    l3=Label(a1,text="Day",bg="#ffdbac",height=2,width=5,font=("Arial","8"))
    l3.place(x=170,y=170)
    e3=Spinbox(a1,from_=1,to=31,textvariable=day,width=10)
    e3.place(x=470, y=170)
    l4=Label(a1,text="Reminder",bg="#ffdbac",height=2,width=5,font=("Arial","8"))
    l4.place(x=170,y=230)
    e4=Entry(a1,text=lab,width=10)
    e4.place(x=470,y=230)
    b1=Button(a1,image=ok,height=50,width=50,command=click1)
    b1.place(x=330,y=300)
def org():
    dt=datetime.datetime.now()
    while(n!=dt.hour):
        dt=datetime.datetime.now()
        time.sleep(30)
    while(n1!=dt.minute):
        dt=datetime.datetime.now()
        time.sleep(5)
    for i in range(4):
        pygame.mixer.music.play()
def org1():
    dt=datetime.datetime.now()
    while(n!=dt.year):
        dt=datetime.datetime.now()
        time.sleep(30)
    while(n1!=dt.month):
        dt=datetime.datetime.now()
        time.sleep(30)
    while(n2!=dt.day):
        dt=datetime.datetime.now()
        time.sleep(30)
    for i in range(4):
        pygame.mixer.music.play()
    l2=Label(f1,text=label)
    l2.place(x=300,y=300)
        
f1=Label(root,image=img)
f1.place(x=0,y=0,relwidth=1, relheight=1)
b1=Button(f1,image=imag,height=75,width=75,command=cmd)
b1.place(x=170,y=140)
b2=Button(f1,image=imag1,height=75,width=75,command=cmd1)
b2.place(x=470,y=140)

root.mainloop()




