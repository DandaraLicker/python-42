#!/usr/bin/env python3

say_something = input('What you gotta say? ')

while say_something != 'STOP':
    say_something = input('I got that! Anything else? :')
    if say_something == 'STOP':
        break