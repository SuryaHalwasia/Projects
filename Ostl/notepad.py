from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import keyword
root=Tk()
root.geometry("700x400")
#root.state("zoomed")
root.title("Notepad")
n11=0
def cmd1():
    e1.delete(0.0,END)
    root.title("Notepad")
    var.set("Notepad")
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
e1=Text(root,height=600,width=400,wrap=WORD)
h1=Scrollbar(root,orient=VERTICAL, command=e1.yview)
e1.configure(yscrollcommand=h1.set)
h1.pack(side=RIGHT,fill=Y)
h2=Scrollbar(root,orient=HORIZONTAL, command=e1.xview)
e1.configure(xscrollcommand=h2.set)
h2.pack(side=BOTTOM,fill=X)
e1.pack()
var=StringVar()
e2=Entry(root,textvariable=var)
e2.insert(END,"Notepad")
menu=Menu(root)
root.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="New",command=cmd1)
filemenu.add_command(label="Open",command=cmd2)
filemenu.add_command(label="Save",command=cmd3)
filemenu.add_command(label="Go back")

