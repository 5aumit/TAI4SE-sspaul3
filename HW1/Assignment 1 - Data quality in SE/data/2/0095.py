#Sorting for a number list
#ascending and descending
ls=[1,34,23,56,34,67,87,54,62,31,66]
ls.sort(reverse=True)
print(ls)
ls.sort()
print(ls)
#Sorting a letter's list with different scenarios
ls_l=["aaa","ertdf","ieurtff","fnjr","resdjx","jfh","r","fd"]

#1-sort according to string length from small length to bigger
ls_l.sort(key=len)
print(ls_l)

#you can always reverse
ls_l.sort(key=len,reverse=True)
print(ls_l)

#2-Sort with first alphabetical order
def FirstLetter(string):
    return string[0]

ls_l.sort(key=FirstLetter)
print(ls_l)





ls2=[[0,1,'f'],[4,2,'t'],[9,4,'afsd']]
def secondItem(ls):
    return ls[2]
ls2.sort(key=secondItem)
print(ls2)
