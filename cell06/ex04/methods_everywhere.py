#!/usr/bin/env python3

import sys



def shrink(string: str):
    sl_aux = slice(0,8)
    print(string[sl_aux])

def enlarge(string: str):
    while(len(string)<8):
        string = string + 'Z'
    print(string)

if len(sys.argv[1:])>1:
    for word in sys.argv[1:]:
        if len(word)> 8:
            shrink(word)
        else:
            enlarge(word)
else:
    print('none')