def part1(file):
    memoryDict = {}
    for i in open(file):
        command = i.split(" = ")
        if len(command[0]) == 4:
            mask = command[1].strip()
        else:
            newString = ""
            command[1] = bin(int(command[1]))[2::]
            while len(command[1]) < 36:
                command[1] = "0" + command[1]
            for i in range(36):
                if mask[i] != "X":
                    newString += mask[i]
                else:
                    newString += command[1][i]
            memoryDict[command[0][4:-1:]] = newString
    total = 0
    for i in memoryDict:
        total += int("0b" + memoryDict[i], 2)
    return total


def part2(file):
    memoryDict = {}
    for i in open(file):
        command = i.split(" = ")
        if len(command[0]) == 4:
            mask = command[1].strip()
        else:
            newIndex = ""
            index = bin(int(command[0][4:-1:]))[2::]
            while len(index) < 36:
                index = "0" + index
            for i in range(36):
                if mask[i] != "0":
                    newIndex += mask[i]
                else:
                    newIndex += index[i]
            enumerator("", int(command[1]), memoryDict, newIndex)
    total = 0
    for i in memoryDict:
        total += memoryDict[i]
    return total


def enumerator(currString, value, memoryDict, totalString):
    while True:
        if len(currString) == 36:
            memoryDict[currString] = value
            return
        elif totalString[len(currString)] != "X":
            currString += totalString[len(currString)]
        else:
            enumerator(currString + "1", value, memoryDict, totalString)
            enumerator(currString + "0", value, memoryDict, totalString)
            return

print("Part 1 :", part1("input.txt"))
print("Part 2 :", part2("input.txt"))