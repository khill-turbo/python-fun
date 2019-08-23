#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):

    #print(meal_cost)

    tip_p = (meal_cost * (20/100) )
    #print(tip_p)

    tax_p = (meal_cost * (8/100) )
    #print(tax_p)

    total = (int(meal_cost+tip_p+tax_p))

    print(total)

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
