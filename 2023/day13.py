def skipCheck(skip, coords, index):
    if skip != None and coords[0] == skip[0] and coords[1] == skip[1] and index == skip[2]:
        return False
    return True

def equalCheck(pattern, index, coords, vertical):
    if vertical and pattern[index][coords[0]] != pattern[index][coords[1]]:
        return True
    elif not vertical and pattern[coords[0]][index] != pattern[coords[1]][index]:
        return True
    return False

def checkReflects(index, pattern, vertical, patternDict=None, skip=None):
    reflects = True
    coords = [index, index+1]
    length1 = len(pattern[0]) if vertical else len(pattern)
    length2 = len(pattern) if vertical else len(pattern[0])
    while coords[0] >= 0 and coords[1] < length1:
        for i in range(length2):
            if equalCheck(pattern, i, coords, vertical) and skipCheck(skip, coords, i):
                name = str(coords[0]) + ":" + str(coords[1]) + ":" + ('V' if vertical else "H")
                if name not in patternDict:
                    patternDict[name] = i
                else:
                    patternDict[name] = None
                reflects = False
        coords[0] -= 1
        coords[1] += 1
    if vertical:
        return index + 1 if reflects else 0
    return (index+1)*100 if reflects else 0

def checkPattern(pattern):
    total = 0
    patternDict = {}
    for i in range(len(pattern)-1):
        total += checkReflects(i, pattern, False, patternDict)
    for i in range(len(pattern[0])-1):
        total += checkReflects(i, pattern, True, patternDict)
    newLine = 0
    for i in patternDict:
        if patternDict[i] != None:
            line = True if i[len(i)-1] == "V" else False
            coords = i.split(":")
            index = int((int(coords[1])-int(coords[0])-1)/2) + int(coords[0])
            newLine += checkReflects(index, pattern, line, patternDict, [int(coords[0]), int(coords[1]), patternDict[i]])
    return total, newLine

def partBoth(fileName):
    patterns = []
    newPattern = []
    total1 = 0
    total2 = 0
    for i in open(fileName, "r"):
        if i[0] == "\n":
            patterns.append(newPattern)
            newPattern = []
        else:
            newPattern.append(i.strip("\n"))
    patterns.append(newPattern)
    for i in patterns:
        res = checkPattern(i)
        total1 += res[0]
        total2 += res[1]
    return total1, total2

print(partBoth("in.txt"))