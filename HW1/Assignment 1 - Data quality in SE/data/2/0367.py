import os
import re

def LD(s, t):
    if s == "":
        return len(t)
    if t == "":
        return len(s)
    if s[-1] == t[-1]:
        cost = 0
    else:
        cost = 1
       
    res = min([LD(s[:-1], t)+1,
               LD(s, t[:-1])+1, 
               LD(s[:-1], t[:-1]) + cost])
    return res


file_item = open('./count_1w.txt')
words = file_item.read().split('\n')
sum = 0
for word in words:
    wor = word.split('\t')[0]
    if(wor[:4]=='she'):
        sum = sum + int(word.split('\t')[1])

list = []

for word in words:
    wor = word.split('\t')[0]
    if wor[:4]=='she' and LD('shep',wor)<=3:
        list.append(word)


my_file  = open('TaskB', 'w')

for word in list:
    wor = word.split('\t')[0]
    rep = float(word.split('\t')[1])
    my_file.write(wor+'\t'+str(rep/sum)+'\n')

my_file.close()