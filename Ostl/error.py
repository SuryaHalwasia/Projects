from tkinter import *
root=Tk()
root.geometry("470x300")
img1=PhotoImage(file="a1.png")
try:
    1/0
except:
    l1=Label(root,image=img1,height=600)
    l1.place(x=0, y=0, relwidth=1, relheight=1)
finally:
    mainloop()
    






