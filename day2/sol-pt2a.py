import os
import sys
f = open(os.path.join(sys.path[0], "input.txt"), "r")
total=0

# X = lose
# Y = tie
# Z = win

score = {'A X':3, 'A Y':4, 'A Z':8,
	 'B X':1, 'B Y':5, 'B Z':9,
	 'C X':2, 'C Y':6, 'C Z':7}
for x in f:
    total += score[x.rstrip()]

print(total)