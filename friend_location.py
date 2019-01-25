import pyrebase
import webbrowser
import gmplot
class FriendLocation(object):
	def plot(string):
		config = {
		"apiKey": "AIzaSyAr_BoRAS-SxWZ4IMPaW_YfxiQB5MiGXO8",
		"authDomain": "hack36-app-module-2019-jan.firebaseapp.com",
		"databaseURL": "https://hack36-app-module-2019-jan.firebaseio.com/",
		"storageBucket": "hack36-app-module-2019-jan.appspot.com"
		}
		firebase = pyrebase.initialize_app(config)
		db = firebase.database()
		st="";
		url="";
		all_users = db.child("friends").get()
		for user in all_users.each():
			val=user.val()
			name=val['name']
			lati=val['latitude']
			longi=val['longitude']
			if name==string:
				return "https://www.google.com/maps/?q="+lati+","+longi
			st=st+name+"\n";
		return st;




