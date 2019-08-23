#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):

    steps = 0
    j = 0
    while (j) < ((len(c))-1):
        # if 2 or less clouds left then don't look at c[j+2]
        if (j+2) >= (len(c)):
            j += 1
            steps += 1
        # if next is 0 then jump 2
        elif (c[j+2]) == 0:
             j += 2
             steps += 1
        else:
            j += 1
            steps += 1

    print("steps = ", steps)
    return(steps)


if __name__ == '__main__':
    # To run set OUTPUT_PATH ex: OUTPUT_PATH=/my/dir/and/filename.txt
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
