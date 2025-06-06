#rough. very rough.

def checkGood(x, y, grid):
    if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[y]) or grid[y][x] == "-":
        return False
    return True

def findFastO(nothing, goal, dirGrid, currIndex, curr):
    end = []
    if dirGrid[curr[0][0]][curr[0][1]] == goal[currIndex]:
        end = [[curr[0][0], curr[0][1], curr[0][2]]]
    else:
        while len(end) == 0:
            newCurr = []
            for j in curr:
                for i in range(4):
                    newPos = j.copy()
                    newPos[1] += 1 if i == 1 else -1 if i == 3 else 0
                    newPos[0] += 1 if i == 2 else -1 if i == 0 else 0
                    newPos[2] += "^" if i == 0 else ">" if i == 1 else "v" if i == 2 else "<"
                    if checkGood(newPos[1], newPos[0], dirGrid):
                        newCurr.append(newPos)
                        if dirGrid[newPos[0]][newPos[1]] == goal[currIndex]:
                            end.append(newPos)
            curr = newCurr
    for i in range(len(end)):
        end[i][2] += "A"
    if currIndex != len(goal) - 1:
        newEnd = []
        endDict = {}
        endStrings = []
        for i in end:
            endStrings.append(i[2])
        minimum = 100000
        for i in end:
            res = findFastO(nothing, goal, dirGrid, currIndex+1, [i])
            for j in res:
                if len(res) < minimum:
                    minimum = len(res)
                    endDict = {j:True}
                elif len(res) == minimum:
                    endDict[j] = True
        for i in endDict:
            newEnd.append(i)
    else:
        newEnd = []
        for i in end:
            newEnd.append(i[2])
    return newEnd

def findFast(nothing, goal, dirGrid, currIndex, curr, moveDict):
    sections = splitString(goal)
    newStrings = [""]
    for i in sections:
        if i in moveDict:
            for j in newStrings:
                j += moveDict[i]
        else:
            newSections = findFastO(nothing, i, dirGrid, 0, curr)
            newNewStrings = {}
            for j in newStrings:
                for k in newSections:
                    newNewStrings[j + k] = True
            newStrings = []
            for j in newNewStrings:
                newStrings.append(j)
    return newStrings

def mapUp(string, moveDict, isString=True):
    if isString:
        currString = ""
        newDict = {}
        currStep = 0
        while currStep < len(string):
            currString += string[currStep]
            if string[currStep] == "A":
                if currString == ">^>A":
                    currString = ">>^A"
                elif currString == "<v<A":
                    currString = "v<<A"
                elif currString == ">vA":
                    currString = "v>A"
                if currString not in newDict:
                    newDict[currString] = 0
                newDict[currString] += 1
                currString = ""
            currStep += 1
    else:
        newDict = {}
        for i in string:
            res = splitString(moveDict[i])
            for j in res:
                currString = j
                if currString not in newDict:
                    newDict[currString] = 0
                newDict[currString] += string[i]
    return newDict

def splitString(string):
    currIndex = 0
    splits = []
    currSplit = ""
    while currIndex < len(string):
        currSplit += string[currIndex]
        if string[currIndex] == "A":
            splits.append(currSplit)
            currSplit = ""
        currIndex += 1
    return splits

def findShortestO(string, dirGrid, moveDict):
    res = findFastO("", string, dirGrid, 0, [[0, 2, ""]])
    step2s = {}
    minimum = 999999
    for j in res:
        res2 = findFastO("", j, dirGrid, 0, [[0, 2, ""]])
        for k in res2:
            if len(k) < minimum:
                step2s = {j:True}
                minimum = len(k)
            elif len(k) == minimum:
                step2s[j] = True
    for j in step2s:
        moveDict[string] = j

def findShortest(string, dirGrid, moveDict):
    res = findFast("", string, dirGrid, 0, [[0, 2, ""]], moveDict)
    resDict = {}
    for i in res:
        resDict[i] = True
    minimum = 999999
    stepMin = [99999, 99999, 99999, 99999, 99999]
    stepDicts = [resDict, {}, {}, {}, {}]
    for i in range(4):
        for j in range(i):
            currStep = i-1
            while currStep > -1:
                delList = []
                for k in stepDicts[currStep]:
                    valid = False
                    for l in stepDicts[currStep][k]:
                        if l in stepDicts[currStep+1]:
                            valid = True
                            break
                    if not valid:
                        delList.append(k)
                for k in delList:
                    del stepDicts[currStep][k]
                currStep -= 1
        for j in stepDicts[i]:
            options = []
            res2 = findFast("", j, dirGrid, 0, [[0, 2, ""]], moveDict)
            for k in res2:
                if "<v<" in k or ">^>" in k:
                    pass
                elif len(k) < stepMin[i+1]:
                    options = [k]
                    stepMin[i+1] = len(k)
                    stepDicts[i+1] = {k:True}
                elif len(k) == stepMin[i+1]:
                    options.append(k)
                    stepDicts[i+1][k] = True
            stepDicts[i][j] = options
        if len(stepDicts[0]) == 1 or len(stepDicts[1]) == 1:
            break
    curr = []
    for i in stepDicts[0]:
        if len(i) < minimum:
            curr = [i]
            minimum = len(i)
        elif len(i) == minimum:
            curr.append(i)
    moveDict[string] = curr[0]

