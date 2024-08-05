import time
import os
time.sleep(5)

f = open('lyricservice.txt', 'r', encoding="utf-8")

i = f.read()
convert_to_link = ('https://genius.com/search?q=' + i)

f = open('lyricservice.txt', 'w', encoding="utf-8")
f.write(convert_to_link)


