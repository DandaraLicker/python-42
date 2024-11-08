#!/usr/bin/env python3

word = input()

for letra in word:
    print(letra.upper() if letra.islower() else letra.lower(), end='')

print('')