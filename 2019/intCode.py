from math import floor

def initializeMapping():
    spaces = {}
    curr = 0
    for i in open("in.txt").read().split(","):
        spaces[curr] = int(i)
        curr += 1
    return spaces

def getDigit(num, index):
    return floor(num/10**index) % 10

def getInstruct(num):
    return num % 100

def getWords(index, spaces):
    noun = spaces[spaces[index + 1]] if getDigit(spaces[index], 2) == 0 else spaces[index + 1]
    verb = spaces[spaces[index + 2]] if getDigit(spaces[index], 3) == 0 else spaces[index + 2]
    return noun, verb

def runOp(index, input, spaces):
    instruct = getInstruct(spaces[index])
    match instruct:
        case 99:
            return (0, 0)
        case 1:
            noun, verb = getWords(index, spaces)
            spaces[spaces[index + 3]] = noun + verb
            next = index + 4
        case 2: 
            noun, verb = getWords(index, spaces)
            spaces[spaces[index + 3]] = noun * verb
            next = index + 4
        case 3:
            spaces[spaces[index + 1]] = input
            next = index + 2
        case 4:
            print(spaces[spaces[index + 1]])
            next = index + 2
        case 5:
            noun, verb = getWords(index, spaces)
            next = verb if noun != 0 else index + 3
        case 6:
            noun, verb = getWords(index, spaces)
            next = verb if noun == 0 else index + 3
        case 7:
            noun, verb = getWords(index, spaces)
            spaces[spaces[index + 3]] = 1 if noun < verb else 0
            next = index + 4
        case 8:
            noun, verb = getWords(index, spaces)
            spaces[spaces[index + 3]] = 1 if noun == verb else 0
            next = index + 4
        case _:
            print("Error: Unknown Opcode")
            print("Opcode:", spaces[index], "Location:", index)
            return (2, 0)
    return (1, next)

def intMain(input1, input2, day):
    spaces = initializeMapping()
    index = 0
    res = 1
    if day == 2:
        spaces[1] = input1
        spaces[2] = input2
    while res == 1:
        if day == 5:
            res, index = runOp(index, input1, spaces)
        else:
            res, index = runOp(index, 0, spaces)
    if res == 2:
        return {}
    return spaces