f = open("input.txt", "r")
elfCounter=1
elfValue=0
maxValue=0
maxElf=0

for x in f:
    if(x != "\n"):
        elfValue += int(x)
    else:
        if(elfValue > maxValue and elfValue != 73211 and elfValue != 71575): #73211 - 1st, 71575 - 2nd, 69172 - 3rd = 213958
            maxValue=elfValue
            maxElf=elfCounter
            
        elfCounter+=1
        elfValue=0
f.close()

print("elf "+str(maxElf)+" has "+str(maxValue)) # max calories 