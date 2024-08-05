import time
import os
from tkinter import *
import webbrowser


print("Please enter the song title you want to find (lowercase with no spaces):")
answer = input()

f = open('songtitle.txt', 'w', encoding="utf-8")
f.write(answer)
f.close()

print ("Please wait...")
time.sleep(1)

for i in range (10):
    print (".")
    time.sleep(1)

f = open('writelyrics.txt', 'r', encoding="utf-8")
lyrics = f.read()
print(lyrics)