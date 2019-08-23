#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    height = 0
    valleys = 0
    for i in s:
        # if you're below sea level and you're about to hit sea level increment valleys
        if i == "U":
            if height == -1:
                valleys += 1
            height += 1
        elif i == "D":
            height += -1
    return(valleys)

if __name__ == '__main__':
    # To run set OUTPUT_PATH ex: OUTPUT_PATH = "/my/dir/and/filename.txt"
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
