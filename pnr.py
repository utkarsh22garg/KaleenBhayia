import requests
from bs4 import BeautifulSoup
from time import sleep

class Pnr:
	def getpnr(pnr):
		try:
		 
		 url = 'https://www.railyatri.in/pnr-status/' + str(pnr)
		 html = requests.get(url)
		 soup = BeautifulSoup(html.text, 'lxml')
		 trainDetails = soup.findAll(class_="pnr-search-result-info")
		 chartStatus = soup.findAll(class_="chart-stats")
		 
		 
		 string=""
		 b1=""
		 b2=""
		 for text in trainDetails:
		 	b1=(text.getText());
		 	b1=b1.lstrip();
		 
		 b1=b1.replace('\n\n','\n')
		 #print(b1)
		 i=0;
		 for text in chartStatus:
		 	b2=(text.getText());
		 	b2=b2.lstrip();
		 	b2=b2.rstrip()
		 	

		 b2=b2.replace('\n\n','\n')
		 

		 try:
		  if b1 == "":
		  	string = "Invalid PNR. Try again!"
		  else:	
		    string ='Train Details: ' + b1  + 'Booking Status: ' + b2
		    string=string[:string.rfind('\n\n')]
		    string+="  is the Current Status"
		 	 
		 except:
		  print("Invalid PNR. Try again!")
		  

		 return string
		except requests.exceptions.ConnectionError:
		 print("Connection Error. Try again!")
