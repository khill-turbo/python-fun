# Declare second integer, double, and String variables.
i = 4
d = 4.0
s = 'HackerRank '

# Read and save an integer, double, and String to your variables.
import os
myInt = int(input())
myFloat = float(input())
myString = input()

# Print the sum of both integer variables on a new line.
print(i+myInt)

# Print the sum of the double variables on a new line.
floatTotal = float(d+myFloat)
print("%.1f" % floatTotal)
# alternative formatting # print("{0:.1f}".format(floatTotal))

# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
catString = (s+myString)
print(catString)

