import requests 
import random
class Cricket:
	def news(self):
		api = requests.get('https://newsapi.org/v2/top-headlines?sources=espn-cric-info&apiKey=4561cd79afb64b00a4fc51da79391d9d').json()
		res =''
		
		i=0
		j=i+10
		while i < j:
			res = res + str((i+1))+'. '+api["articles"][i]["title"] + '\n'
			i += 1
		#print(res)
		return res	

