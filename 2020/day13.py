from math import lcm

def part1(file):
    start = None
    buses = []
    for i in open(file):
        if start == None:
            start = int(i)
        else:
            buses = i.split(",")
    count = start
    while True:
        for i in buses:
            if i.isnumeric() and count % int(i) == 0:
                return int(i) * (count - start)
        count += 1

def part2(file):
    start = None
    buses = {}
    for i in open(file):
        if start == None:
            start = int(i)
        else:
            busesPossibilities = i.split(",")
            count = 0
            for i in busesPossibilities:
                if i.isnumeric():
                    buses[int(i)] = count
                count += 1
    currConst = 0
    for i in buses:
        if currConst == 0:
            currConst = i
            currMult = i
        else:
            while True:
                if (currConst + buses[i]) % i == 0:
                    currMult = lcm(currMult, i)
                    break
                else:
                    currConst += currMult
    return currConst

print("Part 1 :", part1("input.txt"))
print("Part 2 :", part2("input.txt"))