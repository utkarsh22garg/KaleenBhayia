# Send to single device.
# 
from pyfcm import FCMNotification
from Phone_location import Database
class Send_message(object):
	def sendMessage(string):
		push_service = FCMNotification(api_key="AAAAJdSzXcA:APA91bGiskJQAk2g4MwIfhJ0n34pnklye5K-mMBn5s0P8wNr3N1nlOnrVkwlCttICVg1csuHO8defLcKIsy0v-x2kVgOdrB4nnGqcGE8HAlu46BWastj9NGA7mIXtALPAVxiBgHTm-vp")
		proxy_dict = {
          "http"  : "http://edcguest:edcguest@172.31.102.14:3128",
          "https" : "http://edcguest:edcguest@172.31.102.14:3128",
          }
		l=string[3:]
		s=" ";
		s=s.join(l);
		data_message={
		"type":string[0],
		"no" : string[1],
		"message" : s,
		"time" : string[2]
		}
		push_service = FCMNotification(api_key="AAAAJdSzXcA:APA91bGiskJQAk2g4MwIfhJ0n34pnklye5K-mMBn5s0P8wNr3N1nlOnrVkwlCttICVg1csuHO8defLcKIsy0v-x2kVgOdrB4nnGqcGE8HAlu46BWastj9NGA7mIXtALPAVxiBgHTm-vp", proxy_dict=proxy_dict)
		registration_id = "fgBmBG6S3i4:APA91bGYmCvOpOLVpPOlY8hHShWNUg5CX8JcgfN9WHfuh76pGKYkSoHXEsliq93W3qE4sL70nO6RA8nrLjjHRpMq3WotBy3NUezjmJZX1w8c_0AKOa-nlZ67fYCsFi9FFkXDvvzUIT8T"
		message_title = "someone_seaching"
		message_body = "searching..."
		result = push_service.notify_single_device(registration_id=registration_id, message_body=message_body,data_message=data_message)
		val=""
		if string[0]=="message": 
			val="message sent successfully"
		elif string[0]=="find":
			val="Your phone will be ringing in a while"
		elif string[0]=="where":
			#val ="tracking your phone wait a while"
			val=Database.getCoordinate();
			val="Checkout the link \n"+str(val);
		return val	
		#print(result)
