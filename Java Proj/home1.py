from tkinter import *


root = Tk()
root.geometry("2000x2000")
root.title("Project: Career Guiance")

frame=Frame(root,height=1900,width=2000)
frame0=Frame(root,height=2000,width=2000)
frame1=Frame(root,height=1900,width=2000,background="#F3EAE7")
frame2=Frame(root,height=1000,width=2000, background="#C0CFD5" )



b1 = Button(frame0,text='Engineering',fg="white",bg="red",font = "Helvetica 35 bold",relief="raised", command= lambda:voice())

def org():
    
    frame0=Frame(root,height=2000,width=2000).place(x=0,y=0)
    bg = Label(frame0, bg="grey").pack()
    
    l1=Label(frame0,text="Career Guidance For Science Students",fg="#0BB0F6",font=("Arial",50,"bold")).place(x=30,y=30)
    l2=Label(frame0, text="Which field are you more interested in?",fg="#0BB0F6", font=("times new roman",20,"bold")).place(x=450,y=200)
    l3=Label(frame0, text="Confused? Take a quiz?",fg="#0BB0F6", font=("times new roman",20,"bold")).place(x=530,y=450)

    b1 = Button(frame0,text='Engineering',fg="white",bg="red",font = "Helvetica 35 bold",relief="raised", command=play).place(x=300,y=300)
    b2 = Button(frame0,text='Pure Sciences',fg="white",bg="purple",font = "Helvetica 35 bold",relief="raised",command=org1).place(x=700,y=300)
    b3 = Button(frame0,text='Take a Quiz',fg="white",bg="#FFCD01",font = "Helvetica 35 bold",relief="raised",command=quiz1).place(x=520,y=500)
    b4 = Button(frame0, text= " Quit ", fg="Black", font = "Helvetica 20", relief="raised",command=quit).place(x=1200,y=600)
    
def org1():
    frameA=Frame(root,height=2000,width=2000).place(x=0,y=0)
    bg = Label(frame1, bg="grey").pack()
    
    l1=Label(frameA,text="Select the branch of pure science.",fg="#0BB0F6",font=("Arial",50,"bold")).place(x=200,y=30)
        
    b81 = Button(frameA,text='Physics',fg="white",bg="red",font = "Helvetica 35 bold",relief="raised",command=physics).place(x=300,y=300)
    b82 = Button(frameA,text='Maths',fg="white",bg="purple",font = "Helvetica 35 bold",relief="raised",command=maths).place(x=1000,y=300)
    b83 = Button(frameA,text='Chemistry',fg="white",bg="#FFCD01",font = "Helvetica 35 bold",relief="raised",command=chemistry).place(x=300,y=600)
    b84 = Button(frameA,text='Biology',fg="white",bg="green",font="Helvetica 35 bold",relief="raised",command=biology).place(x=1000,y=600)
    b97 = Button(frameA, text= "Back", fg="Black", font = "Helvetica 20", relief="raised",command=org).place(x=1400,y=700)
def physics():
    #physics page
    frameA = Frame(root,height=10000,width=2000).place(x=0,y=100)
      
    l81=Label(frameA,text="Geophysicst",fg="#0BB0F6",font=("Helvetica",30,"bold")).place(x=600,y=250)
    l83=Label(frameA,text=" A geophysicist is someone who studies the Earth using gravity, magnetic, electrical, and \n seismic methods. Some geophysicists spend most of their time outdoors studying various \n features of the Earth, and others spend most of their time indoors using computers for \n modeling and calculations.",fg="black",font=("Helvetica",20,), justify="left").place(x=190,y=350)

    l84=Label(frameA,text=" Salary:",fg="black",font=("Helvetica",20,"bold")).place(x=190,y=510)
    l85=Label(frameA,text=" Approx.  Rs 660,000 per year.",fg="black",font=("Helvetica",20,)).place(x=190,y=550)

    b90 = Button(frameA, text= "Back", fg="Black", font = "Helvetica 20", relief="raised",command=org1).place(x=1200,y=600)

def maths():
    #maths page
    
    frameA = Frame(root,height=10000,width=2000).place(x=0,y=100)

    l41=Label(frameA,text="Statistician",fg="#0BB0F6",font=("Helvetica",30,"bold")).place(x=600,y=250)
    l42=Label(frameA,text=" A statistician is a person who works with theoretical or applied statistics. \n The profession exists in both the private and public sectors. \n It is common to combine statistical knowledge with expertise in other subjects, \n and statisticians may work as employees or as statistical consultants.",fg="black",font=("Helvetica",20,), justify="left").place(x=250,y=350)


    l43=Label(frameA,text=" Salary:",fg="black",font=("Helvetica",20,"bold")).place(x=250,y=510)
    l45=Label(frameA,text=" Statisticians made a median salary of $84,060 in 2017.",fg="black",font=("Helvetica",20,)).place(x=250,y=550)

    b91 = Button(frameA, text= "Back", fg="Black", font = "Helvetica 20", relief="raised",command=org1).place(x=1200,y=600)
