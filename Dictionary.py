import requests
import json
app_id='e8e3ad5a'
app_key='70110215650230effb99b7f1c3bf6156'
language = 'en'
word_id = 'Ace'
class Dictionary:
	def words(word):
		url='https://od-api.oxforddictionaries.com:443/api/v1/entries/en/'+word.lower()
		r=requests.get(url,headers={'app_id':app_id,'app_key':app_key})
		res=r.json()
		#print(res["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0])
		result=''
		for i in range(len(res["results"][0]["lexicalEntries"][0]["entries"][0]["senses"])):
			result=result+str(i+1)+'.'+res["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][i]["definitions"][0]+'\n'
		return result 