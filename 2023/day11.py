from math import floor
def checkRowColumn(index, grid):
    row = True
    col = True
    for i in range(len(grid)):
        if grid[i][index] == "#":
            col = False
        if grid[index][i] == "#":
            row = False
        if (not row) and (not col):
            return False, False
    return row, col

def calcDistance(start, end, gap, rows, cols):
    startY = floor(start/1000)
    startX = start % 1000
    endY = floor(end/1000)
    endX = end % 1000
    dist = 0
    while startX != endX or startY != endY:
        if startX > endX:
            dist += gap if cols[startX] else 1
            startX -= 1
        elif startX < endX:
            dist += gap if cols[startX] else 1
            startX += 1
        if startY > endY:
            dist += gap if rows[startY] else 1
            startY -= 1
        elif startY < endY:
            dist += gap if rows[startY] else 1
            startY += 1
    return dist

def partBoth(gap):
    rowDict = {}
    colDict = {}
    starDict = {}
    distDict = {}
    grid = []
    total = 0
    for i in open("in.txt", "r"):
        gridLine = []
        for j in i:
            if j != "\n":
                gridLine.append(j)
        grid.append(gridLine)
    for i in range(len(grid)):
        rowDict[i], colDict[i] = checkRowColumn(i, grid)
        for j in range(len(grid[i])):
            if grid[i][j] == "#":
                starDict[i*1000 + j] = True
    for i in starDict:
        for j in starDict:
            if (i != j) and (str(j) + ":" + str(i)) not in distDict:
                distDict[str(i) + ":" + str(j)] = calcDistance(i, j, gap, rowDict, colDict)
                total += distDict[str(i) + ":" + str(j)]
    return total
    

print(partBoth(2), partBoth(1000000))