def convertNum(string, numGrid):
    currIndex = 0
    curr = [3, 2, ""]
    while currIndex < len(string):
        target = [0, 0]
        while string[currIndex] not in numGrid[target[0]]:
            target[0] += 1
        while string[currIndex] != numGrid[target[0]][target[1]]:
            target[1] += 1
        dirDict = {}
        lefts = -(target[1] - curr[1])
        downs = target[0] - curr[0]
        dirDict["L"] = lefts
        dirDict["R"] = -lefts
        dirDict["D"] = downs
        dirDict["U"] = -downs
        if (lefts == 2 and curr[0] == 3) or (lefts == 1 and curr[0] == 3 and curr[1] == 1):
            order = ["U", "L", "D", "R"]
        elif downs > 0 and (abs(downs) >= abs(curr[0]-3)):
            order = ["R", "D"]
        else:
            order = ["L", "D", "U", "R"]
        for i in order:
            while dirDict[i] > 0:
                if i == "R":
                    curr[1] += 1
                    curr[2] += ">"
                elif i == "L":
                    curr[1] -= 1
                    curr[2] += "<"
                elif i == "U":
                    curr[0] -= 1
                    curr[2] += "^"
                else:
                    curr[0] += 1
                    curr[2] += "v"
                dirDict[i] -= 1
        currIndex += 1
        curr[2] += "A"
    return curr[2]

def multDict(dictionary):
    total = 0
    for i in dictionary:
        total += len(i) * dictionary[i]
    return total

def optimiseMove(curr, moveDict):
    end = moveDict[curr]
    segments = splitString(end)
    newSegments = []
    left = 0
    down = 0
    for i in segments:
        start = [left, down]
        for j in i:
            if j == "<":
                left += 1
            elif j == "v":
                down += 1
            elif j == ">":
                left -= 1
            elif j == "^":
                down -= 1
        if start[0] == 0 and start[1] == 0 and left == 2:
            newSegments.append("v<<A")
        elif start[0] == 2 and start[1] == 1 and down == 0:
            if left == 1:
                newSegments.append(">^A")
            else:
                newSegments.append(">>^A")
        elif start[0] == 1 and start[1] == 0 and left == 2:
            newSegments.append("v<A")
        else:
            newString = ""
            while start[0] < left:
                start[0] += 1
                newString += "<"
            while start[1] < down:
                start[1] += 1
                newString += "v"
            while start[1] > down:
                start[1] -= 1
                newString += "^"
            while start[0] > left:
                start[0] -= 1
                newString += ">"
            newSegments.append(newString + "A")
    moveDict[curr] = "".join(newSegments)

def partBoth(steps):
    numGrid = ["789", "456", "123", "-0A"]
    dirGrid = ["-^A", "<v>"]
    dirs = ["A", "vA", "^A", "<A", ">A", "<<A", ">>A", "v<A", "<vA", ">>^A", ">^>A", "v<<A", "<v<A", "^<A", "^>A", "<^A", ">^A", ">vA"]
    nums = []
    dirsTest = ["A", "^A", "<A", ">A", "<<A", ">>A", "^<A", "<^A", "<v<A", "^>A", "vA", "v<<A", ">>^A", ">^>A"]
    moveDict = {}
    addDirs = ["^^<<A", "<<^^A", "<^<^A", "^<<^A", "^<^<A", "<^^<A", "^^^<A", "vv>>A", "v>A", "<<vA"]
    total = 0
    for i in open("in.txt"):
        res = i.strip()
        nums.append((int(res[0:3:]), convertNum(i.strip(), numGrid)))
    for i in nums:
        res = splitString(i[1])
        for j in res:
            addDirs.append(j)
    for i in addDirs:
        dirs.append(i)
    for i in dirsTest:
        findShortest(i, dirGrid, moveDict)
    for i in dirs:
        if i not in moveDict:
            findShortest(i, dirGrid, moveDict)
    for i in moveDict:
        optimiseMove(i, moveDict)
    for i in nums:
        res = i[1]
        skip = True
        for j in range(steps+1):
            res = mapUp(res, moveDict, skip)
            skip = False
        total += multDict(res) * i[0]
    return total

print(partBoth(2))
print(partBoth(25))