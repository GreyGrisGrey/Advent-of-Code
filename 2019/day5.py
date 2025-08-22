from intCode import intMachine

def partBoth(fileNameNew = "in.txt"):
    first = intMachine(fileName = fileNameNew)
    first.addInput(1)
    second = intMachine(fileName = fileNameNew)
    second.addInput(5)
    done = [0, 0]
    final = [None, None]
    while done[0] == 0 or done[1] == 0:
        if done[0] == 0:
            done[0], res = first.step()
            if res != None:
                final[0] = res
        if done[1] == 0:
            done[1], res = second.step()
            if res != None:
                final[1] = res
    return final

if __name__ == "__main__":
    res = partBoth("in5.txt")
    print("Part 1:", res[0], "\nPart 2:", res[1])