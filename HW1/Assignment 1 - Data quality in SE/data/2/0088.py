import json
import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier


# In[2]:


#reading json
with open("./train.json") as f:
    data = json.load(f)
df = pd.io.json.json_normalize(data)
df.columns = df.columns.map(lambda x: x.split(".")[-1])
df = df.values
ingridients = []
cusine = []
for row in df:
    ingridients.append(row[2])
    cusine.append(row[0])

# getting unique elements
cSet = set()
iSet = set()
for row in ingridients:
    for column in row:
        iSet.add(column)
for row in cusine:
    cSet.add(row)
cSet = list(cSet)
iSet = list(iSet)

#processing for training set attribuites
tI = []
for row in ingridients:
    temp = []
    for x in iSet:
        if(x in row):
            temp.append(1)
        else:
            temp.append(0)
    tI.append(temp)

#processing for training set classes    
tC = []
for x in cusine:
    tC.append(cSet.index(x))
 

#reading json file test data
with open("./test.json") as f:
    data = json.load(f)
tf = pd.io.json.json_normalize(data)
tf.columns = tf.columns.map(lambda x: x.split(".")[-1])
tf = tf.values


#converting to tuples 
testId = []
testIng = []
for row in tf:
    testId.append(row[0])
    testIng.append(row[1])


#processing for test attribuites and classes
tstIng = []
tstId = []
for row in testIng:
    temp = []
    for x in iSet:
        if(x in row):
            temp.append(1)
        else:
            temp.append(0)
    tstIng.append(temp)       


#train and classify Decision tree
dtcClf = tree.DecisionTreeClassifier()
dtcClf = dtcClf.fit(tI, tC)
dtcPrediction = dtcClf.predict(tstIng)

f = open("resultDT.csv", "w")
f.write("id,cuisine\n")
for i in range(9944):
	f.write("%s,%s\n" % (testId[i],cSet[dtcPrediction[i]]))
f.close()
    

