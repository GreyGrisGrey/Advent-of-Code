def xSearch(grid, y, x):
    search = "MAS"
    options = [[0, 1], [-1, 0], [1, 0], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
    minimum = 0
    maximum = len(grid)-1
    success = 0
    for i in options:
        currIndex = 0
        for j in range(4):
            if currIndex == 3:
                success += 1
            elif (x+i[0]*(j+1) < minimum or x+i[0]*(j+1) > maximum or y+i[1]*(j+1) < minimum or y+i[1]*(j+1) > maximum) or ((grid[x+i[0]*(j+1)][y+i[1]*(j+1)] != search[currIndex])):
                break
            else:
                currIndex += 1
    return success

def aSearch(grid, y, x):
    search = "MAS"
    minimum = 0
    maximum = len(grid)-1
    success = 0
    if not (x-1 < minimum or x+1 > maximum or y-1 < minimum or y+1 > maximum):
        if (grid[x-1][y-1] == grid[x-1][y+1] and grid[x+1][y-1] == grid[x+1][y+1]) or (grid[x+1][y+1] == grid[x-1][y+1] and grid[x-1][y-1] == grid[x+1][y-1]):
            if (grid[x-1][y-1] != grid[x+1][y+1]) and ((grid[x-1][y-1] == "S" and grid[x+1][y+1] == "M") or (grid[x-1][y-1] == "M" and grid[x+1][y+1] == "S")):
                success += 1
    return success

def part1():
    f = open("input.txt", "r")
    end = 0
    xCoord = []
    options = []
    for i in f:
        options.append(i.strip())
    for i in range(len(options)):
        for j in range(len(options[0])):
            if options[i][j] == "X":
                xCoord.append([j, i])
    for i in xCoord:
        end += xSearch(options, i[0], i[1])
    print(end)

def part2():
    f = open("input.txt", "r")
    end = 0
    xCoord = []
    options = []
    for i in f:
        options.append(i.strip())
    for i in range(len(options)):
        for j in range(len(options[0])):
            if options[i][j] == "A":
                xCoord.append([j, i])
    for i in xCoord:
        end += aSearch(options, i[0], i[1])
    print(end)

part1()
part2()