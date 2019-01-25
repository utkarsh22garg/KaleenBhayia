from wit import Wit
import json
from calculate import Calculator
class WitHandler:
	def getInfo(message_string):
		client_access_token="PQCM32TG4TIECXXTP5EGA2AFDLHTAPMD"
		client=Wit(client_access_token)
		response=client.message(message_string)
		# print(response['entities'])

		list_resp={}

		for entity in response['entities']:
			list_resp[response['entities'][str(entity)][0]['confidence']]=[str(entity),response['entities'][str(entity)][0]['value']]

		confidence_list=list(list_resp)
		# print(confidence_list)
		confidence_list=sorted(confidence_list,reverse=True)

		check=list_resp[confidence_list[0]][0]
		value=list_resp[confidence_list[0]][1]
		if check=="calculate":
			# print(value)
			content=Calculator.calculate(str(value))
		else:
			content="I couldn't understand what you just said!! Please try again"

		# print(content)
		return content