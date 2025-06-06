from math import prod

def checkSplittable(items, indices, goal, goalSect):
    if recurse(items, 0, [], [], 9999, 9999, int(goal * 3 / 2), indices, goalSect, True) != -1:
        return True
    return False

def changeVals(res, minI, minQ, checker):
    if checker and res[0] != -1:
        return (0, 0)
    if res[0] != -1 and res[0] <= minI:
        if res[0] < minI:
            minI = res[0]
            minQ = res[1]
        elif res[1] < minQ:
            minQ = res[1]
    return minI, minQ

def recurse(items, currIndex, taken, takenIndices, minQ, minI, goal, indices, goalSect, checker=False):
    if goal == sum(taken) and (checker or checkSplittable(items, takenIndices, goal, goalSect)):
        return (len(taken), prod(taken))
    elif len(taken) > minI or (len(taken) == minI and (goal != sum(taken) or prod(taken) >= minQ)) or currIndex >= len(items):
        return (-1, 0)
    res = recurse(items, currIndex + 1, taken.copy(), takenIndices.copy(), minQ, minI, goal, indices, goalSect, checker)
    minI, minQ = changeVals(res, minI, minQ, checker)
    copies = [taken.copy(), takenIndices.copy()]
    copies[0].append(items[currIndex])
    copies[1].append(currIndex)
    res = recurse(items, currIndex + 1, copies[0], copies[1], minQ, minI, goal, indices, goalSect, checker)
    minI, minQ = changeVals(res, minI, minQ, checker)
    return (minI, minQ)

def partBoth():
    items = []
    for i in open("in.txt"):
        items.append(int(i.strip()))
    return recurse(items, 0, [], [], 999, 999, int(sum(items)/3), [], 3), recurse(items, 0, [], [], 999, 999, int(sum(items)/4), [], 4)

print(partBoth())