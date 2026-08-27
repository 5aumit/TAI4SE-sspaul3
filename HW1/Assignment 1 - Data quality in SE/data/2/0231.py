strings = ['(())())', '(((()())()', '(()())((()))', '((()()(()))(((())))()', '()()()()(()()())()', '(()((())()(']

#print(string[0])
'''
for i in string:
    testlist = []
    for j in string[i]:
        if j == ')':
            if 
'''

def isVPS(phrase):
    testlist = []
    for char in phrase:
        if char == '(':
            testlist.append(char)
        else:
            if len(testlist) == 0:
                #return False
                return 'NO'
            else:
                testlist.pop()
    if len(testlist) == 0:
        #return True
        return 'YES'
    else:
        #return False
        return 'NO'

for string in strings:
    print(isVPS(string))
#print(isVPS(string[0]))