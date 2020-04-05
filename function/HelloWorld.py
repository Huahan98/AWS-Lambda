import json
from botocore.vendored import requests
from datetime import datetime

def getHolidays():
	res = set()
	todayDate = datetime.today().strftime('%Y-%m-%d')
	# api endpoint
	URL = "https://date.nager.at/Api/v2/NextPublicHolidaysWorldwide"

	# defining a params dict for the parameters to be sent to the API
	PARAMS = {}

	# sending get request and saving the response as response object
	r = requests.get(url = URL, params = PARAMS)

	# extracting data in json format
	data = r.json()

	for item in data:
	    if item["date"] == todayDate:
	        res.add(item["name"])

	return res

print('Loading function')

def lambda_handler(event, context):
	S = getHolidays()
	messageString = ""
	for k in S:
		messageString += "Happy " + k + "! \n"
	#Construct the body of the response object
	transactionResponse = {}
	transactionResponse['message'] = "Hello World!\n" + messageString

	#Construct http response object
	responseObject = {}
	responseObject['statusCode'] = 200
	responseObject['headers'] = {}
	responseObject['headers']['Content-Type'] = 'application/json'
	responseObject['body'] = json.dumps(transactionResponse)

	return responseObject
