def part1(file):
    total = 0
    numDict = {}
    curr = 0
    for i in open(file):
        line = i.split(",")
        for j in line:
            numDict[int(j)] = curr
            curr += 1
    for i in range(2019):
        if i < curr:
            total = 0
        else:
            if total in numDict:
                temp = numDict[total]
                numDict[total] = i
                total = i - temp
            else:
                numDict[total] = i
                total = 0
    return total

def part2(file):
    total = 0
    numDict = {}
    curr = 0
    for i in open(file):
        line = i.split(",")
        for j in line:
            numDict[int(j)] = curr
            curr += 1
    for i in range(29999999):
        if i < curr:
            total = 0
        else:
            if total in numDict:
                temp = numDict[total]
                numDict[total] = i
                total = i - temp
            else:
                numDict[total] = i
                total = 0
    return total

inputFile = "input.txt"
print(part1(inputFile))
print(part2(inputFile))