from math import floor

def part1():
    instPairs = []
    step = [None, None, None, 0]
    for i in open("input.txt"):
        if step[0] == None:
            step[0] = int(i.split(" ")[2].strip())
        elif step[1] == None:
            step[1] = int(i.split(" ")[2].strip())
        elif step[2] == None:
            step[2] = int(i.split(" ")[2].strip())
        elif i != "\n":
            nums = i.split(" ")[1].split(",")
            for i in range(int(len(nums)/2)):
                instPairs.append([int(nums[i*2]), int(nums[(i*2)+1])])
    output = ""
    while step[3] < len(instPairs):
        res = runOp(step[0], step[1], step[2], step[3], instPairs[step[3]])
        step = res[0]
        if res[1] != None:
            output = output + str(res[1]) + ","
    return output[:-1:]

def part2():
    compareString = ""
    instPairs = []
    step = [None, None, None, 0]
    for i in open("input.txt"):
        if step[0] == None:
            step[0] = int(i.split(" ")[2].strip())
        elif step[1] == None:
            step[1] = int(i.split(" ")[2].strip())
        elif step[2] == None:
            step[2] = int(i.split(" ")[2].strip())
        elif i != "\n":
            nums = i.split(" ")[1].split(",")
            for i in range(int(len(nums)/2)):
                instPairs.append([int(nums[i*2]), int(nums[(i*2)+1])])
                compareString = compareString + nums[i*2] + nums[(i*2)+1]
    curr = [0]
    for i in range(16):
        next = []
        for j in curr:
            next.append(reversePass(j, int(compareString[len(compareString)-(1+i)])))
        curr = []
        for j in next:
            for k in j:
                curr.append(k)
    return curr

def reversePass(startA, startB):
    successes = []
    for i in range(8):
        A = 8*startA + i
        B = (A%8)^3
        C = floor(A/(2**B))
        B = B^5
        B = B^C
        if B%8 == startB:
            successes.append(startA*8 + i)
    return successes

def runOp(A, B, C, currIndex, inst):
    if inst[1] > 3:
        if inst[1] == 4:
            combo = A
        elif inst[1] == 5:
            combo = B
        else:
            combo = C
    else:
        combo = inst[1]
    match inst[0]:
        case 0:
            A = floor(A/(2**combo))
        case 1:
            B = B ^ inst[1]
        case 2:
            B = combo%8
        case 3:
            if A != 0:
                currIndex = inst[1]-1
        case 4:
            B = B ^ C
        case 5:
            return [[A, B, C, currIndex+1], combo%8]
        case 6:
            B = floor(A/(2**combo))
        case 7:
            C = floor(A/(2**combo))
    return [[A, B, C, currIndex+1], None]

print(part1())
print(min(part2()))