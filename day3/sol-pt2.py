import os
import sys
import math
from itertools import islice

totalPriority = 0

def findCommon(lines):
    common = ""
    for x in lines[0].rstrip():
        for y in lines[1].rstrip():
            for z in lines[2].rstrip():
                if(x == y == z):
                    common = x
                    break
    return common

def calcPriority(value):
    if(common.isupper()):
        return ord(common) - 38
    else:
        return ord(common) - 96


n = 3
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    for lines in iter(lambda: tuple(islice(f, n)), ()):
        common = findCommon(lines)
        totalPriority += calcPriority(common)

print("Total : " + str(totalPriority))
# a = 97
# A = 65

'''
Common : p = 16
Common : L = 38
Common : P = 42
Common : v = 22
Common : t = 20
Common : s = 19
---------------
                157
'''