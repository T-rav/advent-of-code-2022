f = open("input.txt", "r")

score=0

# X = lose
# Y = tie
# Z = win

for x in f:
    parts = x.split(" ")
    p1 = parts[0]
    p2Inst = parts[1].strip('\n')

   
    if(p2Inst == "X"): # lose
        print("lose")
    elif(p2Inst == "Y"): # tie
        print("tie")
    else:
        print("win") # win

   # elif((p1 == "A" and p2 == "B") or (p1=="B" and p2 == "C") or (p1=="C" and p2 == "A")): # win

    #score += ord(p2Move) - 87 # for the shape

f.close()

print("Score: " + str(score) ) # 23 difference
