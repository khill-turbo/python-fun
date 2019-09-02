# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import os
import random
import re
import sys

if __name__ == '__main__':    
    t = int(input())

    inputs = []
    for i in range(t*2):
        inputs.append(input())

    # put the name and numbers into a dictionary
    namenumDict = dict()
    for i in range(t):
        namenumDict.update(x.split(' ') for x in (inputs[i]).split(','))

    # look through the second half of the inputs
    for i in range(t,((t*2))):
        if (inputs[i]) not in namenumDict:
            print("Not found")
        else:
            print((inputs[i])+"="+(namenumDict.get(inputs[(i)])))
