def part1():
    f = open("input.txt", "r")
    listlist = []
    antennaDict = {}
    grid = []
    for i in f:
        gridLine = []
        for j in i:
            gridLine.append(j)
        grid.append(gridLine)
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] in antennaDict:
                listlist[antennaDict[grid[i][j]]].append([i, j])
            elif grid[i][j] != ".":
                antennaDict[grid[i][j]] = count
                count += 1
                listlist.append([])
                listlist[antennaDict[grid[i][j]]].append([i, j])
    total = 0
    minimum = 0
    maximum = len(grid) - 1
    for i in listlist:
        for j in range(len(i)):
            for k in range(len(i)):
                if j != k:
                    placement = (2*i[j][0] - i[k][0], 2*i[j][1] - i[k][1])
                    if not (placement[0] < minimum or placement[0] > maximum or placement[1] < minimum or placement[1] > maximum):
                        grid[placement[0]][placement[1]] = "#"
    for i in grid:
        for j in i:
            if j == "#":
                total += 1
    print(total)

def part2():
    f = open("input.txt", "r")
    listlist = []
    antennaDict = {}
    grid = []
    for i in f:
        gridLine = []
        for j in i:
            gridLine.append(j)
        grid.append(gridLine)
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] in antennaDict:
                listlist[antennaDict[grid[i][j]]].append([i, j])
            elif grid[i][j] != ".":
                antennaDict[grid[i][j]] = count
                count += 1
                listlist.append([])
                listlist[antennaDict[grid[i][j]]].append([i, j])
    total = 0
    minimum = 0
    maximum = len(grid) - 1
    for i in listlist:
        for j in range(len(i)):
            for k in range(len(i)):
                if j != k:
                    step = (i[j][0] - i[k][0], i[j][1] - i[k][1])
                    placement = [i[j][0], i[j][1]]
                    while not (placement[0] < minimum or placement[0] > maximum or placement[1] < minimum or placement[1] > maximum):
                        grid[placement[0]][placement[1]] = "#"
                        placement[0] += step[0]
                        placement[1] += step[1]
    for i in grid:
        for j in i:
            if j == "#":
                total += 1
    print(total)

part1()
part2()