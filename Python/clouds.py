#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumpcount = 0
    currentpos = 0
    while currentpos < len(c) - 2:
        if c[currentpos + 2] == 0:
            currentpos += 1
        currentpos += 1    
        jumpcount += 1    
    lastjump = ((len(c)-1)  - currentpos )
    return jumpcount + lastjump
    
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #n = int(input())

    #c = list(map(int, input().rstrip().split()))
    c = [0, 0, 1, 0, 0, 1, 0, 0]
    result = jumpingOnClouds(c)
    print("{} => {}".format(c, result ))
    # fptr.write(str(result) + '\n')

    # fptr.close()
