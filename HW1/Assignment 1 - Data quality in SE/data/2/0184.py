
#Merge Sort
#O(nlogn)

#Merge Part

from __future__ import division     #use for python2

def merge(A, B): #Merge A[0:m], B[0,n]
        (C, m, n) = ([], len(A), len(B))
        (i, j) = (0, 0)         #Current positions in A, B

        while (i + j) < (m + n):        #i+j is no. of elements merged so far
            if i == m:              #case 1: A is empty
                C.append(B[j])
                j = j+1
            elif j == n:            #case 2: B is empty
                C.append(A[i])
                i = i+1
            elif A[i] < B[j]:       #case 3: Head of A is smaller
                C.append(A[i])
                i = i+1
            elif A[i] > B[j]:       #case 4: Head of B is smaller
                C.append(B[j])
                j = j+1
            else:
                pass

        return C

#A = range(0, 100, 2)        # generate the lists
#B = range(1, 75, 2)         # generate the lists

#print merge(A, B)
#print "\n"
#print len(A) + len(B)

#Sort Part

def mergeSort(A, left, right):
    #Sort the slice A[left:right]

    if (right - left) <= 1: #Base Case
        return A[left:right]

    if (right - left) > 1:      #Recursive call
        mid = (left + right)//2

        L = mergeSort(A, left, mid)
        R = mergeSort(A, mid, right)

        return (merge(L,R))

a = range(1, 100, 2) + range(0, 100, 2)

#print a

#print mergeSort(a, 0, len(a))
