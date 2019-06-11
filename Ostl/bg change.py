from tkinter import *
root=Tk()
root.state('zoomed')
img1=PhotoImage(file="images.png")
img2=PhotoImage(file="images2.png")
img3=PhotoImage(file="images3.png")
img4=PhotoImage(file="images4.png")
img5=PhotoImage(file="images5.png")
img6=PhotoImage(file="images6.png")
ima1=PhotoImage(file="img.png")
ima2=PhotoImage(file="img2.png")
ima3=PhotoImage(file="img3.png")
ima4=PhotoImage(file="img4.png")
ima5=PhotoImage(file="img5.png")
ima6=PhotoImage(file="img6.png")
def cmd():
    l1.config(image=img1)
def cmd2():
    l1.config(image=img2)
def cmd3():
    l1.config(image=img3)
def cmd4():
    l1.config(image=img4)
def cmd5():
    l1.config(image=img5)
def cmd6():
    l1.config(image=img6)
l1=Label(root,image=img1)
l1.place(x=0, y=0, relwidth=1, relheight=1)
b1=Button(root,image=ima1,height=150,width=200,relief="flat",command=cmd)
b1.place(x=50,y=130)
b2=Button(root,image=ima2,height=150,width=200,relief="flat",command=cmd2)
b2.place(x=600,y=130)
b3=Button(root,image=ima3,height=150,width=200,relief="flat",command=cmd3)
b3.place(x=1150,y=130)
b4=Button(root,image=ima4,height=150,width=200,relief="flat",command=cmd4)
b4.place(x=50,y=430)
b5=Button(root,image=ima5,height=150,width=200,relief="flat",command=cmd5)
b5.place(x=600,y=430)
b6=Button(root,image=ima6,height=150,width=200,relief="flat",command=cmd6)
b6.place(x=1150,y=430)
mainloop()



