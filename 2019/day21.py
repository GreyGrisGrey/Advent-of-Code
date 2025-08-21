from intCode import intMachine

def part1(fileName = "in.txt"):
    instructs = ["NOT C T\n", "NOT A J\n", "OR T J\n", "AND D J\n", "WALK\n"]
    machine = intMachine(21)
    for i in instructs:
        for j in i:
            machine.addInput(ord(j))
    res = [0, None]
    while res[0] == 0:
        res = machine.run(getOuts = True)
        if res[1] != None:
            if res[1] > 128:
                return res[1]
    return

def part2(fileName = "in.txt"):
    instructs = ["NOT C T\n", "NOT F J\n", "AND T J\n", "NOT C T\n", "AND F T\n", "AND H T\n", "OR T J\n", "NOT A T\n", "OR T J\n", "NOT B T\n", "OR T J\n", "NOT C T\n", "AND E T\n", "OR T J\n", "AND D J\n", "RUN\n"]
    machine = intMachine(21)
    for i in instructs:
        for j in i:
            machine.addInput(ord(j))
    res = [0, None]
    out = ""
    while res[0] == 0:
        res = machine.run(getOuts = True)
        if res[1] != None:
            if res[1] > 128:
                return res[1]
            out += chr(res[1])
    return

if __name__ == "__main__":
    print("Part 1:", part1("in21.txt"))
    print("Part 2:", part2("in21.txt"))