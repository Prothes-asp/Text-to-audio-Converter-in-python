"""
Firstly Import Modiul.................................
gtts Modiul means-----> Google Text To Speach
gTTS Modiul means-----> Text To Speach Conversion...
Then import...........................................
os   Modiul means-----> to start the Audio file
"""
# Text To Audio Converter......Projects
from gtts import gTTS
import os
fh = open("Some Text.txt","r")
myText = fh.read().replace("\n"," ")
language = "en"
output = gTTS(text = myText,lang = language,slow = False)
output.save("output.mp3")
fh.close()
os.system("start output.mp3")