import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def squarestring(number):
    """Takes a number,  split it, calculates the sum of the square of each digit"""
    string = str(number)
    sum = 0
    for digit in string:
        #print("Debug: sum = {}".format(sum), file=sys.stderr)
        sum += int(digit)**2
    return sum


n = int(input())
for i in range(n):
    memory  = set()
    x = input()
    print("Debug: x = {}".format(x, file=sys.stderr))
    memory.add(x)
    y = x
    while y != 1:
        y = squarestring(y)
        print("Debug: y = {}".format(y, file=sys.stderr))
        if y in memory:
            print("{} :(".format(x))
            break
        memory.add(y)
    if y == 1:
        print("{} :)".format(x))


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

