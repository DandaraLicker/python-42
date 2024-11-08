#!/usr/bin/env python3

age = int(input('Please tell me your age: '))

print(f'You are currently {age} years old.')

for i in range(3):
    mult = (i + 1) * 10
    result_age = mult+age
    print(f'In {mult} years, you\'ll be {result_age} years old.')