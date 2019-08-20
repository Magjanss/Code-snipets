#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    level = 0
    valleys = 0
    for step in s:
        if step == 'U':
            level += 1
            if level == 0:
                valleys += 1
        else:
            level -= 1
        print("step {} to level {} having crossed {} valleys.".format(step, level, valleys))
    return valleys
    # return len(s.split("UD"))-1 #NOTE wrogn due to: ABOVE sealevel



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #n = int(input())
    n = 0
    #s = input()
    s = "DDUUDDUDUUUD"
    result = countingValleys(n, s)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()