#!/usr/bin/env python3
import sys

if len(sys.argv[1:]) == 1:
    for letter in sys.argv[1]:
        letter = str(letter)
        if letter == 'z':
            print('z', end= '')
else:
    print('none')