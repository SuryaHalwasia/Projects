from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import pygame
import keyword
import datetime,time,threading
import webbrowser
import speech_recognition as sr
from twilio.rest import Client
import subprocess
from gtts import gTTS
import os
root=Tk()
flag=0
pygame.init()
pygame.mixer.init()
root.state("zoomed")
root.title("App")
wall=6
img1=PhotoImage(file="images.png")
img2=PhotoImage(file="images2.png")
img3=PhotoImage(file="images3.png")
img4=PhotoImage(file="images4.png")
img5=PhotoImage(file="images5.png")
img6=PhotoImage(file="images6.png")
ima=PhotoImage(file="b1.png")
ima1=PhotoImage(file="b2.png")
ima2=PhotoImage(file="notie.png")
ima3=PhotoImage(file="see.png")
ima4=PhotoImage(file="text.png")
ima5=PhotoImage(file="calc.png")
ima11=PhotoImage(file="img.png")
ima21=PhotoImage(file="img2.png")
ima31=PhotoImage(file="img3.png")
ima41=PhotoImage(file="img4.png")
ima51=PhotoImage(file="img5.png")
ima61=PhotoImage(file="img6.png")
imag=PhotoImage(file="alarm.png") #alarm
imag1=PhotoImage(file="cal.png")    #calendar
ok=PhotoImage(file="ok.png") #ok
stopala=PhotoImage(file="stopala.png")
imgplay=PhotoImage(file="play.png")
imgstop=PhotoImage(file="stop.png")
imgpause=PhotoImage(file="pause.png")
imusic=PhotoImage(file="music.png")
imgbing=PhotoImage(file="bing.png")
imgwiki=PhotoImage(file="wiki.png")
imgyou=PhotoImage(file="you.png")
imggoog=PhotoImage(file="google.png")
alarmtune="alarm.mp3"
file = 'a.mp3'
file3 = 'alar.mp3'
file4="musi1.mp3"
file5="no.mp3"
file6="sear.mp3"
fg1="goog.mp3"
fg2="wiki.mp3"
fg3="yt.mp3"
flag1=1
hr=IntVar()
mins=IntVar()
year=IntVar()
month=IntVar()
day=IntVar()
lab=StringVar()
n=1
oz=1
var=StringVar()
auth=StringVar()
no=StringVar()
n1=2
n2=0
n11=0
nn="12"
label="a"
w1=1
sea=1
def speak1():
    global sea
    while(sea!=0):
        print("3")
        r = sr.Recognizer()
        with sr.Microphone() as source:                # use the default microphone as the audio source
            audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
        try:
            if((r.recognize_google(audio)=="ok google")or
               ((r.recognize_sphinx(audio)=="ok google"))):
                print("google")
                pygame.mixer.music.load(fg1)
                pygame.mixer.music.play()
                with sr.Microphone() as source:                # use the default microphone as the audio source
                    audio = r.listen(source)
                    search="https://www.google.co.in/search?source=hp&ei=2vmoXMSeLa_ez7\
                            sPqp-AyAs&q="+audio+"&btnK=Google+Search&oq="+audio+"&gs_l=psy-ab.3..35i39j0l\
                            2j0i131l2j0j0i131j0l3.1007.1707..2012...0.0..1.503.878.0j2j5-1....1..0...\
                            .1..gws-wiz.....0.4Gi7x9po8AE"
                    webbrowser.open(search)
            elif((r.recognize_google(audio)=="ok wiki")or
               ((r.recognize_sphinx(audio)=="ok wiki"))):
                print("wiki")
                pygame.mixer.music.load(fg2)
                pygame.mixer.music.play()
                with sr.Microphone() as source:                # use the default microphone as the audio source
                    audio = r.listen(source)
                    search="https://en.wikipedia.org/wiki/"+e
                    webbrowser.open(search)
            elif((r.recognize_google(audio)=="ok youtube")or
               ((r.recognize_sphinx(audio)=="ok youtube"))):
                print("youtube")
                pygame.mixer.music.load(fg3)
                pygame.mixer.music.play()
                with sr.Microphone() as source:                # use the default microphone as the audio source
                    audio = r.listen(source)
                    search="https://www.youtube.com/results?search_query="+e
                    webbrowser.open(search)
        except:
            print(audio)
