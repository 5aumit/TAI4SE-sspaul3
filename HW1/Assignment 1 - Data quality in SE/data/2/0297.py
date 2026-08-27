#!/usr/bin/env python

from math import factorial

F = [factorial(i) for i in range(10)]
#F[9] * 8 = 2903040 > this means no 8 digit numbers
#F[9] * 7 = 2540160 < this is the maximum that I could think of

total = 0
for i in xrange(10, 2540160):
    if sum([F[int(d)] for d in str(i)]) == i:
        total = total + i

print total
