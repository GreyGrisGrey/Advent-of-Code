from intCode import intMachine

def partBoth(part2, fileName = "in.txt"):
    machine = intMachine(9)
    machine.addInput(2 if part2 else 1)
    machine.deleteInputs(False)
    print("Part 2: " if part2 else "Part 1: ", end = "")
    machine.run(printOuts = True)

if __name__ == "__main__":
    partBoth(False, "in9.txt")
    partBoth(True, "in9.txt")