'''
'Daniel Moulton
'3/24/15
'Implementation of the mergesort sorting algorithm in python.
'Utilizes a series of random numbers as the initial input
'Uses a top down approach to recursively sort the original list and output the final result.
'''

from random import randrange

def mergeSort(original_list):
    #initializes recursive sorting function
    #prints the final sorted list
    return subSort(original_list)

def subSort(sub_list):
    #sorts the list recursively, splitting into left and right lists
    #then calling the merge function to merge back together
    #returns the list if there is only one element
    if (len(sub_list)<2):
        return sub_list
    #uses built in integer division in python to select the middle value rounded down
    index = len(sub_list)//2
    left_list = sub_list[0:index]
    right_list = sub_list[index:len(sub_list)]
    left_list = subSort(left_list)
    right_list = subSort(right_list)
    return merge(left_list, right_list)

def merge(left_list, right_list):
    #merges the split lists back together while sorting them
    sorted_list = []
    while (len(left_list)!=0 or len(right_list)!=0):
        if (len(left_list)==0):
            sorted_list.append(right_list[0])
            del right_list[0]
            continue
        if (len(right_list)==0):
            sorted_list.append(left_list[0])
            del left_list[0]
            continue
        left = left_list[0]
        right = right_list[0]
        if (left > right):
            sorted_list.append(right)
            del right_list[0]
        elif (right > left):
            sorted_list.append(left)
            del left_list[0]
        else:
            sorted_list.append(right)
            sorted_list.append(left)
            del left_list[0]
            del right_list[0]
    return sorted_list       

def random_list(number):
    original_list = []
    for x in range(0, COUNT+1):
        original_list.append(randrange(MIN, MAX+1))
    return original_list
    
#input list
MIN = 1
MAX = 100
COUNT = 20
original_list = random_list(COUNT)
print('Original: ' + str(original_list))
print('Sorted: ' + str(mergeSort(original_list)))       

        
