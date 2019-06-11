import gtts
import pygame
from tkinter import *

# This module is imported so that we can  
# play the converted audio 
import os 
print('1')
# The text that you want to convert to audio 
mytext = 'Hey! Its Youtube.'
print("2") 
# Language in which you want to convert 
language = 'en'
print('3')  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 
myobj = gtts.gTTS(text=mytext, lang=language, slow=False) 
print('4')
# Saving the converted audio in a mp3 file named 
# welcome  
myobj.save("yt.mp3") 
root=Tk()
root.geometry("500x200")
file = 'yt.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
mainloop()
