import time
import os
from tkinter import *
import webbrowser
import subprocess


print("Please enter the song title you want the lyrics to:    ")
answer = input()


f = open('lyricservice.txt', 'w', encoding="utf-8")
f.write(answer)
f.close()


print ("Please wait...")
time.sleep(1)

for i in range (5):
    print (".")
    time.sleep(1)

f = open('lyricservice.txt', 'r', encoding="utf-8")
lyriclink = f.read()
f.close()


print (lyriclink) 

window = Tk()

def onClick():
    webbrowser.open(lyriclink) # Opening the URL

button = Button(window, text="Click me!", command=onClick) # Assigning button and adding the click event.
button.pack()

window.mainloop()