def speak():
    global flag
    print(flag)
    while(flag!=1):
        print("3")
        r = sr.Recognizer()
        with sr.Microphone() as source:                # use the default microphone as the audio source
            audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
        try:
            if((r.recognize_google(audio)=="open alarms")or
               ((r.recognize_sphinx(audio)=="open alarms"))):
                print("3")
                pygame.mixer.music.load(file3)
                pygame.mixer.music.play()
                time.sleep(1)
                alarm(w1)
                flag=1
            elif((r.recognize_google(audio)=="open music")or
               ((r.recognize_sphinx(audio)=="open music"))):
                print("31")
                pygame.mixer.music.load(file4)
                pygame.mixer.music.play()
                time.sleep(1)
                music()
                flag=1
            elif((r.recognize_google(audio)=="notepad")or
               ((r.recognize_sphinx(audio)=="notepad"))):
                print("32")
                pygame.mixer.music.load(file5)
                pygame.mixer.music.play()
                time.sleep(1)
                notepad()
                flag=1
            elif((r.recognize_google(audio)=="search")or(r.recognize_sphinx(audio)=="search")):
                print("33")
                pygame.mixer.music.load(file6)
                pygame.mixer.music.play()
                time.sleep(1)
                search(w1)
                flag=1
        except:                           
            pass
def alarm1():
    global flag
    flag=1
    alarm(w1)
def alarm(wall):
    frame0=Frame(root,height=2000,width=2000).pack()
    root.geometry("2000x2000")
    root.title("alarm")
    pygame.mixer.music.load(alarmtune)
    f1=Label(frame0,image=img6)
    f1.place(x=0,y=0,relwidth=1, relheight=1)
    if(wall==1):
        f1.config(image=img1)
    elif(wall==2):
        f1.config(image=img2)
    elif(wall==3):
        f1.config(image=img3)
    elif(wall==4):
        f1.config(image=img4)
    elif(wall==5):
        f1.config(image=img5)
    else:
        f1.config(image=img6)
    def cmdd1():
        name=filedialog.askopenfilename()
        global alarmtune
        alarmtune=name
        pygame.mixer.music.load(alarmtune)
    def cmdd2():
        main(wall)
    menu=Menu(root)
    root.config(menu=menu)
    filemenu=Menu(menu)
    menu.add_cascade(label="File",menu=filemenu)
    filemenu.add_command(label="Change Tune",command=cmdd1)
    filemenu.add_command(label="Go back",command=cmdd2)
    def stop():
        pygame.mixer.music.stop()
        b1.config(image=imag)
        b1.config(command=click)
    def stop1():
        pygame.mixer.music.stop()
        b2.config(image=imag1)
        b2.config(command=click1)
        messagebox.showinfo("Reminder", label)
    def click():
        global n
        global n1
        n=hr.get()
        n1=mins.get()
        threadObj1=threading.Thread(target=org)
        threadObj1.start()
    def click1():
        global n
        global n1
        global n2
        global label
        n=year.get()
        n1=month.get()
        n2=day.get()
        label=lab.get()
        threadObj1=threading.Thread(target=org1)
        threadObj1.start()
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
            b1.config(image=stopala)
            b1.config(command=stop)
            
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
            b2.config(image=stopala)
            b2.config(command=stop1)
            
    b1=Button(f1,image=imag,height=75,width=75,command=cmd)  
    b1.place(x=170,y=140)
    b2=Button(f1,image=imag1,height=75,width=75,command=cmd1)
    b2.place(x=470,y=140)
def music1():
    global flag
    flag=1
    music()
def music():
    print("123")
    frame0=Frame(root,height=297,width=526).pack()
    f2=Label(frame0,image=imusic,height=297,width=526)
    f2.place(x=0,y=0,relwidth=1, relheight=1)
    root.geometry("526x297")
    root.title("Music Box")
    def cmdd2():
        main(wall)
    def cmd():
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
    def cmd1():
        pygame.mixer.music.stop()
        b2.config(image=imgpause)
    def cmd2():
        global flag1
        if(flag1==1):
            flag1=0
            pygame.mixer.music.pause()
            b2.config(image=imgplay)
        elif(flag1==0):
            flag1=1
            pygame.mixer.music.unpause()
            b2.config(image=imgpause)
    def cm1():
        global file
        file=filedialog.askopenfilename()
    menu=Menu(root)
    root.config(menu=menu)
    filemenu=Menu(menu)
    menu.add_cascade(label="Menu",menu=filemenu)
    filemenu.add_command(label="Open",command=cm1)
    filemenu.add_command(label="Go back",command=cmdd2)
    b1=Button(f2, height=50, width=50,image=imgplay,command=cmd)
    b1.place(x=155,y=60)
    b2=Button(f2, height=50, width=50,image=imgpause,command=cmd2)
    b2.place(x=275,y=60)
    b3=Button(f2, height=50, width=50,image=imgstop,command=cmd1)
    b3.place(x=395,y=60)
