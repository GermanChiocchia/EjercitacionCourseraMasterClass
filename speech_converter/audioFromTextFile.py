from gtts import gTTS
import os

text = open('speech_converter\demo.txt','r').read()
language = 'es'
output = gTTS(text=text, lang=language, slow=False)
output.save('speech_converter\outputfile.mp3')

os.system('start speech_converter\outputfile.mp3')