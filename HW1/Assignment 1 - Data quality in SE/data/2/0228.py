
def max_product(n):
    lst, lstnums, res, num = [], [], [], 1
    for i in range(0, n+1):
        lstnums.append(i)
        for j in str(i):
            num *= int(j)
        lst.append(num)
        num = 1
​
    maxlst = max(lst)
    for i in range(len(lst)):
        if lst[i] == maxlst:
            res.append(lstnums[i])
​
    return res

