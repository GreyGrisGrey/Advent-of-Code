#Slow and not ideal, will need to be updated later.

def countCube(x, y, z, actives):
    count = 0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if (str(x + (i-1)) + ":" + str(y + (j-1)) + ":" + str(z + (k-1))) in actives:
                    count += 1
    return count

def countCube2(x, y, z, w, actives):
    count = 0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    if (str(x + (i-1)) + ":" + str(y + (j-1)) + ":" + str(z + (k-1)) + ":" + str(w + (l-1))) in actives:
                        count += 1
    return count

def part1():
    maxZ = 0
    maxX = None
    activeDict = {}
    currY = 0
    for i in open("in.txt", "r"):
        currX = 0
        for j in i:
            if j == "#":
                activeDict[str(currX) + ":" + str(currY) + ":0"] = True
            currX += 1
        if maxX == None:
            maxX = currX
        currY += 1
    maxY = currY
    for i in range(6):
        newDict = {}
        for j in range(maxZ+3):
            for k in range(maxY+3):
                for l in range(maxX+3):
                    adj = countCube(l-(1+i), k-(1+i), j-(1+i), activeDict)
                    if adj == 3 or (adj == 4 and (str(l-(1+i)) + ":" + str(k-(1+i)) + ":" + str(j-(1+i))) in activeDict):
                        newDict[(str(l-(1+i)) + ":" + str(k-(1+i)) + ":" + str(j-(1+i)))] = True
        activeDict = newDict
        maxZ += 2
        maxY += 2
        maxX += 2
    return len(activeDict)

def part2():
    maxW = 0
    maxZ = 0
    maxX = None
    activeDict = {}
    currY = 0
    for i in open("in.txt", "r"):
        currX = 0
        for j in i:
            if j == "#":
                activeDict[str(currX) + ":" + str(currY) + ":0:0"] = True
            currX += 1
        if maxX == None:
            maxX = currX
        currY += 1
    maxY = currY
    for i in range(6):
        newDict = {}
        for j in range(maxZ+3):
            for k in range(maxY+3):
                for l in range(maxX+3):
                    for m in range(maxW+3):
                        adj = countCube2(l-(1+i), k-(1+i), j-(1+i), m-(1+i), activeDict)
                        if adj == 3 or (adj == 4 and (str(l-(1+i)) + ":" + str(k-(1+i)) + ":" + str(j-(1+i)) + ":" + str(m-(1+i))) in activeDict):
                            newDict[(str(l-(1+i)) + ":" + str(k-(1+i)) + ":" + str(j-(1+i))) + ":" + str(m-(1+i))] = True
        activeDict = newDict
        maxZ += 2
        maxY += 2
        maxX += 2
        maxW += 2
    return len(activeDict)

print(part1())
print(part2())