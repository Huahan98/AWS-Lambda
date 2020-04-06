import json
from botocore.vendored import requests
from datetime import datetime

print('Loading function')

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

def lambda_handler(event, context):
  S = getHolidays()
  holidayString = ""
  for k in S:
    holidayString += "Happy " + k + "! \n"
  if holidayString == "":
    holidayString = "Today is not a holiday in any Country!"
  message = "Hello World!\n" + holidayString

  #Construct http response object
  responseObject = {}
  responseObject['statusCode'] = 200
  responseObject['headers'] = {}
  responseObject['headers']['Content-Type'] = 'text/html; charset=utf-8'
  responseObject['body'] = message

  return responseObject
