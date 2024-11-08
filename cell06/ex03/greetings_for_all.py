#!/usr/bin/env python3

def greetings(name=''):
    if len(name)> 0:
        print('Hello, ', name)
    else:
        print('Hello, noble stranger.')

try:
    greetings('Alexandra')
    greetings('Wil')
    greetings()
    greetings(42)
except:
    print('Error! It was not a name.')