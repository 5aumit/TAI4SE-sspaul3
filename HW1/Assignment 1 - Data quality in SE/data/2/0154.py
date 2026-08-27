import utilities
import sys

if __name__ == "__main__":
    print('I am main!')
else:
    print(__name__)

for i in range(0,6):
    print(i)
    
mylist = [12, 13, 14, 13, 12]
print(mylist)

#Enter iterations to run [0-5]
#value = -1
value = 3
while (value not in range(0,6)):
    try:
        value = int(input('Enter #test runs [0-5]:'))
    except ValueError:
        print('Invalid value entered, retry')
print('Final value entered {}'.format(value))

dir(sys)
print('done!')
for i in mylist:
    utilities.myfct(i, 'hi')
    utilities.myfct1(i)
