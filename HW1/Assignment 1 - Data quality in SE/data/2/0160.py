import math
while 1:
        n=input()
        if n==0:
                break
        s=map(int,raw_input().split())
        m=0.0
        for i in range(n):
                m+=s[i]
        m=m/n
        a=0.0
        for i in range(n):
                a+=(s[i]-m)**2
        a=(a/n)**0.5
        print a