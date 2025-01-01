def part1(file):
    adaptorList = [0]
    maximum = 0
    for i in open(file):
        adaptorList.append(int(i))
        maximum = maximum if int(i) < maximum else int(i)
    adaptorList.append(maximum+3)
    adaptorList.sort()
    threes = 0
    ones = 0
    for i in range(len(adaptorList)-1):
        if adaptorList[i+1] - adaptorList[i] == 3:
            threes += 1
        elif adaptorList[i+1] - adaptorList[i] == 1:
            ones += 1
    return ones * threes

def part2(file):
    adaptorList = [0]
    adaptorDict = {}
    maximum = 0
    for i in open(file):
        adaptorList.append(int(i))
        adaptorDict[int(i)] = 0
        maximum = maximum if int(i) < maximum else int(i)
    adaptorList.append(maximum+3)
    adaptorDict[0] = 1
    adaptorDict[maximum+3] = 0
    adaptorList.sort()
    for i in adaptorList:
        for j in range(3):
            if i+j+1 in adaptorDict:
                adaptorDict[i+j+1] += adaptorDict[i]
    return adaptorDict[maximum+3]
    

print("Part 1 :", part1("input.txt"))
print("Part 2 :", part2("input.txt"))
