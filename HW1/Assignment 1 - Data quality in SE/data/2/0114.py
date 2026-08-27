#!/usr/bin/python

import itertools

#lines: Prime numbers sieve w/fancy generators
def iter_primes():
     numbers = itertools.count(2)
     while True:
         prime = numbers.next()
         yield prime
         numbers = itertools.ifilter(prime.__rmod__, numbers)

for p in iter_primes():
    if p > 500:
        break
    print p
