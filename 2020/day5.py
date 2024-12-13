def part1():
    f = open("input.txt", "r")
    end = 0
    for i in f:
        row = ""
        column = ""
        for j in i:
            if j == "F":
                row = row + "0"
            elif j == "B":
                row = row + "1"
            elif j == "R":
                column = column + "1"
            elif j == "L":
                column = column + "0"
        if end < (int(row, 2) * 8) + int(column, 2):
            end = (int(row, 2) * 8) + int(column, 2)
    return end

def part2(maximum):
    f = open("input.txt", "r")
    passDict = {}
    for i in f:
        row = ""
        column = ""
        for j in i:
            if j == "F":
                row = row + "0"
            elif j == "B":
                row = row + "1"
            elif j == "R":
                column = column + "1"
            elif j == "L":
                column = column + "0"
        passDict[(int(row, 2) * 8) + int(column, 2)] = True
    count = maximum
    pastStart = False
    while True:
        count -= 1
        if pastStart and count not in passDict:
            return "Part 1: " + str(maximum) + ", Part 2: " + str(count)
        elif count in passDict:
            pastStart = True

print(part2(part1()))