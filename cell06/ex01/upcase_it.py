#!/usr/bin/env python3
import sys

def uppercase_it(word):
    return str(word).upper()

if(len(sys.argv[1:])>0):
    for i in range(len(sys.argv[1:])):
        print(uppercase_it(sys.argv[i+1]))
else:
    print('none')