#!/usr/bin/env python3

array = [2, 8, 9, 48, 8, 22, -12, 2]

result_array = []

print(array)

for i in array:
    if(i > 5):
        result_array.append(i+2)
        
result_array = set(result_array)

print(result_array)