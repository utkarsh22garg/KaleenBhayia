import requests;
import json
import pyrebase
import time
from send_message import Send_message
class Help(object):
	def Message():
		config = {
		"apiKey": "AIzaSyAr_BoRAS-SxWZ4IMPaW_YfxiQB5MiGXO8",
		"authDomain": "hack36-app-module-2019-jan.firebaseapp.com",
		"databaseURL": "https://hack36-app-module-2019-jan.firebaseio.com/",
		"storageBucket": "hack36-app-module-2019-jan.appspot.com"
		}
		firebase = pyrebase.initialize_app(config)
		db = firebase.database()
		no1=db.child("person1").get();
		no1=no1.val();
		no2=db.child("person2").get();
		no2=no2.val();
		no3=db.child("person3").get();
		no3=no3.val();
		print(no1,no2,no3);
		latitude= db.child("latitude").get();
		latitude=latitude.val();
		longitude=db.child("longitude").get();
		longitude=longitude.val();
		string=str("https://www.google.com/maps/?q="+latitude+","+longitude)
		string="I am in Trouble please help me reach here ASAP"+"\n"+string
		lis1=["message",str(no1),"now",string]
		lis3=["message",str(no3),"now",string]
		lis2=["message",str(no2),"now",string]
		Send_message.sendMessage(lis3);
		time.sleep(10)
		Send_message.sendMessage(lis2);
		time.sleep(10);
		Send_message.sendMessage(lis1);



