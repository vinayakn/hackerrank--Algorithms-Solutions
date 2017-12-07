#!/bin/python

import sys


s = raw_input().strip()
cnt=0
for i in s:
    
    if i.upper()==i:
        cnt+=1
print cnt+1
        
        

