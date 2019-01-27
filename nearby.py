import requests
import json
import pyrebase
import webbrowser
class Nearby:
	def Place(string):
		config = {
		"apiKey": "AIzaSyAr_BoRAS-SxWZ4IMPaW_YfxiQB5MiGXO8",
		"authDomain": "hack36-app-module-2019-jan.firebaseapp.com",
		"databaseURL": "https://hack36-app-module-2019-jan.firebaseio.com/",
		"storageBucket": "hack36-app-module-2019-jan.appspot.com"
		}
		firebase = pyrebase.initialize_app(config)
		db = firebase.database()
		latitude= db.child("latitude").get();
		latitude=latitude.val();
		longitude=db.child("longitude").get();
		longitude=longitude.val();
		url="https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="+str(latitude)+","+str(longitude)+"&radius=2500&types="+string+"&sensor=true&key=AIzaSyBvN7-4PKDpvpcw-dkTd_6-B5WuptirDSw"
		results=requests.get(url).json();
		res=results["results"]
		string="";
		for result in res:
			#print(result["name"])
			#print(result["user_ratings_total"])
			#print(result["vicinity"])
			string="name:::"+result["name"]+"\n"+"Address::"+result["vicinity"]+"\n\n"+string;
		return string;