import json
from botocore.vendored import requests
from datetime import datetime

print('Loading function')

def lambda_handler(event, context):
	message = "Hello World!\n"

	#Construct http response object
	responseObject = {}
	responseObject['statusCode'] = 200
	responseObject['headers'] = {}
	responseObject['headers']['Content-Type'] = 'text/html; charset=utf-8'
	responseObject['body'] = message

	return responseObject
