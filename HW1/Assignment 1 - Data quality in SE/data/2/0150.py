'''
Created on Sep 6, 2013

https://projecteuler.net/problem=40

An irrational decimal fraction is created by concatenating 
the positive integers:

0.12345678910
!!!1!!!
112131415161718192021...

It can be seen that the 12th digit of the fractional part 
is 1.

If dn represents the nth digit of the fractional part, find 
the value of the following expression.

d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000

@author: Cawb07
'''
import time


start = time.time()

i = 1
s = "."
while len(s) < 1000001:
    s += str(i)
    i += 1

print int(s[1])*int(s[10])*int(s[100])*int(s[1000])*\
int(s[10000])*int(s[100000])*int(s[1000000])

elapsed = time.time() - start
print "The elapsed time is %s seconds." % (elapsed)
