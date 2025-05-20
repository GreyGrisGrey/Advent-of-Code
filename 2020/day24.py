def checkGrid(x, y, spaces):
    checks = [[x+0.5, y+1], [x+0.5, y-1], [x-0.5, y+1], [x-0.5, y-1], [x+1, y], [x-1, y]]
    count = 0
    for i in checks:
        count += 1 if str(i[0]) + ":" + str(i[1]) in spaces else 0
    if count == 2 or str(x) + ":" + str(y) in spaces and count == 1:
        return True
    return False

def partBoth():
    spaceDict = {}
    total = 0
    maxX = 0
    maxY = 0
    for i in open('in.txt', "r"):
        dirDict = {"x":0.0, "y":0}
        index = 0
        i = i.strip("\n")
        while index < len(i):
            if i[index] == "e":
                dirDict["x"] += 1
                index += 1
            elif i[index] == "w":
                dirDict["x"] -= 1
                index += 1
            else:
                dirDict["y"] += 1 if i[index] == "n" else -1
                dirDict["x"] += 0.5 if i[index+1] == "e" else (-0.5)
                index += 2
        loc = str(dirDict["x"]) + ":" + str(dirDict["y"])
        if loc in spaceDict:
            spaceDict[loc] += 1
        else:
            spaceDict[loc] = 1
    checkDict = {}
    for i in spaceDict:
        if spaceDict[i] % 2 != 0:
            total += 1
            checkDict[i] = True
    maxX = 35
    maxY = 35
    for i in range(100):
        newDict = {}
        for j in range(maxX*2):
            for k in range(maxY*2):
                if checkGrid((j-maxX)/2, k-maxY, checkDict):
                    newDict[str((j-maxX)/2) + ":" + str(k-maxY)] = True
        maxX += 1
        maxY += 1
        checkDict = newDict
    return total, len(checkDict)

print(partBoth())