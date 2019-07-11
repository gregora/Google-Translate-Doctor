from googletrans import Translator
#from random import *
import random
from gtts import gTTS
import vlc
import tkinter as tk


def translate():
    global doctorAnswer, inp, e1
    original = inp.get()
    trstr = []
    sendstr = ""

    for c in original:
        trstr.append(c)

    for x in range(0, len(trstr)//2):
        #if(x>0):
        sendstr = sendstr + trstr[2*x]
        sendstr = sendstr + trstr[2*x - 1] + " "
        '''
        if (random.randint(1, 8) == 4):
            sendstr += " "
        '''


    #if len(sendstr) < 24:
    sendstr = "qe " * 10 + sendstr
    print(sendstr)
    endStr = translator.translate(sendstr, src = "so", dest = "en").text
    print(doctorAnswer)
    tts = gTTS(endStr, lang='en')
    tts.save('answer.mp3')
    player = vlc.MediaPlayer("answer.mp3")
    player.play()
    doctorAnswer.config(text = "Doctor answered:" + endStr)
    doctorAnswer.grid(column = 0, row = 3)



translator = Translator()
root = tk.Tk()
root.title("Doctor Google Translate")
tts = gTTS('Hello patient!', lang='en')
tts.save('hello.mp3')
player = vlc.MediaPlayer("hello.mp3")
player.play()

'''
w = tk.Label(root, text="Hello patient!").grid(row = 0)
languageText = tk.Label(root, text = "Language:").grid(column = 0, row = 1)

e1 = tk.Entry(root)
e1.insert(10, "sl")
e1.grid(column = 1, row = 1)
lang = e1
'''

questionText = tk.Label(root, text = "Your question:").grid(column = 0, row = 2)
inp = tk.Entry(root);
inp.grid(column = 1, row = 2)
doctorAnswer = tk.Label(root, text = "Doctor answered:")
doctorAnswer.grid(column = 0, row = 3)
b1 = tk.Button(root, text='Show', command=translate)
b1.grid(column = 2, row = 2)
root.mainloop()
print("Your Google Translate-Doctor will now answer your question")