def chemistry():
    #chemistry page
    frameA = Frame(root,height=10000,width=2000).place(x=0,y=100)

    l54=Label(frameA, text="Chemistry",fg="#0BB0F6",font=("Helvetica",30,"bold")).place(x=600,y=200)

    l55=Label(frameA, text="Your options are:",fg="black",font=("Helvetica",25,"bold")).place(x=560,y=300)

    l56=Label(frameA, text="1.Clinical Biochemistry\n2.Foresic Scientist\n3.Pharmacologist\n4.Toxiologist\n5.Chemical Engineer\n6.Analytical Chemist",fg="black",font=("Arial",20),justify="left").place(x=530,y=400)
    b92=   Button(frameA, text= "Back", fg="Black", font = "Helvetica 20", relief="raised",command=org1).place(x=1200,y=600) 


def biology():
    #biology page
    frameA = Frame(root,height=10000,width=2000).place(x=0,y=100)

    l57=Label(frameA, text="Biology",fg="#0BB0F6",font=("Helvetica",30,"bold")).place(x=650,y=200)

    l58=Label(frameA, text="Your options are:",fg="black",font=("Helvetica",25,"bold")).place(x=600,y=300)

    l59=Label(frameA, text="1.Soil Scientist\n2.Research Scientist (Life Sciences)\n3.Nature Conservation Officer\n4.Microbiologist",fg="black",font=("Arial",20), justify="left").place(x=530,y=400)

    b93= Button(frameA, text= "Back", fg="Black", font = "Helvetica 20", relief="raised",command=org1).place(x=1200,y=600)    
        

def play():
    #Engineering page
    frame=Frame(root,height=2000,width=2000).place(x=0,y=100)
    l4=Label(frame, text = "Choose a course to know more about it",fg="#0BB0F6", font=("times new roman",20,"bold")).place(x=450,y=130)

    b5 = Button(frame, text= "Back", fg="Black", font = "Helvetica 20", relief="raised",command=org).place(x=1200,y=600)
    b6 = Button(frame,text='Computer Science/Computer Engineering',fg="white",bg="purple",font = "Verdana 20",relief="raised",command=comp).place(x=400,y=170)
    b7 = Button(frame,text='Information Technology',fg="white",bg="#114762",font = "Verdana 20",relief="raised",command=it).place(x=510,y=230)
    b8 = Button(frame,text='Electronics and Telecommunication',fg="white",bg="red",font = "Verdana 20",relief="raised",command=extc).place(x=440,y=290)
    b9 = Button(frame,text='Civil Engineering',fg="white",bg="#FFEF00",font = "Verdana 20",relief="raised",command=civ).place(x=545,y=350)
    b10 = Button(frame,text='Chemical Engineering',fg="white",bg="#00E6FF",font = "Verdana 20",relief="raised",command=chem).place(x=510,y=410)
    b11 = Button(frame,text='Biomedical Engineering',fg="white",bg="#FF0091",font = "Verdana 20",relief="raised",command=biomed).place(x=500,y=470)
    b12 = Button(frame,text='Explore More Options',fg="#0BB0F6",font = "Helvetica 20 bold").place(x=520,y=580)

def it():
    #IT page
    frame1 = Frame(root,height=10000,width=2000).place(x=0,y=100)

    b13 = Button(frame1, text= "Back", fg="Black", font = "Helvetica 20", relief="raised",command=play).place(x=1200,y=600)

    l5= Label(frame1, text = "Information Technology",fg="#0BB0F6", font=("Helvetica",30,"bold")).place(x=450,y=120)
    l6 =  Label(frame1, text = "Curriculum:",fg="black", font=("Helvetica",20,"bold")).place(x=10,y=200)
    l7 = Label(frame1, text = "The curriculum for Information Technology Engineering is primarily designed to provide\n students with both the theoretical knowledge and technical skills. The curriculum also\n intends to improve a technological depth of knowledge and skills in analysis, design,\n implementation, and use of both information technology core skills and specialization skills. ",fg="black", font=("Arial",20), anchor='w').place(x=190,y=200)
    l8 = Label(frame1, text="Job Profile:",fg="black", font=("Helvetica",20,"bold")).place(x=10,y=350)
    l9 = Label(frame1, text="They design, develop, research and test software and digital\n hardware, digital devices and interfaces. So, various organizations are becoming more oriented\n to recruit IT engineers with a view to operate computer systems, software, servers,\n computer networking or network security.",fg="black", font=("Arial",20), anchor='w').place(x=190,y=350)
    l10 = Label(frame1, text="Salary:",fg="black", font=("Helvetica",20,"bold")).place(x=10,y=525)
    l11 = Label(frame1, text="$52000 to $59000 per annum",fg="black", font=("Arial",20), anchor='w').place(x=190,y=525)

