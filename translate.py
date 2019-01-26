from googletrans import Translator

class Translate(object):
	def translate(text):
		trans=Translator();
		ttext =trans.translate(text).text
		pron = trans.translate(text).pronunciation
		if pron == None:
			pron = ttext
		message = ttext
		return message