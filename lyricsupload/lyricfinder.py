import time
import os
import os.path
time.sleep(8)

f = open('songtitle.txt', 'r', encoding="utf-8")

i = f.read()

file_name = i + '.txt'
cur_dir = 'lyricsdata'

while True:
    file_list = os.listdir(cur_dir)
    parent_dir = os.path.dirname(cur_dir)
    if file_name in file_list:
        f = open(r"C:\Users\Victoria Liu\Desktop\lyricsupload\lyricsdata" + "\\" + file_name, 'r', encoding="utf-8")
        readlyrics = f.read()
        print("Reading files")
        f= open('writelyrics.txt', 'w', encoding="utf-8")
        f.write(readlyrics)
        f.close()
        break
        
    else:
        f= open('writelyrics.txt', 'w', encoding="utf-8")
        f.write('Lyrics not found')
        f.close()
        break




