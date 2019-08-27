#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    maximum = -999999999999999
    #print("maximum = ", maximum)
    for i in range(0, ((len(arr)-2))):
        row1 = (arr[i])
        row2 = (arr[i+1])
        row3 = (arr[i+2])
        current = int()
        for j in range(0, ((len(row1)-2))):
            #print(row1[j], row1[j+1], row1[j+2])
            current += int(row1[j] + row1[j+1] + row1[j+2])
            #print("row1 current = ", current)

            #print(row2[j+1])
            current += int(row2[j+1])
            #print("row2 current = ", current)

            #print(row3[j], row3[j+1], row3[j+2])
            current += int(row3[j] + row3[j+1] + row3[j+2])
            #print("row3 current = ", current)

            if current > maximum:
                #print("updating maximum = ", maximum, " to ", current)
                maximum = current
                #print("now maximum = ", maximum)
            current = int()

            #print("maximum = ", maximum)
        if i == (len(row1)-3):
            #print("maximum = ", maximum)
            return(maximum)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