def notepad1():
    global flag
    flag=1
    notepad()
def notepad():
    f4=Frame(root,height=400,width=600)
    f4.place(x=0,y=0,relwidth=1, relheight=1)
    frame0=Label(f4,height=400,width=600).pack()
    root.geometry("700x400")
    root.title("Notepad")
    def cmd1():
        e1.delete(0.0,END)
        root.title("Notepad")
        var.set("Notepad")
    def cmdd2():
        main(wall)
    def cmd2():
        name=filedialog.askopenfilename()
        filen=open(name,'r')
        f1=filen.read()
        filen.close()
        e1.delete(0.0,END)
        e1.insert(END,f1)
        root.title(name)
        var.set(name)
    def cmd3():
        nn=var.get()
        if(nn[-2]+nn[-1])=="py":
            for s1 in keyword.kwlist:
                s1=s1+" "
                idx = '1.0'
                while 1:
                    idx = e1.search(s1, idx, nocase=1, stopindex=END)
                    if not idx:
                        break
                    lastidx = '%s+%dc' % (idx, len(s1))
                    e1.tag_add('found', idx, lastidx)
                    idx = lastidx
                e1.tag_config('found', foreground='purple')
        if(nn!="Notepad"):
            file=open(nn,'w')
            file.write(e1.get(0.0,END))
            file.close()
        else:
            global n11
            n11=n11+1
            st="Untitled"+str(n11)+".txt"
            file1=filedialog.asksaveasfilename(initialfile=st)
            try:
                file=open(file1,'w')
                file.write(e1.get(0.0,END))
                file.close()
                var.set(file1)
                root.title(file1)
            except:
                n11=n11-1
    e1=Text(frame0,height=600,width=400,wrap=WORD)
    h1=Scrollbar(frame0,orient=VERTICAL, command=e1.yview)
    e1.configure(yscrollcommand=h1.set)
    h1.pack(side=RIGHT,fill=Y)
    h2=Scrollbar(frame0,orient=HORIZONTAL, command=e1.xview)
    e1.configure(xscrollcommand=h2.set)
    h2.pack(side=BOTTOM,fill=X)
    e1.place(x=0,y=0)
    e2=Entry(root,textvariable=var)
    e2.insert(END,"Notepad")
    menu=Menu(root)
    root.config(menu=menu)
    filemenu=Menu(menu)
    menu.add_cascade(label="File",menu=filemenu)
    filemenu.add_command(label="New",command=cmd1)
    filemenu.add_command(label="Open",command=cmd2)
    filemenu.add_command(label="Save",command=cmd3)
    filemenu.add_command(label="Go back",command=cmdd2)
def search1():
    global flag
    flag=1
    search(w1)
