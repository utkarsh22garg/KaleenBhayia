import requests
import datetime
import os
class Meeting:
	def AddMeeting(st):
		f=open("meetings.txt", "a+")
		i=1
		day,month,year = st[0].split('/')
		hrs,mi=st[1].split(":")
		if (int(hrs)>12 or int(hrs)<0) or (int(mi)>=60 or int(mi)<0):
			f.close();
			return "time is invalid"
		if st[2].lower()!="am" and st[2].lower()!="pm":
			f.close();
			return "meridians should be am or pm"
		isValidDate = True
		try :
			datetime.datetime(int(year),int(month),int(day))
		except ValueError :
			isValidDate = False
		if isValidDate:
			try:
				#if os.stat("meetings.txt").st_size == 0:
				f.write("Meeting is on %s at %s%s for %s\n" %(st[0],st[1],st[2],st[3]))
				# else:
				# 	f.write("Meeting is on %s at %s%s for %s" %(st[0],st[1],st[2],st[3]))
				return "OK"
			except:
				f.close();
				return "Error in writing check proper fields:)"
		else:
			f.close();
			return "Date is not valid"
		f.close();
	def ShowMeeting():
		string=""
		f=open("meetings.txt",'r')
		for line in f.readlines():
			string+=line
		return string