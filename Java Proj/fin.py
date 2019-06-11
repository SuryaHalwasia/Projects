from tkinter import *
import sqlite3
root=Tk()
root.geometry("2000x2000")
db=sqlite3.connect('tests.db')
cursor=db.cursor()
img=PhotoImage(file="images.png")
img2=PhotoImage(file="images2.png")
img1=PhotoImage(file="csi1.png")
imga=PhotoImage(file="robot.png")
imgb=PhotoImage(file="pb.png")
imgc=PhotoImage(file="eh1.png")
imgd=PhotoImage(file="ai.png")
frame0=Frame(root,height=2000,width=2000)
frame=Frame(root,height=500,width=1000,background="#F3EAE7")
frame1=Frame(root,height=500,width=1000,background="#F3EAE7")
frame2=Frame(root,height=1000,width=2000)
name=StringVar()
username=StringVar()
username1=StringVar()
password=StringVar()
password1=StringVar()
passwordr=StringVar()
r1=IntVar()
a1=IntVar()
p1=IntVar()
ev=IntVar()
def org():
	frame0=Frame(root,height=2000,width=2000).pack()
	panel=Label(frame0,image=img).place(x=0,y=0)
	csi=Label(frame0,image=img1,relief="raised").place(x=30,y=30)
	l1=Label(frame0,text="Computer Society Of India",fg="white",bg='black',font="Helvatica 50 italic",relief="sunken").place(x=270,y=40)
	b1 = Button(frame0,text='REGISTER',fg="yellow",bg="black",font = "Helvetica 16 bold italic",relief="raised",command=play).place(x=400,y=200)
	b2= Button(frame0,text='LOGIN',fg="yellow",bg="black",font = "Helvetica 16 bold italic",relief="raised",command=play1).place(x=750,y=200)
	b3= Button(frame0,text='CREATE',fg="yellow",bg="black",font = "Helvetica 16 bold italic",relief="raised",command=create).place(x=100,y=200)
	b4= Button(frame0,text='QUIT',fg="yellow",bg="black",font = "Helvetica 16 bold italic",relief="raised",command=quit).place(x=990,y=200)	
def play():
	frame=Frame(root,height=500,width=1000,background="#F3EAE7").place(x=140,y=300)
	l1=Label(frame,text="NAME",fg='black',font=("Helvatica",17),bg='#F98F6C',width=8,relief='raised').place(x=200,y=370)
	l2=Label(frame,text="USERNAME",fg='black',font=("Helvatica",17),bg='#F98F6C',relief='raised').place(x=200,y=430)
	l3=Label(frame,text="PASSWORD",fg='black',font=("Helvatica",17),bg='#F98F6C',relief='raised').place(x=200,y=490)
	l4=Label(frame,text="REENTER PASSWORD",fg='black',font=("Helvatica",17),bg='#F98F6C',relief='raised').place(x=200,y=550)
	e1=Entry(frame,width=30,text=name,fg='black',font=('Arial',17,'italic')).place(x=500,y=370)
	e2=Entry(frame,width=30,text=username,fg='black',font=('Arial',17,'italic')).place(x=500,y=430)
	e3=Entry(frame,width=30,text=password,fg='black',font=('Arial',17,'italic'),show="*").place(x=500,y=490)
	e4=Entry(frame,width=30,text=passwordr,fg='black',font=('Arial',17,'italic'),show="*").place(x=500,y=550)
	b3 = Button(frame,text='SUBMIT',fg="yellow",bg="black",font = "Helvetica 16 bold italic",relief="raised",command=submit).place(x=600,y=600)
	name.set("")
	username.set("")
	password.set("")
	passwordr.set("")
def play1():
	frame1=Frame(root,height=500,width=1000,background="#F3EAE7").place(x=140,y=300)
	la=Label(frame1,text="USERNAME",fg='black',font=("Helvatica",17),bg='#F98F6C',relief='raised').place(x=200,y=370)
	lb=Label(frame1,text="PASSWORD",fg='black',font=("Helvatica",17),bg='#F98F6C',relief='raised').place(x=200,y=490)
	ea=Entry(frame1,width=30,text=username1,fg='black',font=('Arial',17,'italic')).place(x=500,y=370)
	eb=Entry(frame1,width=30,text=password1,fg='black',font=('Arial',17,'italic'),show="*").place(x=500,y=490)
	ba = Button(frame1,text='SUBMIT',fg="yellow",bg="black",font = "Helvetica 16 bold italic",relief="raised",command=submit1).place(x=600,y=600)
	username1.set("")
	password1.set("")
