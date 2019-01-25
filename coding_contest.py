import requests
import json
import datetime
apikey="58d312690dfea3caadc60c0bb6f727347a9165a5"
class Coding(object):
	def getList(self):
		d=datetime.date.today()
		month='{:02d}'.format(d.month)
		results=requests.get('https://clist.by/api/v1/contest/?format=json&username=Aniket468&api_key=58d312690dfea3caadc60c0bb6f727347a9165a5&end__year=2019&'+'end_month'+month).json();
		string="";
		#print(results)
		i=0;
		for i in range(0,15):
			string+=str(i)+". "+results["objects"][i]["event"]+"\n"+"startTime:-> "+results["objects"][i]["start"]+" ::: "+" endTime:-> "+results["objects"][i]["end"]+"\n"+results["objects"][i]["href"]+"\n"
			string+="\n\n"
		return string