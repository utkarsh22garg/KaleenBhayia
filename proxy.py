import requests
import urllib.request
import socket
from config import Config
import urllib.error
from bs4 import BeautifulSoup
class Proxy(object):
	def getProxyLists():
		proxyDict = { 
              "http"  : Config.getProxy()
            }
		page=requests.get("http://172.31.9.69/dc/proxy.php",proxies=proxyDict)
		if page.status_code == 200:
			soup=BeautifulSoup(page.content,'html.parser')
			texts=soup.find_all(class_="text-success")
			i=0
			lists=[]
			for text in texts:
				if i==0:
					i+=1
					continue
				ip=list(text.children)[0].getText()
				port=list(text.children)[1].getText()
				status=list(text.children)[2].getText()
				uptime=list(text.children)[3].getText()
				speed=list(text.children)[4].getText()
				tup=(ip,port,status,uptime,speed)
				lists.append(tup)
			return lists
		else :
			return "Either you are not connect to internet or you have to be in College network"
	def getProxyStatus():
		lists=Proxy.getProxyLists()
		string="";
		for lis in lists:
			string=(lis[0]+" "+lis[1]+" "+lis[2]+" "+lis[3]+" "+lis[4])+"\n\n"+string;
		return string
	def is_bad_proxy(pip):
		try:
			proxy_handler = urllib.request.ProxyHandler({'http': pip})
			opener = urllib.request.build_opener(proxy_handler)
			hdr = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),
       ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
       ('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'),
       ('Accept-Encoding','none'),
       ('Accept-Language', 'en-US,en;q=0.8'),
       ('Connection', 'keep-alive')]
			opener.addheaders = hdr
			urllib.request.install_opener(opener)
			req=urllib.request.Request('http://172.31.9.69/dc/proxy.php')
			sock=urllib.request.urlopen(req)
		except urllib.error.HTTPError as e:
			#print('Error code: ', e.code)
			return True
		except Exception as detail:
			#print("ERROR:", detail)
			return True
		return False
	def getWorkingProxy():
		socket.setdefaulttimeout(120)
		lists=Proxy.getProxyLists();
		answer="";
		for lis in lists:
			string="edcguest:edcguest@"+lis[0]+":"+lis[1];
			if lis[2]==" Working":
				if Proxy.is_bad_proxy(string)==False:
					answer=(lis[0]+" "+lis[1]+" "+lis[2]+" "+lis[3]+" "+lis[4])+"\n\n"+answer
		return answer
	def getHelpList():
		string="following are the proxy commands::\n"+" proxy :- It shows the proxies status that are available in MNNIT Campus\n\n"+" proxy working :- It shows the proxies that are only working in your area\n"
		return string;			
