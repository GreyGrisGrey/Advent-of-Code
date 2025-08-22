from intCode import intMachine

def part1(fileNameNew = "in.txt"):
    machine = intMachine(fileName = fileNameNew)
    machine.setIndex(1, 12)
    machine.setIndex(2, 2)
    machine.run()
    return machine.getIndex(0)

def part2(fileNameNew = "in.txt"):
    for i in range(100):
        for j in range(100):
            machine = intMachine(fileName = fileNameNew)
            machine.setIndex(1, i)
            machine.setIndex(2, j)
            machine.run()
            if machine.getIndex(0) == 19690720:
                return (i * 100 + j)

if __name__ == "__main__":
    print("Part 1:", part1("in2.txt"))
    print("Part 2:", part2("in2.txt"))