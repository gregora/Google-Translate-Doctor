from googletrans import Translator
#from random import *
import random
translator = Translator()

lang = raw_input("Language: ")

while True:

    print("----------------------------------------------------------")

    inp = raw_input("Your question: ");
    print("Your Google Translate-Doctor will now answer your question")

    trstr = []
    sendstr = ""

    for c in inp:
        trstr.append(c)

    for x in range(0, len(trstr)/2):
        #if(x>0):
        sendstr = sendstr + trstr[2*x]
        sendstr = sendstr + trstr[2*x - 1] + " "
        '''
        if (random.randint(1, 8) == 4):
            sendstr += " "
        '''
    #print(sendstr)

    #if len(sendstr) < 24:
    sendstr = "qe " * 10 + sendstr

    print("\tThe Doctor replied: " + translator.translate(sendstr, src = "so", dest = lang).text)
