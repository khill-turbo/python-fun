#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    # count how many of each unique integer
    new_set_ar = set(ar)
    divsbytwo = 0
    total = 0
    for h in new_set_ar:
        indices = [i for i, x in enumerate(ar) if x == h]
        # then divide by 2 and throw out remainder
        divsbytwo = int(len(indices)/2)
        # then add all of the totals and return that number
        total += (divsbytwo)
    return(total)


if __name__ == '__main__':
    # To run set OUTPUT_PATH ex: OUTPUT_PATH=/my/dir/and/filename.txt
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
