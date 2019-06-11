import speech_recognition as sr
import threading
from tkinter import *
def speak():
    global flag
    while(flag!=1):
        r = sr.Recognizer()
        with sr.Microphone() as source:                # use the default microphone as the audio source
            audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
        def aud(audio):
            if(audio=="hello"):
                print("bitch lasgigna")
                flag=1
        try:
            if(r.recognize_google(audio)=="hello"):
                print("bitch lasgigna")
            if(r.recognize_sphinx(audio)=="hello"):
                print("i am better")
        except:                           
            pass

flag=0
root=Tk()
threadObj=threading.Thread(target=speak)
threadObj.start()
mainloop()
