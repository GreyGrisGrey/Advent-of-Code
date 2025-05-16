def addRule(rules, line):
    lineSplit = line.strip("\n").split(" ")
    name = lineSplit[0][0:len(lineSplit[0])-1:]
    if len(lineSplit) == 6:
        rules[name + "a"] = lineSplit[1] + ":" + lineSplit[2]
        rules[name + "b"] = lineSplit[4] + ":" + lineSplit[5]
    elif len(lineSplit) == 3:
        rules[name] = lineSplit[1] + ":" + lineSplit[2]
    elif len(lineSplit) == 2:
        rules[name] = lineSplit[1].strip('"')
    elif len(lineSplit) == 4:
        rules[name + "a"] = lineSplit[1].strip('"')
        rules[name + "b"] = lineSplit[3].strip('"')
    return

def genOptions(rules, digit):
    if digit == "a" or digit == "b":
        return digit
    newOps = []
    newRes = {}
    for i in rules:
        if i.rstrip("ab") == digit:
            newOps.append(rules[i].split(":"))
    for i in newOps:
        if len(i) == 2:
            for j in genOptions(rules, i[0]):
                for k in genOptions(rules, i[1]):
                    newRes[j + k] = True
        else:
            for j in genOptions(rules, i[0]):
                newRes[j] = True
    return newRes

def partBoth():
    rulesDict = {}
    lines = []
    total2 = 0
    total1 = 0
    for i in open("in.txt", "r"):
        if (i[0] == "a" or i[0] == "b"):
            lines.append(i.strip("\n"))
        elif i[0] != "\n":
            addRule(rulesDict, i)
    A = genOptions(rulesDict, "42")
    B = genOptions(rulesDict, "31")
    target = 8
    for i in lines:
        if len(i) % target == 0 and len(i) > target:
            aFlag = True
            bCount = 0
            bFlag = True
            for j in range(int(len(i)/target)):
                if aFlag and (i[0+(j*target):target+(j*target):] not in A):
                    aFlag = False
                    bCount += 1
                    if i[0+(j*target):target+(j*target):] not in B:
                        bFlag = False
                        break
                elif (not aFlag) and i[0+(j*target):target+(j*target):] not in B:
                    bFlag = False
                    break
                elif not aFlag:
                    bCount += 1
                if j < 2 and i[0+(j*target):target+(j*target):] not in A:
                    bFlag = False
                    break
                elif j == int(len(i)/target) - 1 and i[0+(j*target):target+(j*target):] not in B:
                    bFlag = False
            total2 += 1 if (bFlag and (bCount < int(len(i)/target)/2)) else 0
            total1 += 1 if (bFlag and (bCount == 1) and (len(i) == target*3)) else 0
    return total1, total2

print(partBoth())