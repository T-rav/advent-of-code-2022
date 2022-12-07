import os
import sys
f = open(os.path.join(sys.path[0], "input.txt"), "r")

score=0

for x in f:
    parts = x.split(" ")
    p1 = parts[0]
    p2Move = parts[1].strip('\n')
    p2 = chr(ord(p2Move) - 23) # rebase into A, B, C world

    if(p1 == p2): # tie
        score += 3 # for the tie
    elif((p1 == "A" and p2 == "B") or (p1=="B" and p2 == "C") or (p1=="C" and p2 == "A")): # win
        score += 6 #win

    score += ord(p2Move) - 87 # for the shape

f.close()

print("Score: " + str(score) )
