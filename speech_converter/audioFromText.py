from gtts import gTTS
import os

text = 'LOL this is really funny'
output = gTTS(text=text, lang='en',slow=False)
output.save('speech_converter\output.mp3')

os.system("start speech_converter\output.mp3")