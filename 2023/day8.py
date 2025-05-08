class Node():
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right
    
    def returnNext(self, letter):
        if letter == "R":
            return self.right
        return self.left
    
    def getName(self):
        return self.name

def determineSteps(node, nodeMap, endNodes, count, instruct):
    endFlag = False
    steps = 0
    endSkip = True
    while True:
        if endSkip:
            endSkip = False
        elif node in endNodes:
            break
        if count == len(instruct):
            count = 0
        node = nodeMap[node.returnNext(instruct[count])]
        count += 1
        steps += 1
    return [node, steps]
import math
def part1():
    nodeDict = {}
    instruct = None
    skip = True
    for i in open("in.txt", "r"):
        if instruct == None:
            instruct = i.strip()
        elif skip:
            skip = False
        else:
            name = i[0:3:]
            nodeDict[name] = Node(i[0:3:], i[7:10:], i[12:15:])
            if name == "AAA":
                curr = nodeDict[name]
            elif name == "ZZZ":
                end = nodeDict[name]
    steps = 0
    count = 0
    while curr != end:
        if count == len(instruct):
            count = 0
        curr = nodeDict[curr.returnNext(instruct[count])]
        count += 1
        steps += 1
    return steps

def part2():
    instruct = None
    ends = []
    starts = []
    nodeDict = {}
    for i in open("in.txt", "r"):
        if instruct == None:
            instruct = i.strip("\n")
        elif i != "\n":
            name = i[0:3:]
            left = i[7:10:]
            right = i[12:15:]
            nodeDict[name] = Node(name, left, right)
            if name[2] == "Z":
                ends.append(name)
            elif name[2] == "A":
                starts.append(name)
    nextEnds = []
    count = 0
    for i in starts:
        count2 = count
        steps = 0
        curr = nodeDict[i]
        while curr.getName() not in ends:
            curr = nodeDict[curr.returnNext(instruct[count2])]
            steps += 1
            count2 = (count2 + 1) % len(instruct)
        nextEnds.append(int(steps))
    total = nextEnds[0]
    for i in range(len(nextEnds)-1):
        total *= int(nextEnds[i+1] / math.gcd(total, nextEnds[i+1]))
    total
    return total


print(part1())
print(part2())