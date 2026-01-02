def part1():
    lines = open("in.txt").read().split("\n")
    beams = {lines[0].find("S"):1}
    splits = 0
    for i in range(1, len(lines) - 1):
        newBeams = {}
        for j in beams:
            if lines[i][j] == ".":
                newBeams[j] = 1 if j not in newBeams else newBeams[j] + 1
            else:
                splits += 1
                newBeams[j + 1] = 1 if j + 1 not in newBeams else newBeams[j + 1] + 1
                newBeams[j - 1] = 1 if j - 1 not in newBeams else newBeams[j - 1] + 1
        beams = newBeams
    return splits

def part2():
    lines = open("in.txt").read().split("\n")
    beams = {lines[0].find("S"):1}
    for i in range(1, len(lines) - 1):
        newBeams = {}
        for j in beams:
            if lines[i][j] == ".":
                newBeams[j] = beams[j] if j not in newBeams else newBeams[j] + beams[j]
            else:
                newBeams[j + 1] = beams[j] if j + 1 not in newBeams else newBeams[j + 1] + beams[j]
                newBeams[j - 1] = beams[j] if j - 1 not in newBeams else newBeams[j - 1] + beams[j]
        beams = newBeams
    total = 0
    for i in beams:
        total += beams[i]
    return total

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())