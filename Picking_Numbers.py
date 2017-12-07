#!/bin/python

import sys


n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))

print(max(a.count(x)+a.count(x+1) for x in set(a)))
