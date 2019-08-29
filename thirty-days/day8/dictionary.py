# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    # TODO: try using 2 dictionaries to make this run more efficiently 
    
    t = int(input())

    thisdict = dict()
    inputs = []
    for i in range(t*2):
        inputs.append(input())

    for i in range(t):
        thisdict.update(x.split(' ') for x in (inputs[i]).split(','))

    holder = thisdict.keys()
    for i in range(t,((t*2))):
        if (inputs[i]) not in holder:
            print("Not found")
        else:
            print((inputs[i])+"="+(thisdict.get(inputs[(i)])))