def search(wall):
    root.geometry("900x400")
    root.title("Search")
    frame0=Frame(root,height=2000,width=2000).pack()
    f1=Label(frame0,image=img6)
    f1.place(x=0,y=0,relwidth=1, relheight=1)
    if(wall==1):
        f1.config(image=img1)
    elif(wall==2):
        f1.config(image=img2)
    elif(wall==3):
        f1.config(image=img3)
    elif(wall==4):
        f1.config(image=img4)
    elif(wall==5):
        f1.config(image=img5)
    else:
        f1.config(image=img6)
    def cmd():
        e=e1.get(0.0,END)
        search="https://www.bing.com/search?q="+e+"&form=EDGEAR&qs=AS&cvid=9fb3f042d83b48ce9c77e05b3d287442&cc=IN&setlang=en-US \
        &elv=AQj93OAhDTi*HzTv1paQdngdqlwkJ3SELDpFDN9t7SsRZcLft44BpuXatLcQqjLIAOa8VLUSnAethQHXPCNrvX0GNMW7A3ByZE6I%21jLOda6O&PC=LCTS"
        webbrowser.open(search)
    def cmd1():
        e=e2.get(0.0,END)
        search="https://en.wikipedia.org/wiki/"+e
        webbrowser.open(search)
    def cmd2():
        e=e3.get(0.0,END)
        search="https://www.youtube.com/results?search_query="+e
        webbrowser.open(search)
    def cmd3():
        e=e4.get(0.0,END)
        search="https://www.google.co.in/search?source=hp&ei=2vmoXMSeLa_ez7\
        sPqp-AyAs&q="+e+"&btnK=Google+Search&oq="+e+"&gs_l=psy-ab.3..35i39j0l\
        2j0i131l2j0j0i131j0l3.1007.1707..2012...0.0..1.503.878.0j2j5-1....1..0...\
        .1..gws-wiz.....0.4Gi7x9po8AE"
        webbrowser.open(search)
    def cmdd2():
        main(wall)
    l1=Button(f1,image=imgbing,height=45, width=50,command=cmd)
    l1.place(x=70,y=40)
    threadObj1=threading.Thread(target=speak1)
    threadObj1.start()
    e1=Text(f1,width=30,height=2,font=("Arial","12"))
    e1.place(x=230,y=45)
    l2=Button(f1,image=imgwiki,height=45, width=50,command=cmd1)
    l2.place(x=70,y=110)
    e2=Text(f1,width=30,height=2,font=("Arial","12"))
    e2.place(x=230,y=115)
    l3=Button(f1,image=imgyou,height=45, width=50,command=cmd2)
    l3.place(x=70,y=180)
    e3=Text(f1,width=30,height=2,font=("Arial","12"))
    e3.place(x=230,y=185)
    l4=Button(f1,image=imggoog,height=45, width=50,command=cmd3)
    l4.place(x=70,y=250)
    e4=Text(f1,width=30,height=2,font=("Arial","12"))
    e4.place(x=230,y=255)
    menu=Menu(root)
    root.config(menu=menu)
    filemenu=Menu(menu)
    menu.add_cascade(label="File",menu=filemenu)
    filemenu.add_command(label="Go back",command=cmdd2)
def sms1():
    global flag
    flag=1
    sms(w1)
def sms(wall):
    def cmdd2():
        main(wall)
    root.geometry("2000x2000")
    root.title("Text")
    frame0=Frame(root,height=2000,width=2000).pack()
    f1=Label(frame0,image=img6)
    f1.place(x=0,y=0,relwidth=1, relheight=1)
    if(wall==1):
        f1.config(image=img1)
    elif(wall==2):
        f1.config(image=img2)
    elif(wall==3):
        f1.config(image=img3)
    elif(wall==4):
        f1.config(image=img4)
    elif(wall==5):
        f1.config(image=img5)
    else:
        f1.config(image=img6)
    def click2():
        msg=t1.get(0.0,END)
        message=twilioCli.messages.create(body=msg,from_=myTwilioNumber,to=myCellPhone)
        a3=Label(f1,height=500,width=400,bg="#ffffff")
        a3.place(x=0,y=0)
        l2=Label(a3,text="Message Sent!",bg="#ffdbac",height=2,width=20,font=("Arial","8"))
        l2.place(x=170,y=140)
    def click1():
        myTwilioNumber="+12014307514"
        global t1
        myCellPhone=no.get()
        a2=Label(f1,height=600,width=700,bg="#ffffff")
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
    t1=Text()       
    a1=Label(f1,height=500,width=400,bg="#ffffff")
    a1.place(x=0,y=0)
    menu=Menu(root)
    root.config(menu=menu)
    filemenu=Menu(menu)
    menu.add_cascade(label="File",menu=filemenu)
    filemenu.add_command(label="Go back",command=cmdd2)
    l1=Label(a1,text="Auth Number",bg="#ffdbac",height=2,width=20,font=("Arial","8"))
    l1.place(x=170,y=140)
    e1=Entry(a1,text=auth,width=40,show="*")
    e1.place(x=470,y=140)
    b1=Button(a1,image=ok,command=click,height=50,width=50)
    b1.place(x=330,y=360)
    twilioCli=Client(accountSID, '129e510e19dc45f44102f1c96291b614')
def calci():
    subprocess.Popen("C:\Windows\WinSxS\wow64_microsoft-windows-calc_31bf3856ad364e35_10.0.17134.1_none_999337e4b8471fe2\calc.exe")
