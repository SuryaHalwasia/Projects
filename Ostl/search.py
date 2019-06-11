import webbrowser
from tkinter import *
root=Tk()
root.geometry("900x400")
root.title("Search")
imgbing=PhotoImage(file="bing.png")
imgwiki=PhotoImage(file="wiki.png")
imgyou=PhotoImage(file="you.png")
imggoog=PhotoImage(file="google.png")
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
f1=Frame(root,height=370,width=500)
f1.pack()
l1=Button(f1,image=imgbing,height=45, width=50,command=cmd)
l1.place(x=70,y=40)
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
mainloop()
