from intCode import intMachine
from math import floor

def printCode(mapping):
    print("Part 2:")
    maxX = -1000
    minX = 1000
    maxY = -1000
    minY = 1000
    for i in mapping:
        if floor(i/100) > maxX:
            maxX = floor(i/100)
        if i % 100 > maxY:
            maxY = i % 100
        if i % 100 < minY:
            minY = i % 100
        if floor(i/100) < minX:
            minX = floor(i/100)
    for i in range((maxY + 1) - minY):
        newLine = ""
        for j in range(maxX - minX):
            if (i + minY) + (j + minX) * 100 in mapping and mapping[(i + minY) + (j + minX) * 100] == 1:
                newLine += "#"
            else:
                newLine += " "
        print(newLine)
    

def partBoth(two = False, fileNameNew = "in.txt"):
    machine = intMachine(fileName = fileNameNew)
    currSpace = [0, 0]
    direction = [0, -1]
    mapping = {}
    if two:
        mapping[0] = 1
    else:
        mapping[0] = 0
    while True:
        machine.addInput(mapping[currSpace[0] * 100 + currSpace[1]])
        res = machine.run(getOuts = True)
        if res[0] != 0:
            if not two:
                return len(mapping) - 1
            else:
                printCode(mapping)
            break
        mapping[currSpace[0] * 100 + currSpace[1]] = res[1]
        res = machine.run(getOuts = True)
        if res[1] == 1:
            temp = direction[0]
            direction[0] = -direction[1]
            direction[1] = temp
        else:
            temp = -direction[0]
            direction[0] = direction[1]
            direction[1] = temp
        currSpace[0] += direction[0]
        currSpace[1] += direction[1]
        if currSpace[0] * 100 + currSpace[1] not in mapping:
            mapping[currSpace[0] * 100 + currSpace[1]] = 0

if __name__ == "__main__":
    print("Part 1:", partBoth(False, "in11.txt"))
    partBoth(True, "in11.txt")