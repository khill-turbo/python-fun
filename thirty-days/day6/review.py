# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
import os
import random
import re
import sys

def printStuff(inputs):
    list_s = list(inputs)
    new_s_List = []
    for i in range(0, (len(list_s))):
        if (i % 2) == 0:
            new_s_List.append(list_s[i])

    new_s_List.append(" ")

    for i in range(0, (len(list_s))):
        if (i % 2) == 1:
            new_s_List.append(list_s[i])

    new_s_List = ''.join(new_s_List)
    print(new_s_List)


if __name__ == '__main__':
    t = int(input())
    inputs = []
    for i in range(t):
        inputs.append(input())

    for i in range(t):
        printStuff(inputs[i])
    
