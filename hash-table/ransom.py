#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    """The result of counters' operator substraction is a counter that shows 
    how many more values magazine is missing to match those present in rasom. 
    When an empty dict is returned, every element in rasom is present enough 
    times in magazine."""
    result = (Counter(note) - Counter(magazine)) == {}
    if result == True:
        print("Yes")
    else:
        print("No")
    """
    # too slow for large cases
    while len(note) > 0:
        if note[0] in magazine:
            #print("magazine = ", magazine)
            #print("note = ", note)
            magazine.remove(note[0])
            note.remove(note[0])
            #print("magazine = ", magazine)
            #print("note = ", note)
        else:
            print("No")
            break
    if len(note) == 0:
        print("Yes")
"""


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
