
def part1():
    f = open("input.txt")
    line = f.readline()
    searchString = "-1234567890"
    addString = ""
    summation = 0
    for i in range(len(line)):
        if line[i] in searchString:
            addString = addString + line[i]
        elif len(addString) > 0:
            summation += int(addString)
            addString = ""
    print(summation)

def part2():
    f = open("input.txt")
    line = f.readline()
    numberString = "-1234567890"
    currChar = 0
    val = 0
    while currChar < len(line):
        if line[currChar] == "{":
            res = layer(currChar+1, True, numberString, line)
            currChar = res[0]
            val += res[1]
        else:
            res = layer(currChar+1, False, numberString, line)
            currChar = res[0]
            val += res[1]
    print(val)

def layer(currChar, allOrNothing, numberString, line):
    addString = ""
    val = 0
    red1 = False
    red2 = False
    valCheck = True
    while currChar < len(line):
        if line[currChar] == "{":
            res = layer(currChar+1, True, numberString, line)
            currChar = res[0]
            val += res[1]
        elif line[currChar] == "[":
            res = layer(currChar+1, False, numberString, line)
            currChar = res[0]
            val += res[1]
        elif line[currChar] in numberString:
            addString = addString + line[currChar]
        elif len(addString) > 0:
            val += int(addString)
            addString = ""
        if red1 and red2 and line[currChar] == "d":
            valCheck = False
        elif red1 and line[currChar] == "e":
            red2 = True
        elif line[currChar] == "r" and allOrNothing:
            red1 = True
            red2 = False
        else:
            red1 = False
            red2 = False
        if line[currChar] == "]" or line[currChar] == "}":
            if len(addString) > 0:
                val += int(addString)
            if valCheck:
                return currChar+1, val
            else:
                return currChar+1, 0
        currChar += 1
    return currChar, val

part1()
part2()