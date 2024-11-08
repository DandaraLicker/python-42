#!/usr/bin/env python3

number: int = int(input('Enter a number: '))

for i in range(10):
    print(i,'x',number,'=', number*i)