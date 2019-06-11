import pygame
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
file = 'a.mp3'
pygame.init()
pygame.mixer.init()

flag=1;#not paused
def cmd():
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
def cmd1():
    pygame.mixer.music.stop()
    b2.config(image=img3)
def cmd2():
    global flag
    if(flag==1):
        flag=0
        pygame.mixer.music.pause()
        b2.config(image=img1)
    elif(flag==0):
        flag=1
        pygame.mixer.music.unpause()
        b2.config(image=img3)
def cm1():
    global file
    file=filedialog.askopenfilename()
root = Tk()
menu=Menu(root)
root.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label="Menu",menu=filemenu)
filemenu.add_command(label="Open",command=cm1)

img=PhotoImage(file="music.png")
img1=PhotoImage(file="play.png")
img2=PhotoImage(file="stop.png")
img3=PhotoImage(file="pause.png")
frame=Label(root,image=img)
frame.pack()
b1=Button(frame, height=50, width=50,image=img1,command=cmd)
b1.place(x=155,y=60)
b2=Button(frame, height=50, width=50,image=img3,command=cmd2)
b2.place(x=275,y=60)
b3=Button(frame, height=50, width=50,image=img2,command=cmd1)
b3.place(x=395,y=60)
root.mainloop()

