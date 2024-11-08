#!/usr/bin/env python3

import sys

if(len(sys.argv) > 3):
    for i in range(len(sys.argv) - 1):
        print(f'{sys.argv[len(sys.argv)-1-i]}')
else:
    print('none\n')