def main(wall):
    root.title("App")
    root.geometry("2000x2000")
    global flag
    global w1
    w1=wall
    flag=0
    f1=Frame(root,height=2000,width=2000).pack()
    menu=Menu(root)
    def cmdz(wall):
        def cmd():
            global oz
            l1z.config(image=img1)
            oz=1
        def cmd2():
            global oz
            l1z.config(image=img2)
            oz=2
        def cmd3():
            global oz
            l1z.config(image=img3)
            oz=3
        def cmd4():
            global oz
            l1z.config(image=img4)
            oz=4
        def cmd5():
            global oz
            l1z.config(image=img5)
            oz=5
        def cmd6():
            global oz
            l1z.config(image=img6)
            oz=6
        l1z=Label(f1,image=img1)
        l1z.place(x=0, y=0, relwidth=1, relheight=1)
        if(wall==1):
            l1z.config(image=img1)
        elif(wall==2):
            l1z.config(image=img2)
        elif(wall==3):
            l1z.config(image=img3)
        elif(wall==4):
            l1z.config(image=img4)
        elif(wall==5):
            l1z.config(image=img5)
        else:
            l1z.config(image=img6)
        def cmddo():
            main(oz)
        
        b1z=Button(l1z,image=ima11,height=150,width=200,relief="flat",command=cmd)
        b1z.place(x=50,y=130)
        b2z=Button(l1z,image=ima21,height=150,width=200,relief="flat",command=cmd2)
        b2z.place(x=600,y=130)
        b3z=Button(l1z,image=ima31,height=150,width=200,relief="flat",command=cmd3)
        b3z.place(x=1150,y=130)
        b4z=Button(l1z,image=ima41,height=150,width=200,relief="flat",command=cmd4)
        b4z.place(x=50,y=430)
        b5z=Button(l1z,image=ima51,height=150,width=200,relief="flat",command=cmd5)
        b5z.place(x=600,y=430)
        b6z=Button(l1z,image=ima61,height=150,width=200,relief="flat",command=cmd6)
        b6z.place(x=1150,y=430)
        menu=Menu(root)
        root.config(menu=menu)
        filemenu=Menu(menu)
        menu.add_cascade(label="File",menu=filemenu)
        filemenu.add_command(label="Go back",command=cmddo)
    def cmdd1():
        cmdz(wall)
    def cmdd2():
        result=messagebox.askyesno("Quit","Do you wanna quit?")
        if(result==True):
            root.destroy()
        else:
            pass
    root.config(menu=menu)
    filemenu=Menu(menu)
    menu.add_cascade(label="File",menu=filemenu)
    filemenu.add_command(label="Change Background",command=cmdd1)
    filemenu.add_command(label="Quit",command=cmdd2)
    lm=Label(f1,image=img1)
    lm.place(x=0, y=0, relwidth=1, relheight=1)
    if(wall==1):
        lm.config(image=img1)
    elif(wall==2):
        lm.config(image=img2)
    elif(wall==3):
        lm.config(image=img3)
    elif(wall==4):
        lm.config(image=img4)
    elif(wall==5):
        lm.config(image=img5)
    else:
        lm.config(image=img6)
    threadObj=threading.Thread(target=speak)
    threadObj.start()
    b1=Button(lm,image=ima,height=70,width=90,command=alarm1)
    b1.place(x=60,y=120)
    l1=Label(text="Alarm",height=1,width=5, bg="#ffffff",font=("Arial","10","bold"))
    l1.place(x=85,y=200)
    b2=Button(lm,image=ima1,height=70,width=90,command=music1)
    b2.place(x=360,y=120)
    l2=Label(text="Music",height=1,width=5, bg="#ffffff",font=("Arial","10","bold"))
    l2.place(x=385,y=200)
    l1.place(x=85,y=200)
    b3=Button(lm,image=ima2,height=70,width=90,command=notepad1)
    b3.place(x=660,y=120)
    l3=Label(text="Notepad",height=1,width=8, bg="#ffffff",font=("Arial","10","bold"))
    l3.place(x=683,y=200)
    b4=Button(lm,image=ima3,height=70,width=90,command=search1)
    b4.place(x=660,y=420)
    l4=Label(text="Search",height=1,width=8, bg="#ffffff",font=("Arial","10","bold"))
    l4.place(x=675,y=500)
    b5=Button(lm,image=ima4,height=70,width=90,command=sms1)
    b5.place(x=960,y=420)
    l5=Label(text="Text",height=1,width=8, bg="#ffffff",font=("Arial","10","bold"))
    l5.place(x=975,y=500)
    b6=Button(lm,image=ima5,height=70,width=90,command=calci)
    b6.place(x=1260,y=420)
    l6=Label(text="Calculator",height=1,width=8, bg="#ffffff",font=("Arial","10","bold"))
    l6.place(x=1275,y=500)
main(6)
mainloop()
