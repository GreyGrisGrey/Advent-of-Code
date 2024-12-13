def part1():
    f = open("input.txt", "r")
    total = 0
    tempDict = {}
    for i in f:
        for j in i:
            tempDict[j] = True
        if i == "\n":
            total += len(tempDict)-1
            tempDict = {}
    total += len(tempDict)-1
    return total

def part2():
    f = open("input.txt", "r")
    total = 0
    tempDict = {}
    count = 0
    for i in f:
        if i == "\n":
            for j in tempDict:
                if tempDict[j] == count:
                    total += 1
            tempDict = {}
            count = 0
            total -= 1
        else:
            for j in i:
                if j in tempDict:
                    tempDict[j] += 1
                else:
                    tempDict[j] = 1
            count += 1
    for j in tempDict:
        if tempDict[j] == count:
            total += 1
    return total

print(part1())
print(part2())