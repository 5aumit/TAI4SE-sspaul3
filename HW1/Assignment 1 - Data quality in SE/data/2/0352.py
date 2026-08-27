import json
from bson import json_util
from bson.json_util import dumps
from pymongo import MongoClient
connection = MongoClient('localhost', 27017)
database = connection['market']
collection = database['stocks']

def findDocument(query):
  try:
    line = "--" * 45  
    result=collection.find(query).count()
    print(line +"\n")
    print("Value of Documents: "+str(result)+" Documents")
    print(line +"\n")
  
  except ValidationError as ve:
    abort(400, str(ve))
  

def main():
  line = "--" * 45  
  print("\t\t Enter Two Numerical Values Down Below \n");
  print(line+"\n")
  high = float(raw_input("Enter Highest Values# "))
  low = float(raw_input("Enter Lowest Value# "))
  myDocument = { "50-Day Simple Moving Average" : {"$gt":high,"$lt":low}}
  findDocument(myDocument)
main()