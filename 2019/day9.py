from intCode import intMachine

def partBoth(part2):
    machine = intMachine(9)
    machine.addInput(2 if part2 else 1)
    machine.deleteInputs(False)
    print("Part 2: " if part2 else "Part 1: ", end = "")
    machine.run(printOuts = True)

if __name__ == "__main__":
    partBoth(False)
    partBoth(True)