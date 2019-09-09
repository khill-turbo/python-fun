#!/bin/python3

import math
import os
import random
import re
import sys

def countConsecOnes(n):
    binaryN = f'{n:b}'
    #print("binaryN = ", binaryN)
    stringN = str(binaryN)
    #print("stringN = ", stringN)

    # get the length of the string
    j = len(stringN)
    while(j >= 1):
        # start from max length and search to smaller
        maxOnes = "1"*j
        if maxOnes in stringN:
            #print(maxOnes)
            # break as soon as the max length found
            break
        j += -1

    total = len(maxOnes)
    return(total)

if __name__ == '__main__':
    n = int(input())
    n = countConsecOnes(n)
    print(n)
