from intCode import intMachine
from math import floor
        
def part1(fileName = "in.txt"):
    opens = [[intMachine(), [0, 0]]]
    closed = []
    steps = 1
    remaining = 1
    while True:
        if remaining == 0:
            steps += 1
            remaining = len(opens)
        remaining -= 1
        curr = opens[0]
        for i in range(4):
            copy = curr[0].clone()
            newCoords = [curr[1][0], curr[1][1]]
            if i < 2:
                newCoords[1] -= 1 if i == 0 else -1
            else:
                newCoords[0] -= 1 if i == 2 else -1
            if newCoords[0] * 1000 + newCoords[1] not in closed:
                copy.addInput(i + 1)
                res = copy.run(getOuts = True)
                if res[0] == 0 and res[1] == 2:
                    return [steps, part2(copy, newCoords)]
                elif res[0] == 0 and res[1] == 1:
                    closed.append(newCoords[0] * 1000 + newCoords[1])
                    opens.append([copy, newCoords])
        del opens[0]

def part2(endMachine, endCoords):
    opens = [[endMachine, endCoords]]
    closed = []
    steps = 0
    remaining = 1
    while len(opens) > 0:
        if remaining == 0:
            steps += 1
            remaining = len(opens)
        remaining -= 1
        curr = opens[0]
        for i in range(4):
            copy = curr[0].clone()
            newCoords = [curr[1][0], curr[1][1]]
            if i < 2:
                newCoords[1] -= 1 if i == 0 else -1
            else:
                newCoords[0] -= 1 if i == 2 else -1
            if newCoords[0] * 1000 + newCoords[1] not in closed:
                copy.addInput(i + 1)
                res = copy.run(getOuts = True)
                if res[0] == 0 and res[1] == 1:
                    closed.append(newCoords[0] * 1000 + newCoords[1])
                    opens.append([copy, newCoords])
        del opens[0]
    return steps
    
    
def printMapping(mapping, coords, curr, end):
    for i in range((coords[3] - coords[2]) + 501):
        for j in range((coords[1] - coords[0]) + 1):
            if curr[0] == j and curr[1] == i:
                print("@", end="")
            elif end != None and end[0] == j and end[1] == i:
                print("*", end="")
            elif j * 1000 + i not in mapping:
                print(" ", end="")
            elif mapping[j * 1000 + i]:
                print(".", end="")
            else:
                print("#", end="")

if __name__ == "__main__":
    res = part1("in15.txt")
    print("Part 1:", res[0], "\nPart 2:", res[1])