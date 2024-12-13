def part1():
    f = open("input.txt")
    grid = []
    areaGrid = []
    perimDict = {}
    for i in f:
        gridLine = []
        areaLine = []
        for j in i:
            if j != "\n":
                gridLine.append(j)
                areaLine.append(0)
        grid.append(gridLine)
        areaGrid.append(areaLine)
    count = 1
    areaDict = {}
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] != "." and grid[i][j] != "#":
                perimDict[count] = 0
                letter = grid[i][j]
                areaDict[count] = DFS(grid, letter, [i, j], areaGrid, count, perimDict)
                count += 1
                hashWipe(grid, [i, j])
    total = 0
    for i in perimDict:
        total += perimDict[i] * areaDict[i]
    return total

def part2():
    f = open("input.txt")
    grid = []
    areaGrid = []
    for i in f:
        gridLine = []
        areaLine = []
        for j in i:
            if j != "\n":
                gridLine.append(j)
                areaLine.append(0)
        grid.append(gridLine)
        areaGrid.append(areaLine)
    count = 1
    areaDict = {}
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] != "." and grid[i][j] != "#":
                letter = grid[i][j]
                perimDict = {}
                areaDict[count] = part2DFS(grid, letter, [i, j], areaGrid, count, perimDict, None)
                perimeter = 0
                for k in perimDict:
                    if perimDict[k]:
                        perimeter += 1
                        direction = k[-1::]
                        eliminateSide(perimDict, k, direction)
                total += areaDict[count] * perimeter
                count += 1
                hashWipe(grid, [i, j])
    return total

def DFS(grid, letter, curr, zoning, count, perimeter):
    if curr[0] < 0 or curr[1] < 0 or curr[0] >= len(grid) or curr[1] >= len(grid):
        perimeter[count] += 1
        return 0
    if grid[curr[0]][curr[1]] == letter:
        grid[curr[0]][curr[1]] = "."
        zoning[curr[0]][curr[1]] = count
        total = 1
        total += DFS(grid, letter, [curr[0]+1, curr[1]], zoning, count, perimeter)
        total += DFS(grid, letter, [curr[0]-1, curr[1]], zoning, count, perimeter)
        total += DFS(grid, letter, [curr[0], curr[1]+1], zoning, count, perimeter)
        total += DFS(grid, letter, [curr[0], curr[1]-1], zoning, count, perimeter)
        return total
    elif grid[curr[0]][curr[1]] == ".":
        return 0
    else:
        perimeter[count] += 1
        return 0

def part2DFS(grid, letter, curr, zoning, count, perimeter, prev):
    if curr[0] < 0 or curr[1] < 0 or curr[0] >= len(grid) or curr[1] >= len(grid):
        actual = [curr[0]-prev[0], curr[1]-prev[1]]
        if actual[1] == 1:
            perimeter[str(curr[0]) + "." + str(curr[1]) + "D"] = True
        elif actual[1] == -1:
            perimeter[str(curr[0]) + "." + str(curr[1]) + "U"] = True
        elif actual[0] == 1:
            perimeter[str(curr[0]) + "." + str(curr[1]) + "R"] = True
        else:
            perimeter[str(curr[0]) + "." + str(curr[1]) + "L"] = True
        return 0
    if grid[curr[0]][curr[1]] == letter:
        grid[curr[0]][curr[1]] = "."
        zoning[curr[0]][curr[1]] = count
        total = 1
        total += part2DFS(grid, letter, [curr[0]+1, curr[1]], zoning, count, perimeter, [curr[0], curr[1]])
        total += part2DFS(grid, letter, [curr[0]-1, curr[1]], zoning, count, perimeter, [curr[0], curr[1]])
        total += part2DFS(grid, letter, [curr[0], curr[1]+1], zoning, count, perimeter, [curr[0], curr[1]])
        total += part2DFS(grid, letter, [curr[0], curr[1]-1], zoning, count, perimeter, [curr[0], curr[1]])
        return total
    elif grid[curr[0]][curr[1]] == ".":
        return 0
    else:
        actual = [curr[0]-prev[0], curr[1]-prev[1]]
        if actual[1] == 1:
            perimeter[str(curr[0]) + "." + str(curr[1]) + "D"] = True
        elif actual[1] == -1:
            perimeter[str(curr[0]) + "." + str(curr[1]) + "U"] = True
        elif actual[0] == 1:
            perimeter[str(curr[0]) + "." + str(curr[1]) + "R"] = True
        else:
            perimeter[str(curr[0]) + "." + str(curr[1]) + "L"] = True
        return 0

def hashWipe(grid, curr):
    if curr[0] >= 0 and curr[1] >= 0 and curr[0] < len(grid) and curr[1] < len(grid) and grid[curr[0]][curr[1]] == ".":
        grid[curr[0]][curr[1]] = "#"
        hashWipe(grid, [curr[0]+1, curr[1]])
        hashWipe(grid, [curr[0]-1, curr[1]])
        hashWipe(grid, [curr[0], curr[1]-1])
        hashWipe(grid, [curr[0], curr[1]+1])
    return

def inGrid(grid, curr):
    if curr[0] < 0 or curr[1] < 0 or curr[1] >= len(grid) or curr[0] >= len(grid):
        return False
    return True

def eliminateSide(perimDict, index, direction):
    if index in perimDict and perimDict[index]:
        perimDict[index] = False
        indices = index[0:-1:].split(".")
        x = int(indices[1])
        y = int(indices[0])
        if direction == "L":
            eliminateSide(perimDict, (str(y) + "." + str(x+1) + direction), direction)
            eliminateSide(perimDict, (str(y) + "." + str(x-1) + direction), direction)
        if direction == "R":
            eliminateSide(perimDict, (str(y) + "." + str(x+1) + direction), direction)
            eliminateSide(perimDict, (str(y) + "." + str(x-1) + direction), direction)
        if direction == "U":
            eliminateSide(perimDict, (str(y+1) + "." + str(x) + direction), direction)
            eliminateSide(perimDict, (str(y-1) + "." + str(x) + direction), direction)
        if direction == "D":
            eliminateSide(perimDict, (str(y+1) + "." + str(x) + direction), direction)
            eliminateSide(perimDict, (str(y-1) + "." + str(x) + direction), direction)
    else:
        return

print(part1())
print(part2())