#!/usr/bin/env python3
import sys

def downcase_it(word):
    return str(word).lower()

if(len(sys.argv[1:])>0):
    for i in range(len(sys.argv[1:])):
        print(downcase_it(sys.argv[i+1]))
else:
    print('none')