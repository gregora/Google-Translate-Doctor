from googletrans import Translator
import random
from gtts import gTTS
import vlc
import Tkinter as tk
#import tkinter as tk !!(for python 3)!!!



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

        if (random.randint(1, 8) == 4):
            sendstr += " qe "



    #sendstr = "qm " * 10 + sendstr
    print("Sending string "+sendstr)

    #detecting sendstr language (for better translation)
    detected_language = str(translator.detect(sendstr));
    #cut off unnecessary info
    detected_language = detected_language[14:18]
    if(detected_language[2]==","):
        detected_language = detected_language[0:2]
    elif(detected_language[3]==","):
        detected_language = detected_language[0:3]

    print("Detected language: " + detected_language)

    endStr = translator.translate(sendstr, src = detected_language, dest = "en").text
    print("Answer: "+endStr)
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
