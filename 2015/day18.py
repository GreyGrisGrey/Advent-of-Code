def checkOn(grid, x, y, curr):
    count = []
    count.append(grid[y+1][x-1])
    count.append(grid[y-1][x-1])
    count.append(grid[y-1][x+1])
    count.append(grid[y+1][x+1])
    count.append(grid[y-1][x])
    count.append(grid[y+1][x])
    count.append(grid[y][x-1])
    count.append(grid[y][x+1])
    val = 0
    for i in count:
        if i == "#":
            val += 1
    if val == 3:
        return "#"
    elif val == 2 and curr == "#":
        return "#"
    return "."

f = open("input.txt")
grid = []
line = []
for i in range(102):
    line.append(".")
grid.append(line) 
for i in f:
    line = ["."]
    for j in i:
        line.append(j)
    line.append(".")
    grid.append(line)
line = []
for i in range(102):
    line.append(".")
grid.append(line) 
grid[1][1] = "#"
grid[1][100] = "#"
grid[100][1] = "#"
grid[100][100] = "#"
for i in range(100):
    newGrid = []
    line = []
    for i in range(102):
        line.append(".")
    newGrid.append(line) 
    for j in range(len(grid)-2):
        newLine = ["."]
        for k in range(len(grid[0])-2):
            if (k == 0 or k == 99) and (j == 0 or j == 99):
                newLine.append("#")
            else:
                newLine.append(checkOn(grid, k+1, j+1, grid[j+1][k+1]))
        newLine.append(".")
        newGrid.append(newLine)
    line = []
    for i in range(102):
        line.append(".")
    newGrid.append(line)
    grid = newGrid
count = 0
for i in grid:
    for j in i:
        if j == "#":
            count += 1
print(count)