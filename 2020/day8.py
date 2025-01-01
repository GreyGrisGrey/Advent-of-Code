def partTotal():
    maximum = 0
    instructionDict = {}
    runDict = {}
    for i in open("input.txt"):
        instructionDict[maximum] = i
        runDict[maximum] = False
        maximum += 1
    part1Val = 0
    count = 0
    possibleWrongs = []
    while True:
        if runDict[count]:
            for j in runDict:
                runDict[j] = False
            break
        else:
            runDict[count] = True
            currInst = instructionDict[count].split()
            if currInst[0] == "jmp":
                possibleWrongs.append(count)
                count += int(currInst[1]) - 1
            elif currInst[0] == "acc":
                part1Val += int(currInst[1])
            else:
                possibleWrongs.append(count)
            count += 1
    for i in possibleWrongs:
        count = 0
        part2Val = 0
        while True:
            if count == maximum:
                return "Part 1 : " + str(part1Val) + " Part 2 : " + str(part2Val)
            elif runDict[count]:
                for j in runDict:
                    runDict[j] = False
                break
            else:
                runDict[count] = True
                currInst = instructionDict[count].split()
                if (currInst[0] == "jmp" and count != i) or (count == i and currInst[0] == "nop"):
                    count += int(currInst[1]) - 1
                elif currInst[0] == "acc":
                    part2Val += int(currInst[1])
                count += 1


print(partTotal())