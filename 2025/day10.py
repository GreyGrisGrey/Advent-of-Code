from math import gcd

def spanning(currArrangement, buttons, currIndex, countAdded, goal):
    if checkGood(goal, currArrangement):
        return countAdded
    elif currIndex == len(buttons):
        return 1000
    res1 = spanning(currArrangement, buttons, currIndex + 1, countAdded, goal)
    res2 = spanning(modifyArrange(currArrangement, buttons[currIndex]), buttons, currIndex + 1, countAdded + 1, goal)
    return min(res1, res2)

def checkGood(goal, curr):
    for i in range(len(goal)):
        if goal[i] != curr[i]:
            return False
    return True

def modifyArrange(curr, button):
    new = curr.copy()
    for i in button:
        new[i] = False if new[i] else True
    return new

def part1():
    lines = []
    for i in open("in.txt").read().split("\n"):
        i = i.split(' ')
        goal = []
        buttons = []
        for j in range(1, len(i) - 1):
            nums = list(map(lambda x: int(x), i[j][1:len(i[j]) - 1:].split(",")))
            buttons.append(nums)
        for j in i[0]:
            if j == ".":
                goal.append(False)
            elif j == "#":
                goal.append(True)
        lines.append([goal, buttons])
    total = 0
    curr = 1
    for i in lines:
        curr += 1
        start = [False] * len(i[0])
        total += spanning(start, i[1], 0, 0, i[0])
    return total

def solve(jolts, buttons):
    eqs = [[] for i in range(len(jolts))]
    for i in range(len(jolts)):
        for j in buttons:
            if i not in j:
                eqs[i].append(0)
            else:
                eqs[i].append(1)
        eqs[i].append(jolts[i])
    maximums = [9999] * len(buttons)
    for i in eqs:
        for j in range(len(i) - 1):
            if i[len(i) - 1] < maximums[j] and i[j] == 1:
                maximums[j] = i[len(i) - 1]
    return getResEqual(eqs, maximums)

def getResEqual(eqs, maximums):
    extras = []
    oldEqs = []
    for i in eqs:
        oldEqs.append(i.copy())
    sets = []
    done = []
    for i in range(len(eqs[0]) - 1):
        good = False
        eqSpecific = None
        for j in range(len(eqs)):
            if eqs[j][i] != 0 and j not in done:
                good2 = True
                for k in sets:
                    if eqs[j][k] != 0:
                        good2 = False
                        break
                if good2:
                    good = True
                    sets.append(i)
                    done.append(j)
                    eqSpecific = j
                    break
        if good:
            for j in range(len(eqs)):
                if j != eqSpecific:
                    shrinkLine(eqs[eqSpecific])
                    shrinkLine(eqs[j])
                    equalize(eqs[eqSpecific], eqs[j], i)
        else:
            extras.append(i)
    
    presses = {}
    removeList = []
    for i in range(len(sets)):
        good = True
        bonus = []
        for j in range(len(eqs[0]) - 1):
            if j != sets[i] and eqs[done[i]][j] != 0:
                good = False
                bonus.append(j)
        if good:
            presses[sets[i]] = eqs[done[i]][len(eqs[0]) - 1] * eqs[done[i]][sets[i]]
            removeList.append(done[i])
    for i in range(len(eqs)):
        remove = True
        for j in eqs[i]:
            if j != 0:
                remove = False
        if remove and i not in removeList:
            removeList.append(i)
    removeList.sort()
    removeList.reverse()
    
    total = 0
    for i in presses:
        for j in oldEqs:
            if j[i] == 1:
                j[len(j) - 1] -= presses[i]
                j[i] = 0
        total += presses[i]
    for i in oldEqs:
        for j in range(len(i) - 1):
            if i[j] == 1 and i[len(i) - 1] < maximums[j]:
                maximums[j] = i[len(i) - 1]
        
    
    for i in range(len(sets)):
        for j in range(len(eqs)):
            if done[i] != j:
                equalize(eqs[done[i]], eqs[j], sets[i])
    for i in removeList:
        del eqs[i]
    maxButtons = 0
    for i in eqs:
        newSum = 0
        for j in range(len(i) - 1):
            if i[j] != 0:
                newSum += 1
        if i[len(i) - 1] > maxButtons:
            maxButtons = newSum
    
    leftovers = []
    isolated = []
    
    if len(eqs) != 0:
        for i in range(len(eqs[0]) - 1):
            for j in eqs:
                if j[i] != 0 and i in sets:
                    isolated.append(i)
                elif j[i] != 0 and i not in leftovers:
                    leftovers.append(i)
        pressLimit = []
        for i in leftovers:
            pressLimit.append(maximums[i])
        res = stage3(eqs, leftovers, isolated, maximums)
        return total + res
    return total