def comp():
    #Comp page
    frameC=Frame(root,height=1900,width=2000).place(x=0,y=100)

    lA=Label(frameC,text="COMPUTER ENGINEERING",fg="#0BB0F6",font=("Helvetica",30,"bold")).place(x=440,y=120)
    lB=Label(frameC,text="Curriculum:",fg="black",font=("Helvetica",20,"bold")).place(x=30,y=250)
    lC=Label(frameC,text="Computer engineering is a branch of engineering that integrates several fields of computer\n science and electronics engineering required to develop computer hardware and software.\n Computer engineers usually have training in electronic engineering (or electrical engineering),\n software design, and hardware–software integration instead of only software engineering or\n electronic engineering.",fg="black",font=("Helvetica",20,)).place(x=190,y=250)
    lD=Label(frameC,text="Job Profile:",fg="black",font=("Helvetica",20,"bold")).place(x=30,y=410)
    lE=Label(frameC,text="As a computer engineer, you're responsible for researching, designing, developing and\n testing computer hardware and equipment, including chips, analog sensors, circuit boards,\n keyboards, modems, routers and printers. You may work on the manufacturing\n of these components, as well as the installation.",fg="black",font=("Helvetica",20,)).place(x=190,y=410)
    lF=Label(frameC,text="Salary:",fg="black",font=("Helvetica",20,"bold")).place(x=30,y=550)
    lG=Label(frameC,text="Approx. $110,650 per annum",fg="black",font=("Helvetica",20,)).place(x=150,y=550)
    
    b13 = Button(frameC, text="Back",fg="Black", font="Helvetica 20", relief="raised", command=play).place(x=1200,y=600)

def civ():
    #Civil Engg
    frame2 = Frame(root,height=10000,width=2000).place(x=0,y=100)

    b13 = Button(frame2, text= "Back", fg="Black", font = "Helvetica 20", relief="raised",command=play).place(x=1200,y=600)

    l12= Label(frame2, text = "Civil Engineering",fg="#0BB0F6", font=("Helvetica",30,"bold")).place(x=450,y=120)
    l13 =  Label(frame2, text = "Curriculum:",fg="black", font=("Helvetica",20,"bold")).place(x=10,y=200)
    l14 = Label(frame2, text = "With the background acquired in the junior year, students are equipped\n to take design classes and to engage in the professional practice/capstone design sequence.\n Required classes also include foundation design and transportation. For the \nrest of the senior year, technical elective courses are available.",fg="black", font=("Arial",20), anchor='w').place(x=190,y=200)
    l15 = Label(frame2, text="Job Profile:",fg="black", font=("Helvetica",20,"bold")).place(x=10,y=350)
    l16 = Label(frame2, text="Civil engineers design, construct, supervise, operate, and maintain large \nconstruction projects and systems, including roads, buildings, airports, tunnels, dams,\n bridges, and systems for water supply and sewage treatment. Many\n civil engineers work in design, construction, research, and education.",fg="black", font=("Arial",20), anchor='w').place(x=190,y=350)
    l17 = Label(frame2, text="Salary:",fg="black", font=("Helvetica",20,"bold")).place(x=10,y=525)
    l18 = Label(frame2, text="$50000 to $65000 per annum",fg="black", font=("Arial",20), anchor='w').place(x=190,y=525)

