#!/usr/bin/env python3

try:
    number = float(input('Give me a number: '))

    decimal = number - int(number) > 0 

    if decimal:
        print('This number is a decimal.')
    else:
        print('This number is an integer.')
except:
    print('ERROR \n')
    
    

