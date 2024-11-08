#!/usr/bin/env python3

import sys

first_number = int(sys.argv[1] if sys.argv[1] < sys.argv[2] else sys.argv[2])
second_number = int(sys.argv[2] if sys.argv[2] > sys.argv[1] else sys.argv[1])+1


print(list(range(first_number, second_number)))