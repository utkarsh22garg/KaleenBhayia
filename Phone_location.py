import pyrebase
import webbrowser
class Database(object):
	def getCoordinate():
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
		print(latitude,longitude);
		webbrowser.open("https://www.google.com/maps/?q="+latitude+","+longitude);
		return "https://www.google.com/maps/?q="+latitude+","+longitude;