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
    divsbytwo = int(0)
    total = int(0)
    for h in new_set_ar:
        indices = [i for i, x in enumerate(ar) if x == h]
        # then divide by 2 and throw out remainder
        divsbytwo = int(len(indices)/2)
        # then add all of the totals and return that number
        total += (divsbytwo)
    return(total)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()


"""
John works at a clothing store. 
He has a large pile of socks that he must pair by color for sale. 
Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

sockMerchant has the following parameter(s):
    n: the number of socks in the pile
    ar: the colors of each sock

Return the total number of matching pairs of socks that John can sell.

Constraints:
1 <= n <= 100
1 <= ar[i] <= 100 where 0 <= i < n

Sample Input
9
10 20 20 10 10 30 50 10 20

Sample Output
3


# Set OUTPUT_PATH to something like below
# export OUTPUT_PATH = "/set/directory/path/and/filename.txt"
"""
