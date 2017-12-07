#!/bin/python

import sys

def migratoryBirds(n, ar):
    # Complete this function
    
    d={}
    for i in ar:
        if i in d.keys():
            d[i]+=1
        else:
            d[i]=1
            
    #print d         
    #return max(a)+1
    return max(d, key=lambda k: d[k])
            
    
n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = migratoryBirds(n, ar)
print(result)

