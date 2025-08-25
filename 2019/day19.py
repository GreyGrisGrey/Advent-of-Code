from intCode import intMachine

def part1(fileName = "in.txt"):
    count = 0
    for i in range(50):
        for j in range(50):
            machine = intMachine(fileName = fileName)
            machine.addInputs([i, j])
            res = machine.run(getOuts = True)
            if res[1] != 0:
                count += 1
    return count

# Takes a minute
def part2(fileName = "in.txt"):
    currX = 0
    currY = 870
    while True:
        machine = intMachine(fileName = fileName)
        machine.addInputs([currX, currY])
        res = machine.run(getOuts = True)
        if res[1] == 1:
            break
        else:
            currX += 1
    while True:
        while True:
            machine = intMachine(fileName = fileName)
            machine.addInputs([currX, currY])
            res = machine.run(getOuts = True)
            if res[1] == 1:
                break
            else:
                currX += 1
        size = 0
        while True:
            machine = intMachine(fileName = fileName)
            machine.addInputs([currX + size, currY])
            res = machine.run(getOuts = True)
            if res[1] == 0:
                break
            size += 1
        baseX = currX
        while True:
            machine = intMachine(fileName = fileName)
            machine.addInputs([baseX, currY + 99])
            res = machine.run(getOuts = True)
            if res[1] == 1:
                break
            else:
                baseX += 1
        if size - (baseX - currX) >= 100:
            return (baseX * 10000) + currY
        currY += 1

if __name__ == "__main__":
    print("Part 1:", part1("in19.txt"))
    print("Part 2:", part2("in19.txt"))