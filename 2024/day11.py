def part1(steps):
    f = open("input.txt", "r")
    end = 0
    line = []
    for i in f:
        line = i.split(" ")
    for i in range(steps):
        newLine = []
        for j in line:
            if int(j) == 0:
                newLine.append("1")
            elif len(j)%2 == 0:
                newLine.append(str(int(j[0:int(len(j)/2):])))
                newLine.append(str(int(j[int(len(j)/2)::])))
            else:
                newLine.append(str(int(j)*2024))
        line = newLine
    return len(line)

def newTheory(steps):
    f = open("input.txt", "r")
    startingStones = []
    for i in f:
        startingStones = i.split(" ")
    stonesDict = {}
    for i in startingStones:
        if i in stonesDict:
            stonesDict[int(i)] += 1
        else:
            stonesDict[int(i)] = 1
    for i in range(steps):
        newDict = {}
        for j in stonesDict:
            if j == 0:
                if 1 in newDict:
                    newDict[1] += stonesDict[j]
                else:
                    newDict[1] = stonesDict[j]
            elif len(str(j))%2 == 0:
                left = int(str(j)[0:int(len(str(j))/2):])
                right = int(str(j)[int(len(str(j))/2)::])
                if left in newDict:
                    newDict[left] += stonesDict[j]
                else:
                    newDict[left] = stonesDict[j]
                if right in newDict:
                    newDict[right] += stonesDict[j]
                else:
                    newDict[right] = stonesDict[j]
            else:
                if j*2024 in newDict:
                    newDict[j*2024] += stonesDict[j]
                else:
                    newDict[j*2024] = stonesDict[j]
        stonesDict = newDict
    total = 0
    for i in stonesDict:
        total += stonesDict[i]
    return total

steps = 75
#print(part1(steps))
print(newTheory(steps))