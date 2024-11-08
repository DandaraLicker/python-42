#!/usr/bin/env python3


number1 = int(input('Enter the first number:'))
number2 = int(input('Enter the second number:'))
result = number1 * number2

print(f'{number1} x {number2} = {result}')
if result < 0:
    print('This result is negative.')
elif result > 0:
    print('This result is positive')
else:
    print('This result is both positive and negative.')