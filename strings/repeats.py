#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    # (s.count("a") --> count a's in s
    #
    # * (n // len(s)) --> multiply by n
    # and divide with integral result (discard remainder)
    # * (10 // 3) --> * 3
    #
    # + s[:n % len(s)].count("a") --> plus s[3].count("a")
    # + s[:10 % 3].count("a") --> + s[:1].count("a")
    #
    # (s.count("a") * 3 + s[:1].count("a"))
    print(s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))

    # counts 6, from example 0
    ###print(s.count("a") * (n // len(s)))
    # counts 1, from example 0
    ###print(s[:n % len(s)].count("a"))

    # Too slow
    #asdf = (s * n)
    #print("asdf = ", asdf)
    #asdf = asdf[:n]
    #print("asdf = ", asdf)
    #total = asdf.count("a") 
    #print(total)

    return(s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
