#!/usr/bin/env python3
import sys

if len(sys.argv[1:]):
    for word in sys.argv[1:]:
            if not word.endswith('ism'):
                print(f'{word}ism')
else:
     print('none')