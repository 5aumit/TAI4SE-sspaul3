# -*- coding: utf-8 -*-
# Enter your code here. Read input from STDIN. Print output to STDOUT

n= input()
vals= list(map(int,input().split()))

def median(values):
    n=len(values)
    values = sorted(values)
    if n%2==1:
        return values[(n+1)//2 - 1]
    else:
        return int(sum(values[int((n/2)-1):int((n/2)+1)])/2)
    
def quartiles(values):
    n=len(values)
    values.sort()
    Q2=median(values)
    Q1=median(values[:int(n/2)])
    #print ("values=",values)

    if n%2==0:
        Q3=median(values[int(n/2):]) 

    else:
        Q3=median(values[int(n/2+1):])
                               
    return Q1,Q2,Q3

Q1,Q2,Q3=quartiles(vals)

print(Q1)
print(Q2)
print(Q3)
