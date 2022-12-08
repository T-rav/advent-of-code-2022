import os
import sys
import math
f = open(os.path.join(sys.path[0], "input.txt"), "r")

class assignedSegment:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.prettyPrint = ""

    def print(self):
        if(self.prettyPrint == ""):
            result = ""
            for x in range(0,self.start-1):
                result += "."

            for x in range(self.start, self.end+1):
                result += str(x)

            for x in range(self.end+1, 10):
                result += "."


            self.prettyPrint = result

        return self.prettyPrint
    
    def overlaps(self, otherSegment):
        myRange = range(self.start, self.end)
        theirRange = range(otherSegment.start, otherSegment.end)
        intersection = range(max(myRange.start,theirRange.start), min(myRange.stop-1,theirRange.stop-1)+1)

        print(intersection.start <= intersection.stop)

        if(intersection.start <= intersection.stop):
            return True
        
        return False
        
def parseInputIntoObject(assignment):
    sections = assignment.split('-')
    start = int(sections[0])
    end = int(sections[1])

    return assignedSegment(start, end)

pairsContainedInOtherPairs = 0
for x in f:
    parts = x.rstrip().split(',')
    part1 = parseInputIntoObject(parts[0])
    part2 = parseInputIntoObject(parts[1])

    print(part1.print())
    print(part2.print())
    if(part1.overlaps(part2)):
        print("overlap")
        pairsContainedInOtherPairs+=1
    
print(pairsContainedInOtherPairs) # expecting 4 on sample