def equalize(eq1, eq2, keyIndex):
    multiply(eq1, eq2, keyIndex)
    if eq1[keyIndex] > 0:
        while eq2[keyIndex] > 0:
            for i in range(len(eq2)):
                eq2[i] -= eq1[i]
        while eq2[keyIndex] < 0:
            for i in range(len(eq2)):
                eq2[i] += eq1[i]
    if eq1[keyIndex] < 0:
        while eq2[keyIndex] > 0:
            for i in range(len(eq2)):
                eq2[i] += eq1[i]
        while eq2[keyIndex] < 0:
            for i in range(len(eq2)):
                eq2[i] -= eq1[i]
    shrinkLine(eq1, keyIndex)
    shrinkLine(eq2)
        
                
def multiply(eq1, eq2, keyIndex):
    if eq2[keyIndex] == 0:
        return
    mult1 = eq1[keyIndex]
    mult2 = eq2[keyIndex]
    for i in range(len(eq1)):
        eq1[i] *= mult2
        eq2[i] *= mult1
    
    
def shrinkLine(eq, keyIndex = None):
    flip = False
    if keyIndex != None and eq[keyIndex] < 0:
        flip = True
    divisor = None
    first = None
    for i in range(len(eq)):
        if eq[i] != 0:
            if first == None:
                first = eq[i]
            elif divisor == None:
                divisor = gcd(first, eq[i])
            else:
                divisor = gcd(divisor, eq[i])
    if divisor != None:
        for i in range(len(eq)):
            eq[i] = int(eq[i]/divisor)
    if flip:
        for i in range(len(eq)):
            eq[i] = -eq[i]


def makeConsistent(eqs, newEq):
    newEqs = []
    for i in eqs:
        newEqs.append(i.copy())
        keyIndex = 0
        for j in range(len(i)):
            if i[j] != 0:
                keyIndex = j
                break
        equalize(i, newEq, keyIndex)
    keyIndex = 0
    for i in range(len(newEq)):
        if newEq[i] != 0:
            keyIndex = i
            break
    for i in newEqs:
        equalize(newEq, i, keyIndex)
    newEqs.append(newEq)
    return [newEqs, checkConsistent(newEqs)]


def checkConsistent(eqs):
    for i in eqs:
        allZero = True
        for j in range(len(eqs[0]) - 1):
            if i[j] != 0:
                shrinkLine(i, j)
                allZero = False
        if allZero and i[len(i) - 1] != 0:
            return False
        if i[len(i) - 1] < 0:
            return False
    return True


def stage3(eqs, left, iso, pressLimit):
    newEqs = []
    for i in iso:
        newEq = [i, []]
        for j in eqs:
            if j[i] != 0:
                for k in range(len(j)):
                    if k in left and k != len(j) - 1:
                        newEq[1].append(-j[k])
                    elif k == len(j) - 1:
                        newEq[1].append(j[k])
                    elif k == i:
                        newEq.append(j[k])
        newEqs.append(newEq)
    best = newBFS(newEqs, left, pressLimit)
    return best


def newBFS(eqs, left, pressLimit):
    leftVals = [[0] * len(left)]
    remaining = 1
    steps = 0
    currLevel = 0
    best = 9999
    cache = {}
    while True:
        if len(leftVals) == 0:
            break
        curr = leftVals[0]
        res = checkCon2(eqs, curr, pressLimit)
        if res[0] and res[1] + currLevel < best:
            best = res[1] + currLevel
        if currLevel == best:
            break
        for i in range(len(left)):
            if curr[i] < pressLimit[left[i]]:
                nextVals = curr.copy()
                nextVals[i] += 1
                newNum = 0
                for j in nextVals:
                    newNum *= 1000
                    newNum += j
                if newNum not in cache:
                    cache[newNum] = True
                    leftVals.append(nextVals)
        del leftVals[0]
        remaining -= 1
        if remaining == 0:
            remaining = len(leftVals)
            currLevel += 1
            cache = {}
        steps += 1
    return best
            

def checkCon2(eqs, freeVals, pressLimit):
    total = 0
    for i in eqs:
        total2 = 0
        for pos, num in enumerate(i[1]):
            if pos < len(i[1]) - 1:
                total2 += freeVals[pos] * num
            else:
                total2 += num
        if total2 < 0 or total2 > pressLimit[i[0]] * i[2] or total2 / i[2] % 1 != 0:
            return [False, 9999]
        total += int(total2 / i[2])
    return [True, total]


def part2():
    lines = []
    for i in open("in.txt").read().split("\n"):
        i = i.split(' ')
        buttons = []
        for j in range(1, len(i) - 1):
            nums = list(map(lambda x: int(x), i[j][1:len(i[j]) - 1:].split(",")))
            buttons.append(nums)
        jolts = list(map(lambda x: int(x), i[len(i) - 1].strip("}{").split(",")))
        lines.append([jolts, buttons])
    total = 0
    curr = 1
    for i in lines:
        curr += 1
        total += solve(i[0], i[1])
    return total

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())