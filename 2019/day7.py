from intCode import intMachine
from itertools import permutations

def part1():
    options = permutations([0, 1, 2, 3, 4])
    maximum = 0
    for i in options:
        prev = 0
        count = 0
        for j in i:
            newMachine = intMachine(7)
            newMachine.addInput(j)
            newMachine.addInput(prev)
            prev = newMachine.run(getOuts=True)[1]
            count += 1
        if prev > maximum:
            maximum = prev
    return maximum

def part2():
    options = permutations([5, 6, 7, 8, 9])
    maximum = 0
    for i in options:
        machines = [intMachine(7), intMachine(7), intMachine(7), intMachine(7), intMachine(7)]
        count = 0
        for j in i:
            machines[count].addInput(j)
            count += 1
        prev = 0
        count = 0
        while True:
            machines[count].addInput(prev)
            res = machines[count].run(getOuts = True)[1]
            if res == None:
                break
            prev = res
            count = (count + 1) % 5
        if prev > maximum:
            maximum = prev
    return maximum

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())