def extc():
    #EXTC Page
    frameB = Frame(root,height=10000,width=2000).place(x=0,y=100)

    b13 = Button(frameB, text= "Back", fg="Black", font = "Helvetica 20", relief="raised",command=play).place(x=1200,y=600)

    lH=Label(frameB, text="ELECTRONICS & TELECOMMUNICATION ENGINEERING",fg="#0BB0F6", font=("Helvetica",30,"bold")).place(x=200,y=120)
    lI=Label(frameB, text="Curriculum:",fg="black", font=("Helvetica",20,"bold")).place(x=10,y=200)
    lJ=Label(frameB, text="Telecommunications engineering, or telecom engineering, is an engineering discipline that\n integrates electrical engineering with computer science to develop telecommunication systems.\n A Telecom equipment engineer is an electronics engineer that designs equipment such\n as routers, switches, multiplexers and other splecialized computer / electronics\n equipment designed to be used in the telecommunication network infrastructure",fg="black", font=("Arial",20), anchor='w').place(x=190,y=200)
    lK=Label(frameB, text="Job Profile:", font=("Helvetica",20,"bold")).place(x=10,y=375)
    lL=Label(frameB, text="As an electronics engineer you'll design, develop and test components, devices,\n systems or equipment that use electricity as part of their source of power.\n These components include capacitors, diodes, resistors and transistors",fg="black", font=("Arial",20), anchor='w').place(x=190,y=375)
    lM=Label(frameB, text="Salary:",fg="black", font=("Helvetica",20,"bold")).place(x=10,y=525)
    lN=Label(frameB, text="$5620 to $7024 per annum",fg="black", font=("Arial",20), anchor='w').place(x=190,y=525)



def chem():
    #chemical Engg
    frame3 = Frame(root,height=10000,width=2000).place(x=0,y=100)

    b14 = Button(frame3, text= "Back", fg="Black", font = "Helvetica 20", relief="raised",command=play).place(x=1200,y=600)

    l19= Label(frame3, text = "Chemical Engineering",fg="#0BB0F6", font=("Helvetica",30,"bold")).place(x=450,y=120)
    l20 =  Label(frame3, text = "Curriculum:",fg="black", font=("Helvetica",20,"bold")).place(x=10,y=200)
    l21 = Label(frame3, text = "Chemical engineering is all about changing raw materials into useful products such as\n clothes, food and drink, and energy. Chemical engineers focus on processes and\n products – they develop and design processes to create\n products; either focussing on improving existing processes or creating new ones.",fg="black", font=("Arial",20), anchor='w').place(x=190,y=200)
    l22 = Label(frame3, text="Job Profile:",fg="black", font=("Helvetica",20,"bold")).place(x=10,y=350)
    l23 = Label(frame3, text="Chemical engineers develop and design chemical manufacturing processes. Chemical\n engineers apply the principles of chemistry, biology, physics, and math\n to solve problems that involve the production or use of chemicals, fuel, drugs,\n food, and many other products.",fg="black", font=("Arial",20), anchor='w').place(x=190,y=350)
    l24 = Label(frame3, text="Salary:",fg="black", font=("Helvetica",20,"bold")).place(x=10,y=525)
    l25 = Label(frame3, text="$60,770 per annum",fg="black", font=("Arial",20), anchor='w').place(x=190,y=525)

def biomed():
    #Biomedical Engg
    frame4 = Frame(root,height=10000,width=2000).place(x=0,y=100)

    b14 = Button(frame4, text= "Back", fg="Black", font = "Helvetica 20", relief="raised",command=play).place(x=1200,y=600)

    l26= Label(frame4, text = "Biomedical Engineering",fg="#0BB0F6", font=("Helvetica",30,"bold")).place(x=450,y=120)
    l27 =  Label(frame4, text = "Curriculum:",fg="black", font=("Helvetica",20,"bold")).place(x=10,y=200)
    l28 = Label(frame4, text = "Biomedical Engineering, also referred to as Bioengineering, BioMed\n or BME, is a multidisciplinary STEM field that combines biology and engineering,\n applying engineering principles and materials to medicine and healthcare.",fg="black", font=("Arial",20), anchor='w').place(x=190,y=200)
    l29 = Label(frame4, text="Job Profile:",fg="black", font=("Helvetica",20,"bold")).place(x=10,y=350)
    l30 = Label(frame4, text="Design biomedical equipment and devices, such as artificial internal\n organs, replacements for body parts, and machines for diagnosing medical problems.\n Install, adjust, maintain, repair, or provide technical support for biomedical equipment.",fg="black", font=("Arial",20), anchor='w').place(x=190,y=350)
    l31 = Label(frame4, text="Salary:",fg="black", font=("Helvetica",20,"bold")).place(x=10,y=525)
    l32 = Label(frame4, text="$80,751 per annum",fg="black", font=("Arial",20), anchor='w').place(x=190,y=525)









