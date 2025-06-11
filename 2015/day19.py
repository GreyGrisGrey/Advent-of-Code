def split(textLine):
    textLine = textLine + "Z"
    steps = []
    index = 0
    curr = ""
    while index < len(textLine):
        if textLine[index] == textLine[index].upper() and len(curr) != 0:
            steps.append(curr)
            curr = ""
        curr += textLine[index]
        index += 1
    return steps

def addRule(start, end, rules):
    res = split(end)
    index = 0
    while start + "-" + str(index) in rules:
        index += 1
    if len(res) <= 2:
        rules[start + "-" + str(index)] = res
        return start + str(index)
    index2 = 0
    index3 = 0
    while index3 < len(res)-2:
        while str(index2) + "-0" in rules:
            index2 += 1
        rules[str(index2) + "-0"] = [res[index3], res[index3+1]]
        res[index3+1] = str(index2)
        index3 += 1
    rules[str(start) + "-" + str(index)] = [res[index3], res[index3+1]]
    return start + str(index)

def reverseRule(rule, ruleDict, reverseDict):
    res = ruleDict[rule]
    next = rule.split("-")[0]
    if len(res) == 2:
        key = res[0] + ":" + res[1]
    else:
        key = res[0]
    index = 0
    while key + "-" + str(index) in reverseDict:
        index += 1
    reverseDict[key + "-" + str(index)] = next
    return

def stepBack(matrix, index, reverseDict):
    nextLine = []
    for i in range(len(matrix[index])-1):
        nextLine.append({})
        for j in range(index+1):
            left = matrix[j][i]
            right = matrix[len(matrix)-1-j][i+1+j]
            getCombs(left, right, reverseDict, nextLine[i], index)
    return nextLine

def getCombs(left, right, reverseDict, addDict, num2):
    index = 0
    for i in left:
        newLeft = i.split("-")[0]
        for j in right:
            index = 0
            newRight = j.split("-")[0]
            while newLeft + ":" + newRight + "-" + str(index) in reverseDict:
                newIndex = 0
                if reverseDict[newLeft + ":" + newRight + "-" + str(index)].strip("0123456789") != "":
                    num = 1 + left[i] + right[j]
                else:
                    num = 0 + left[i] + right[j]
                addDict[reverseDict[newLeft + ":" + newRight + "-" + str(index)] + "-" + str(newIndex)] = num
                index += 1
    return

def newString(input, replacement, index):
    new = ""
    for i in range(len(input)):
        new += input[i] if i != index else replacement[0] + replacement[1]
    return new

def part1(input, rules):
    optionsDict = {}
    for i in range(len(input)):
        curr = input[i] + "-"
        index = 0
        while curr + str(index) in rules:
            res = newString(input, rules[curr + str(index)], i)
            optionsDict[res] = True
            index += 1
    return len(optionsDict)

def partBoth(fileName):
    ruleDict = {}
    reverseDict = {}
    skip = False
    for i in open(fileName):
        if i == "\n":
            skip = True
        elif skip:
            mol = split(i.strip())
            break
        else:
            res = i.strip("\n").split(" => ")
            res = addRule(res[0], res[1], ruleDict)
    for i in ruleDict:
        reverseRule(i, ruleDict, reverseDict)
    res = part1(mol, ruleDict)
    for i in range(len(mol)):
        mol[i] = {mol[i] + "-z":0}
    matrix = [mol]
    count = len(mol)-1
    index = 0
    while count > 0:
        matrix.append(stepBack(matrix, index, reverseDict))
        index += 1
        count -= 1
    for i in matrix[len(matrix)-1]:
        for j in i:
            return res, i[j]
    return 1

print(partBoth("in.txt"))