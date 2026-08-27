def codechef(n,a,b,c,floor):
    #cook your dish here
    diff_lis = []
    time = abs(b-a)+c
    if a>=b:
        x1 = a 
        x2 = b
    elif b>a:
        x1 = b
        x2 = a
    for i in floor:
        if x2<i<x1:
            return time
    
    for i in range(len(floor)):
        if floor[i]>=x1:
            diff_lis.append(floor[i]-x1)
        
        elif floor[i]<=x2:
            diff_lis.append(x2-floor[i])
            
    time = time+2*min(diff_lis)
    return time
        
            
    
    
    

if __name__ == "__main__":
    t = int(input())
    while t>0:
    
        n,a,b,c = list(map(int,input().split()))
        floor = list(map(int,input().split()))
        print(codechef(n,a,b,c,floor))
        t = t-1
