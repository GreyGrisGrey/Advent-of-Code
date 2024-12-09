def part1():
    f = open("input.txt", "r")
    line = ""
    for i in f:
        line = i
    #ok
    count = 0
    total = {}
    highestIndex = -1
    while count < len(line):
        if count%2 == 0:
            total[int(count/2)] = int(line[count])
            highestIndex += 1
        count += 1
    inactualValues = 0
    for i in range(len(line)):
        if i%2 == 0:
            inactualValues += int(line[i])
    curr = 0
    currIndex = -1
    summary = 0
    actualMaximum = inactualValues
    while inactualValues > 0:
        while curr == 0:
            currIndex += 1
            curr = int(line[currIndex])
        if currIndex % 2 == 0:
            summary += (actualMaximum - inactualValues) * int(currIndex/2)
            curr -= 1
            inactualValues -= 1
        else:
            nextMult = highestIndex
            total[highestIndex] -= 1
            summary += (actualMaximum - inactualValues) * nextMult
            if total[highestIndex] == 0:
                highestIndex -= 1
            inactualValues -= 1
            curr -= 1
    end = 0
    print(summary)
    return end

def part2():
    f = open("input.txt", "r")
    line = ""
    for i in f:
        line = i
    #ok
    countSpace = 0
    countVal = 0
    spaces = {}
    values = {}
    valuesValues = {}
    amimum = 0
    allValues = 0
    for i in range(len(line)):
        if i%2 == 0:
            values[countVal*10] = int(line[i])
            valuesValues[countVal*10] = countVal
            countVal += 1
            maximum = countVal*10 + 9
            allValues += int(line[i])
        else:
            spaces[countSpace] = int(line[i])
            countSpace += 1
    SETlength = len(values)
    for i in range(SETlength):
        nextCheck = ((SETlength-1)-i)*10
        for j in range(countSpace):
            if j < ((SETlength-1)-i) and spaces[j] >= values[nextCheck]:
                chck = 0
                while True:
                    if (j*10 + chck) in values:
                        chck += 1
                    else:
                        values[j*10 + chck] = values[nextCheck]
                        valuesValues[j*10 + chck] = valuesValues[nextCheck]
                        break
                spaces[j] -= values[nextCheck]
                spaces[int(nextCheck/10) - 1] += values[nextCheck]
                values[nextCheck] = 0
                break
    for i in range(countSpace):
        if spaces[i] != 0:
            check = 0
            while True:
                if (i*10 + check) in values:
                    check += 1
                else:
                    values[i*10 + check] = spaces[i]
                    allValues += spaces[i]
                    valuesValues[i*10 + check] = 0
                    break
    total = 0
    curr = 0
    currIndex = -1
    setMax = maximum
    setAll = allValues
    for i in range(setMax):
        if allValues <= 0:
            break
        while curr == 0:
            currIndex += 1
            if currIndex in values:
                curr = values[currIndex]
        while curr != 0:
            total += (setAll - allValues) * valuesValues[currIndex]
            curr -= 1
            allValues -= 1
    print(total)



part1()
part2()