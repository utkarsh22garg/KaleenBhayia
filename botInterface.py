import speech_recognition as sr  
import zulip
import os

# print(os.getcwd())
# get audio from the microphone                                                                       

while True:
	r = sr.Recognizer()                                                                                   


	with sr.Microphone() as source:                                                                       
	    print("Speak:")                                                                                   
	    audio = r.listen(source)   

	try:
	    input_text=r.recognize_google(audio)
	except sr.UnknownValueError:
	    print("Could not understand audio")
	except sr.RequestError as e:
	    print("Could not request results; {0}".format(e))


	# Pass the path to your zuliprc file here.
	client = zulip.Client(config_file="./zuliprc")

	# Send a stream message
	request = {
	    "type": "stream",
	    "to": "general",
	    "subject": "general",
	    "content": "@**Kaleen_Bhayia** "+input_text
	}

	result = client.send_message(request)

	if result['result']!='error':
		request = {
		    'use_first_unread_anchor': True,
		    'num_before': 0,
		    'num_after': 1,
		    'narrow': [{'operator': 'sender', 'operand': 'Kaleen_Bhayia-bot@kaleenbhayiakeladke.zulipchat.com'},
		               {'operator': 'stream', 'operand': 'general'}],
		}  # type: Dict[str, Any]	
		result = client.get_messages(request)
		print(result)
	else:
		print('Error in sending the message to the bot!!')