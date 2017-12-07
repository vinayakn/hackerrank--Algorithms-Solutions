#!/bin/python

import sys


n = int(raw_input().strip())
scores = map(int,raw_input().strip().split(' '))
m = int(raw_input().strip())
alice = map(int,raw_input().strip().split(' '))
# your code goes here



x = set(scores)  ##

x = list(x)      ##
x.sort()         ## Elimination of Duplicates and resorting 
leng = len(x)+1
lo = 0           ## Storage of past indexes

for score in alice:
    rank = leng                               #  Binary Search given 
    hi = leng - 1                             #  remaining Indexes
    while lo < hi:                            #
        mid = (lo+hi)//2                      #
        if x[mid] <= score: lo = mid+1        #
        else: hi = mid                        #
    rank -= lo                                # Return rank
    print(rank)                               # Print result
