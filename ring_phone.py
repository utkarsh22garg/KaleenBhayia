import pyrebase
class Database(object):
	def getCoordinate():
		config = {
		"apiKey": "AIzaSyAr_BoRAS-SxWZ4IMPaW_YfxiQB5MiGXO8",
		"authDomain": "hack36-app-module-2019-jan.firebaseapp.com",
		"databaseURL": "https://hack36-app-module-2019-jan.firebaseio.com/",
		"storageBucket": "hack36-app-module-2019-jan.appspot.com",
		"serviceAccount": "google-services.json"
		}
		firebase = pyrebase.initialize_app(config)
		db = firebase.database()
		latitude= db.child("latitude").get();
		longitude=db.child("longitude").get();
		print(latitude,longitude);