def play2():
	frame2=Frame(root,height=1000,width=2000).place(x=0,y=150)
	panel1=Label(frame2,image=img2).place(x=0,y=150)
	by = Button(frame2,text='BACK',fg="yellow",bg="black",font = "Helvetica 16 bold italic",relief="raised",command=org).place(x=400,y=200)
	bx = Button(frame2,text='PROCEED',fg="yellow",bg="black",font = "Helvetica 16 bold italic",relief="raised",command=play3).place(x=750,y=200)
	bx = Button(frame2,text='SUBMIT',fg="yellow",bg="black",font = "Helvetica 16 bold italic",relief="raised",command=submit2).place(x=990,y=200)
	panela=Label(frame2,image=imga).place(x=100,y=300)
	panelax=Label(frame2,text='ROBOTICS  Rs.225',fg="yellow",bg="black",font = "Helvetica 16 bold italic",relief="raised").place(x=130,y=550)
	e1=Entry(frame2,text=r1,width=5,fg='black',font=('Arial',17,'italic')).place(x=160,y=600)
	panel1=Label(frame2,image=imgb).place(x=400,y=300)
	panelax=Label(frame2,text='POWERBANK MAKING  Rs.100',fg="yellow",bg="black",font = "Helvetica 16 bold italic",relief="raised").place(x=390,y=550)
	e2=Entry(frame2,text=p1,width=5,fg='black',font=('Arial',17,'italic')).place(x=450,y=600)
	panel1=Label(frame2,image=imgc).place(x=700,y=300)
	panelax=Label(frame2,text='ETHICAL HACKING  Rs.100',fg="yellow",bg="black",font = "Helvetica 16 bold italic",relief="raised").place(x=710,y=550)
	e3=Entry(frame2,text=ev,width=5,fg='black',font=('Arial',17,'italic')).place(x=770,y=600)
	panel1=Label(frame2,image=imgd).place(x=1000,y=300)
	panelax=Label(frame2,text='ARTIFICIAL INTELLIGENCE  Rs.150',fg="yellow",bg="black",font = "Helvetica 16 bold italic",relief="raised").place(x=980,y=550)
	e4=Entry(frame2,width=5,text=a1,fg='black',font=('Arial',17,'italic')).place(x=1050,y=600)
def play3():
	frame3=Frame(root,height=1000,width=2000).place(x=0,y=150)
	panel1=Label(frame3,image=img2).place(x=0,y=150)
	by = Button(frame3,text='PRINT',fg="yellow",bg="black",font = "Helvetica 16 bold italic",relief="raised",command=play4).place(x=400,y=200)
	bx = Button(frame3,text='QUIT',fg="yellow",bg="black",font = "Helvetica 16 bold italic",relief="raised",command=quit).place(x=750,y=200)

def play4():
	x=username1.get()
	o=r1.get()
	p=p1.get()
	a=a1.get()  
	e=ev.get()
	y=0
	frame4=Frame(root,height=500,width=1000,background="#F3EAE7").place(x=140,y=300)
	l1=Label(frame4,text="NAME",fg='black',font=("Helvatica",17),bg='#F3EAE7').place(x=200,y=370)
	l11=Label(frame4,text=username1.get(),fg='black',font=("Helvatica",17),bg='#F3EAE7').place(x=400,y=370)
	cursor.execute("Select ITEMS from CUSTOMERS WHERE USERNAME='%s'"%(username1.get()))
	db.commit()
	for r in cursor.fetchone():
		print("Customer details :{} ".format(r))
		l22=Label(frame4,text=format(r),fg='black',font=("Helvatica",17),bg='#F3EAE7').place(x=400,y=430)

	l2=Label(frame4,text="ITEMS",fg='black',font=("Helvatica",17),bg='#F3EAE7').place(x=200,y=430)
	l3=Label(frame4,text="AMOUNT",fg='black',font=("Helvatica",17),bg='#F3EAE7').place(x=200,y=490)
	if(o>0):
		y=225*o
	if(p>0):
		y+=100*p   
	if(a>0):  
		y+=150*a  
	if(e>0):  
		y+=100*e
	print(y)
	l25=Label(frame4,text=str(y),fg='black',font=("Helvatica",17),bg='#F3EAE7').place(x=400,y=490)
	l4=Label(frame4,text="THANKYOU FOR SHOPPING!",fg='RED',font=("Helvatica",22),bg='#F3EAE7').place(x=400,y=600)
def submit():
	if((password.get())!=(passwordr.get())):
		X=Label(root,fg='RED',font=('Arial',17,'italic'),text='WRONG PASSWORD').place(x=800,y=550)
	else:
		n=name.get()
		u=username.get()
		p=password.get()
		i="0"
		insertsql='''insert INTO CUSTOMERS(NAME,USERNAME,PASSWORD,ITEMS)values('%s','%s','%s','%s')'''%(n,u,p,i)
		cursor.execute(insertsql)
		db.commit()
		cursor.execute('Select * from CUSTOMERS')
		for r in cursor.fetchall():
			print("Customer details :{} {} {} {}".format(r[0] ,r[1] ,r[2] ,r[3] ))
		return play1()
		
def dele(Frame):
	Frame.destroy()
	return org()
def create():
	db.execute('''CREATE TABLE CUSTOMERS(NAME TEXT NOT NULL,USERNAME PRIMARY KEY NOT NULL,PASSWORD VARCHAR[100],ITEMS VARCHAR[100]);''')
	db.commit()
def submit1():
	x=username1.get()
	y=password1.get()
	cursor.execute("Select * from CUSTOMERS where USERNAME='%s' AND PASSWORD='%s'"%(x,y))
	for r in cursor.fetchone():
		return play2()
def submit2():
	x=username1.get()
	r=r1.get()
	p=p1.get()
	a=a1.get()
	e=ev.get()
	t=""
	if(r>0):
		t+=str(r)+" robotics "
	if(p>0):
		t+=str(p)+"powerbank "
	if(a>0):
		t+=str(a)+" AI "
	if(e>0):
		t+=str(e)+" ethical "
	cursor.execute("UPDATE CUSTOMERS SET ITEMS='%s' where USERNAME='%s'"%(t,x))
	db.commit()
	cursor.execute('Select * from CUSTOMERS')
	for r in cursor.fetchall():
		print("Customer details :{} {} {} {}".format(r[0] ,r[1] ,r[2] ,r[3] ))	
	db.commit()
org()
root.mainloop()