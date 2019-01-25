import pprint
import requests
from gtts import gTTS
import os
class Joke():
    def tellJoke():
    	result="amazonaws"
    	joke=requests.get('https://official-joke-api.appspot.com/random_joke').json()
    	#print(joke["setup"])
    	#print(joke["punchline"])
    	string=joke["setup"]+'\n'+"answer"+joke["punchline"]
    	result='**'+joke["setup"]+'**'+'\n'+'Answer : '+ joke["punchline"]
    	tts=gTTS(text=string,lang='en')
    	tts.save("audio.mp3")
    	os.system('mpg321 audio.mp3 -quiet')
    	os.remove("audio.mp3")
    	return result
