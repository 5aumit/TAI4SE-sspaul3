import os.path
from nltk.classify import NaiveBayesClassifier
import json

posfeats_file = os.path.dirname(os.path.realpath(__file__)) + '/posfeats.txt'
negfeats_file = os.path.dirname(os.path.realpath(__file__)) + '/negfeats.txt'

print posfeats_file

posfeats = []
negfeats = []

def word_feats(words):
    return dict([(word, True) for word in words])


with open(posfeats_file, 'r') as f:
    posfeats=json.loads(f.readline())

with open(negfeats_file, 'r') as f:
    negfeats=json.loads(f.readline())

#Set cut off: 4/5 for train and 1/5 for test
negcutoff = len(negfeats)*6/7
poscutoff = len(posfeats)*6/7

trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff]
testfeats = negfeats[negcutoff:] + posfeats[poscutoff:]

#The function call to train the data

classifier = NaiveBayesClassifier.train(trainfeats)
classifier.show_most_informative_features(10)

def get_sentiment(raw):
    tweetWords=[]
    words=raw.split()
    for i in words:
        i = i.lower().strip('\'$"?,.!')
        tweetWords.append(i)
    tweet = tweetWords
    return classifier.classify(word_feats(tweet))
