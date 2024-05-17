# A lot of these early ones probably have a non brute force solution, but the inputs are so small that finding them is unnecessary

def iterater(nameSet, currString, valDict):
    if len(nameSet) == 0:
        ordering = currString.split(":")
        out = 0
        for i in range(len(ordering)):
            if i == len(ordering)-1:
                try:
                    out += valDict[ordering[i] + ":" + ordering[0]]
                except:
                    out += valDict[ordering[0] + ":" + ordering[i]]
            else:
                try:
                    out += valDict[ordering[i] + ":" + ordering[i+1]]
                except:
                    out += valDict[ordering[i+1] + ":" + ordering[i]]
        if out > 800:
            print(out, currString)
        return out
    solutionSet = set()
    for i in nameSet:
        nextSet = nameSet.copy()
        nextSet.remove(i)
        solutionSet.add(iterater(nextSet, currString + ":" + i, valDict))
    return max(solutionSet)

def part1():
    f = open("input.txt")
    valueDict = {}
    nameSet = set()
    for i in f:
        if i[len(i)-1] == "\n":
            i = i[:len(i)-2:]
        else:
            i = i[:len(i)-1:]
        line = i.split()
        nameSet.add(line[0])
        if line[2] == "gain":
            val = int(line[3])
        else:
            val = -int(line[3])
        if ord(line[0][0]) > ord(line[10][0]):
            index = line[0] + ":" + line[10]
        else:
            index = line[10] + ":" + line[0]
        if index in valueDict:
            valueDict[index] += val
        else:
            valueDict[index] = val
    solutionSet = set()
    for i in nameSet:
        nextSet = nameSet.copy()
        nextSet.remove(i)
        solutionSet.add(iterater(nextSet, i, valueDict))
    print(max(solutionSet))

def part2():
    f = open("input.txt")
    valueDict = {}
    nameSet = set()
    for i in f:
        if i[len(i)-1] == "\n":
            i = i[:len(i)-2:]
        else:
            i = i[:len(i)-1:]
        line = i.split()
        nameSet.add(line[0])
        if line[2] == "gain":
            val = int(line[3])
        else:
            val = -int(line[3])
        if ord(line[0][0]) > ord(line[10][0]):
            index = line[0] + ":" + line[10]
        else:
            index = line[10] + ":" + line[0]
        if index in valueDict:
            valueDict[index] += val
        else:
            valueDict[index] = val
    solutionSet = set()
    for i in nameSet:
        valueDict["Grey:" + i] = 0
    nameSet.add("Grey")
    for i in nameSet:
        nextSet = nameSet.copy()
        nextSet.remove(i)
        solutionSet.add(iterater(nextSet, i, valueDict))
    print(max(solutionSet))

part1()
part2()