def quiz1():
    #Quiz1
	eng=0
	app=0
	frameE=Frame(root,height=2000,width=2000).place(x=0,y=0)
	bg = Label(frameE, bg="grey").pack()
    
	l65=Label(frameE,text="1. Do you want to study about the \n practical application of Sciences.",fg="#0BB0F6",font=("Arial",50,"bold")).place(x=200,y=30)
            
	b81 = Button(frameE,text='A. YES',fg="white",bg="red",font = "Helvetica 35 bold",relief="raised",command=click1).place(x=300,y=400)
	b82 = Button(frameE,text='B. NO',fg="white",bg="purple",font = "Helvetica 35 bold",relief="raised",command=click2).place(x=1000,y=400)
    
	b83 = Button(frameE, text= "Next", fg="Black", font = "Helvetica 20", relief="raised",command=quiz2).place(x=1000,y=550)

def quiz2():
#Quiz2
    
    frameF=Frame(root,height=2000,width=2000).place(x=0,y=0)
    bg = Label(frameF, bg="grey").pack()
    
    l66=Label(frameF,text="2. Are you willing to study uptil \n you get you Ph.D degree?",fg="#0BB0F6",font=("Arial",50,"bold")).place(x=200,y=30)
        
    b84 = Button(frameF,text='A. YES',fg="white",bg="red",font = "Helvetica 35 bold",relief="raised",command=click3).place(x=300,y=400)
    b85 = Button(frameF,text='B. NO',fg="white",bg="purple",font = "Helvetica 35 bold",relief="raised",command=click4).place(x=1000,y=400)
    
    b86 = Button(frameF, text= "Next", fg="Black", font = "Helvetica 20", relief="raised",command=quiz3).place(x=1000,y=550)

def quiz3():
    #Quiz3

    frameG=Frame(root,height=2000,width=2000).place(x=0,y=0)
    bg = Label(frameG, bg="grey").pack()
    
    l67=Label(frameG,text="3. Are you interested in \n developing new theories?",fg="#0BB0F6",font=("Arial",50,"bold")).place(x=150,y=30)
         
    b87 = Button(frameG,text='A. YES',fg="white",bg="red",font = "Helvetica 35 bold",relief="raised",command=click5).place(x=300,y=400)
    b88 = Button(frameG,text='B. NO',fg="white",bg="purple",font = "Helvetica 35 bold",relief="raised",command=click6).place(x=1000,y=400)
    
    b89 = Button(frameG, text= "Next", fg="Black", font = "Helvetica 20", relief="raised",command=quiz4).place(x=1000,y=700)

def quiz4():
    
    frameH=Frame(root,height=2000,width=2000).place(x=0,y=0)
    bg = Label(frameH, bg="grey").pack()
    
    l68=Label(frameH,text="4. Are you interested in learning skills \n based upon problem solving.",fg="#0BB0F6",font=("Arial",50,"bold")).place(x=150,y=30)
        
    b99 = Button(frameH,text='A. YES',fg="white",bg="red",font = "Helvetica 35 bold",relief="raised",command=click8).place(x=300,y=400)
    b98 = Button(frameH,text='B. NO',fg="white",bg="purple",font = "Helvetica 35 bold",relief="raised",command=click7).place(x=1000,y=400)
    
    b96 = Button(frameH, text= "Next", fg="Black", font = "Helvetica 20", relief="raised",command=result).place(x=1000,y=700)


	




def click1():
	global eng
	eng=eng+1
	print(eng)
	return quiz2()
    
def click2():
	global app
	app=app+1
	print(app)
	return quiz2()

def click4():
	global eng
	eng=eng+1
	print(eng)
	return quiz3()
    
def click3():
	global app
	app=app+1
	print(app)
	return quiz3()


def click6():
	eng=eng+1
	print(eng)
	return quiz4()
    
def click5():
	app=app+1
	print(app)
	return quiz4()


def click7():
	eng=eng+1
	print(eng)
	return result()
    
def click8():
    
    app=app+1
    return result()








def result():
    
    frameI=Frame(root,height=2000,width=2000).place(x=0,y=0)
    bg = Label(frameI, bg="grey").pack()
    
    l45=Label(frameI,text="The Course You Should Choose is:",fg="#0BB0F6",font=("Arial",50,"bold")).place(x=200,y=30)
    eng=engg.get()
    app=applied.get()    
    if eng==app:
        l121=Label(frameI,text="Engineering",fg="#0BB0F6",font=("Arial",50,"bold")).place(x=400,y=200)
    else:
        l122=Label(frameI,text="Pure Sciences",fg="#0BB0F6",font=("Arial",50,"bold")).place(x=600,y=200)
    
    b45 = Button(frameI, text= "Next", fg="Black", font = "Helvetica 20", relief="raised",command=org).place(x=1000,y=700)
    b46 = Button(frameI, text= "Back", fg="Black", font = "Helvetica 20", relief="raised",command=quiz1).place(x=1000,y=700)

    





org()
root.mainloop()