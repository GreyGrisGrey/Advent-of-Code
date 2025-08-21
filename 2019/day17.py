from intCode import intMachine
# Hardcoded part 2
def printScreen(spaces, maxY, maxX):
    for i in range(maxY):
        for j in range(maxX):
            print(spaces[j * 1000 + i], end="")

def checkIntersect(spaces, index, maxX, maxY):
    if (index + 1) % 1000 < maxY and index - 1000 > 0 and index + 1000 < maxX * 1000 and (index - 1) % 1000 < maxY:
        if spaces[index + 1] == spaces[index - 1] and spaces[index + 1] == spaces[index + 1000]:
            if spaces[index + 1000] == spaces[index - 1000] and spaces[index + 1] == "#" and spaces[index] == "#":
                return True
    return False

def checkGood(index, maxX, maxY):
    if index % 1000 < maxY and index > 0 and index < maxX * 1000:
        return True
    return False

def part1(fileName = "in.txt"):
    machine = intMachine(17)
    spaces = {}
    x = 0
    y = 0
    maxX = 0
    while True:
        res = machine.run(getOuts = True)
        if res[0] != 0:
            y -= 1
            break
        else:
            spaces[x * 1000 + y] = chr(res[1])
            if res[1] != 10 and res[1] != 35 and res[1] != 46:
                curr = [x, y]
                direction = [0, -1]
        x += 1
        if x > maxX:
            maxX = x
        if res[1] == 10:
            while x < maxX:
                x += 1
            x = 0
            y += 1
    maxY = y
    total = 0
    for i in range(maxX):
        for j in range(maxY):
            if checkIntersect(spaces, i * 1000 + j, maxX, maxY):
                total += i * j
    print("Part 1:", total)
    sequence = "LRLRLRLLRLRLRLLRLRLRLLRLRLRLLRLRLLRLRLLR"
    instructs = []
    index = 0
    count = 0
    flag = False
    flag2 = False
    while True:
        if index == len(sequence):
            flag2 = True
        if flag:
            next = [curr[0] + direction[0], curr[1] + direction[1]]
            if not checkGood(next[0] * 1000 + next[1], maxX, maxY) or spaces[next[0] * 1000 + next[1]] != "#":
                flag = False
                instructs.append(sequence[index - 1])
                while count > 0:
                    instructs.append(str(count))
                    count = 0
                count = 0
            else:
                curr = next
                count += 1
        elif flag2:
            break
        else:
            if sequence[index] == "L":
                temp = direction[0]
                direction[0] = direction[1]
                direction[1] = -temp
            else:
                temp = direction[0]
                direction[0] = -direction[1]
                direction[1] = temp
            flag = True
            index += 1

def part2(fileName = "in.txt"):
    machine = intMachine(17)
    A = "L 12 R 8 L 6 R 8 L 6"
    B = "R 8 L 12 L 12 R 8"
    C = "L 6 R 6 L 12"
    mainFunct = "A B A A B C B C C B"
    funcs = [mainFunct, A, B, C]
    machine.setIndex(0, 2)
    for i in funcs:
        res = machine.run(getOuts = True)
        while res[1] != 58:
            res = machine.run(getOuts = True)
            if res[0] == 1:
                return
        for j in i:
            if j == " ":
                machine.addInput(ord(","))
            else:
                machine.addInput(ord(j))
        machine.addInput(10)
    machine.addInput("n")
    machine.addInput(10)
    while True:
        res = machine.run(getOuts = True)
        if res[0] == 0 and res[1] > 1000:
            print("Part 1:", res[1])
        elif res[0] != 0:
            break
                
        
            

if __name__ == "__main__":
    part1("in17.txt")
    part2("in17.txt")