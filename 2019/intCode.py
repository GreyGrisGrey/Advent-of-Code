def initializeMapping():
    spaces = {}
    curr = 0
    for i in open("in.txt").read().split(","):
        spaces[curr] = int(i)
        curr += 1
    return spaces

def runOp(index, spaces):
    match spaces[index]:
        case 99:
            return 0
        case 1:
            spaces[spaces[index + 3]] = spaces[spaces[index + 1]] + spaces[spaces[index + 2]]
        case 2: 
            spaces[spaces[index + 3]] = spaces[spaces[index + 1]] * spaces[spaces[index + 2]]
        case _:
            return 2
    return 1

def intMain(input1, input2):
    spaces = initializeMapping()
    index = 0
    res = 1
    spaces[1] = input1
    spaces[2] = input2
    while res == 1:
        res = runOp(index, spaces)
        index += 4
    if res == 2:
        print("Error: Unknown Opcode")
        return {}
    return spaces