from math import floor

def part1():
    f = open("input.txt", "r")
    testEnds = []
    testVals = []
    for i in f:
        step1 = i.split(":")
        testEnds.append(step1[0])
        step2 = step1[1].split(" ")[1::]
        vals = []
        for j in step2:
            vals.append(j.strip())
        testVals.append(vals)
    total = 0
    for i in range(len(testEnds)):
        exponent = len(testVals[i])-1
        count = 0
        while count < 2**exponent:
            bitString = bin(count)[2::]
            while len(bitString) < exponent:
                bitString = "0" + bitString
            if checkRes(testVals[i], testEnds[i], bitString):
                total += int(testEnds[i])
                break
            count += 1
    print(total)

def part2():
    f = open("input.txt", "r")
    testEnds = []
    testVals = []
    for i in f:
        step1 = i.split(":")
        testEnds.append(step1[0])
        step2 = step1[1].split(" ")[1::]
        vals = []
        for j in step2:
            vals.append(j.strip())
        testVals.append(vals)
    total = 0
    for i in range(len(testEnds)):
        exponent = len(testVals[i])-1
        count = 0
        while count < 3**exponent:
            bitString = intToTern(count)
            while len(bitString) < exponent:
                bitString = "0" + bitString
            if checkRes(testVals[i], testEnds[i], bitString):
                total += int(testEnds[i])
                break
            count += 1
        print(i)
    print(total)

def intToTern(integer):
    newString = ""
    if integer == "0":
        return "0"
    while integer != 0:
        newString = str(integer%3) + newString
        integer = floor(integer/3)
    return newString

def checkRes(vals, end, bits):
    if bits[0] == "0":
        currEnd = int(vals[0]) + int(vals[1])
    elif bits[0] == "1":
        currEnd = int(vals[0]) * int(vals[1])
    else:
        currEnd = int(vals[0] + vals[1])
    for i in range(len(bits)-1):
        if bits[i+1] == "0":
            currEnd = currEnd + int(vals[i+2])
        elif bits[i+1] == "1":
            currEnd = currEnd * int(vals[i+2])
        else:
            currEnd = int(str(currEnd) + vals[i+2])
    if currEnd == int(end):
        return True
    return False


part1()
part2()