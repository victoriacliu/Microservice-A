**Clear instructions for how to programmatically REQUEST data from the microservice you implemented. **

**For the web-based search version:**
The program will request data from the user as an input in the ui.py file. Then, it will wait for the lyricservice.py file to do work and then again request the data through lyricservice.txt to display in a button.

**For the local file version:**
The program will request data from the user as an input in the ui.py file. Then it will request data from the writelyric.txt file to print the lyrics

**Clear instructions for how to programmatically RECEIVE data from the microservice you implemented.**

**For the web-based search version:**
The program will recieve data from the user and then send it to the lyricservice.txt file. It will the recieve data from the lyricserivce.txt file with the link to the lyric site.

**For the local file version:**
The program will recieve data from the user and then send it to the song title file. From there, lyricfinder.py will recieve that data and find the .txt file with the lyrics to writelyrics.txt. The program then recieves the lyric data and prints it for the user.

**UML sequence diagram showing how requesting and receiving data works. Make it detailed enough that your teammate (and your grader) will understand.**

https://github.com/victoriacliu/Microsesrvice-A/blob/main/uml/filemanual%20UML.jpeg
