import collections
import re
from collections import Counter
import operator
import pickle
import math
import json

path='C:/Users/rahul/Desktop/CSCI 544/HW 2/op_spam_train/'
#path=sys.argv[1]

badWordList = ['and','the','was','for']
RE=r'\b[^\W\d_]+\b'

# NEGATIVE TWEETS
c=collections.Counter()
NT="negativeTweets.txt/"
with open("negativeTweets.txt") as f: 
    c.update( word.lower() for line in f for word in re.findall(r'\b[^\W\d_]+\b', line) if len(word)>2 and word not in badWordList)

# POSITIVE TWEETS
d=collections.Counter()
PT="positiveTweets.txt/"
with open("positiveTweets.txt") as f: 
    d.update( word.lower() for line in f for word in re.findall(r'\b[^\W\d_]+\b', line) if len(word)>2 and word not in badWordList)

# Storing Counts in a dictionary nb
dicts=[dict(c),dict(d)]    
nb,cnt={},0
for d in dicts:
    for k, v in d.items():
        if(k in nb): nb[k][cnt]= nb[k][cnt]+v
        else: 
            nb[k]=[1,1]
            nb[k][cnt]= nb[k][cnt]+v
    cnt=cnt+1

for k,v in nb.items():
    print k,v
    
print len(nb);

totalClassWord=[0,0]
for k, v in nb.items():
    totalClassWord=[x + y for x, y in zip(totalClassWord, v)]

prob={}    
for k, v in nb.items():
    prob[k]=[0,0]
    prob[k][0]= math.log10( float(nb[k][0])/float(totalClassWord[0]))
    prob[k][1]= math.log10( float(nb[k][1])/float(totalClassWord[1]))

for k,v in prob.items():
    print k,v

#Dumping dictionary as JSON object in file
#with open('hackTechTweetClassificationModel.txt', 'wb') as handle: pickle.dump(prob, handle)
keys=json.dumps(prob, sort_keys=True)
output_file=open('hackTechTweetClassificationModel.txt', 'w')
output_file.write(keys)
output_file.close()

output_file=open('hackTechTweetPHP.php', 'w')
#Format of PHP output
#$result=mysqli_query($con, "INSERT INTO ttrain VALUES ('aaa','-2.232','222.4234')" );
for k,v in prob.items():
    strop="$result=mysqli_query($con, \"INSERT INTO ttrain VALUES (\'"+str(k)+"\',\'"+str(v[0])+"\',\'"+str(v[1])+"\')\" );\n" 
    output_file.write(strop)
output_file.close()
