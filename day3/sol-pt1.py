import os
import sys
import math
f = open(os.path.join(sys.path[0], "input.txt"), "r")

totalPriority = 0

def findCommon(part1, part2):
    common = ""
    for y in part1:
        for z in part2:
            if(y == z):
                common = z 
                break
    return common

def calcPriority(value):
    if(common.isupper()):
        return ord(common) - 38
    else:
        return ord(common) - 96

for line in f:
    length = len(line)
    mid = math.floor((length / 2))
    part1 = line[0:mid]
    part2 = line[mid:length]

    # find common item in both parts
    common = findCommon(part1, part2)
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