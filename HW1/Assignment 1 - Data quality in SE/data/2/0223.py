import requests
import json
r = requests.get('http://pythonspot.com/')

jsondata = str(r.headers).replace("'", '"')
print(jsondata)
#headerObj = json.loads(jsondata)
#ERROR >> json.decoder.JSONDecodeError: Expecting ',' delimiter: line 1 column 556 (char 555)

#print(headerObj)["server"]
#print(headerObj)['content-length']
#print(headerObj)['content-encoding']
#print(headerObj)['content-type']
#print(headerObj)['date']
#print(headerObj)['x-powered-by']

## I could not the problem.