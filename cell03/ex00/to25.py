#!/usr/bin/env python3

number = input('Enter a number less than 25: ')

if number.isnumeric():
    number = int(number)
else: 
    print('Error \n') 
    quit()


if number > 25:
    print('Error \n')

while(number <=25):
    print('Inside the loop, my variable is', number)
    number += 1