#!/usr/bin/env python3

import sys

if len(sys.argv[1:]) > 0:
    password = input('What was the parameter? ')
    if password == sys.argv[1]:
        print('Good job!')
    else:
        print('Nope, sorry...')
else:
    print('none')
   
