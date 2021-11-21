import os
import random
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', 'spanish')



toronto = ['ton', 'to', 'toron']
msg = 'toronto'
none = None

def check(w):
	return w == 'mar'

cantidad = random.randint(90,100)
for n in range(cantidad):
	random.choice(toronto)
	msg += random.choice(toronto)

engine.save_to_file(msg, 'test.mp3')
engine.runAndWait()

print(msg)
