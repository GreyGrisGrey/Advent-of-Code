from intCode import intMachine

def part1(fileName = "in.txt"):
    machine = intMachine(2)
    machine.setIndex(1, 12)
    machine.setIndex(2, 2)
    machine.run()
    print("Part 1:", machine.getIndex(0))

def part2(fileName = "in.txt"):
    for i in range(100):
        for j in range(100):
            machine = intMachine(2)
            machine.setIndex(1, i)
            machine.setIndex(2, j)
            machine.run()
            if machine.getIndex(0) == 19690720:
                print("Part 2:", i * 100 + j)
                break

if __name__ == "__main__":
    part1("in2.txt")
    part2("in2.txt")