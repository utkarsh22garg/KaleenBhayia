import requests
import urllib.request
import socket
from config import Config
import urllib.error
from bs4 import BeautifulSoup
from config import Config
class Dean(object):
	def getNotice():
		proxyDict = { 
              "http"  : Config.getProxy()
            }
		requests.packages.urllib3.disable_warnings()
		page=requests.get("https://academics.mnnit.ac.in/",proxies=proxyDict,verify=False)
		if page.status_code == 200:
			soup=BeautifulSoup(page.content,'html.parser')
			texts=soup.find_all(class_="lefttxtblank")
			text2=soup.find_all(class_="leftnormaltxt")
			#print(texts)
			string="";
			url=""
			i=0;
			for text in texts:
				ani=""
				b1=(text.getText());
				b1=b1.rstrip('\n')
				b2=(text2[i].getText());
				b2=	b2.rstrip('\n')
				A=text2[i].find_all('a')
				for a in A:
					if "href" in str(a):	
						url=a['href'];
						if "https" not in url :
							url="https://academics.mnnit.ac.in"+url[1:];
							ani=ani+url+"\n"	
				string=string+str(i)+". "+b1+"\n"+b2+"\n"+ani
				url="";
				ani=""
				i+=1
		else :
			return "something went wrong "+"\n"+"network status_code "+str(page.status_code)
		return string;