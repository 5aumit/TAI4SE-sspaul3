#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import urllib2
#this is executed by a cron job on the pi inside the pooltable
secret ='secret'
baseurl='https://pooltable.mysite.com/'
url = baseurl + 'gettrans.php?secret=' + secret
req = urllib2.Request(url)
f = urllib2.urlopen(req)
response = f.read()
f.close()
print response
#check if there is a transaction
if response != 'error' and response != 'false' and response != False:
    obj = json.loads(response)
    trans = str(obj['transaction_hash'])
#move the transaction to the processed table and delete from unprocessed
    url = baseurl + 'deltrans.php?secret=' + secret + '&trans=' + trans 
    req = urllib2.Request(url)
    f = urllib2.urlopen(req)
    response = f.read()
    f.close()
#if transaction was moved correctly, set off the solanoid
    if response == '*ok*':
        print response
        #run solanoid script
