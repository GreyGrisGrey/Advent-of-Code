def partboth(doneCheck):
    f = open("input.txt", "r")
    grid = []
    for i in f:
        gridLine = []
        for j in i:
            if j != "\n":
                gridLine.append(j)
        grid.append(gridLine)
    heads = []
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "0":
                total += BFS((i, j), grid, [], 0, doneCheck)
    print(total)

def BFS(start, grid, done, curr, doneCheck):
    if start[0] < 0 or start[0] >= len(grid) or start[1] < 0 or start[1] >= len(grid):
        return 0
    if start in done or grid[start[0]][start[1]] == "." or int(grid[start[0]][start[1]]) != curr:
        return 0
    elif grid[start[0]][start[1]] == "9":
        if doneCheck:
            done.append(start)
        return 1
    else:
        total = 0
        total += BFS((start[0]+1, start[1]), grid, done, curr + 1, doneCheck)
        total += BFS((start[0]-1, start[1]), grid, done, curr + 1, doneCheck)
        total += BFS((start[0], start[1]+1), grid, done, curr + 1, doneCheck)
        total += BFS((start[0], start[1]-1), grid, done, curr + 1, doneCheck)
        return total

partboth(True)
partboth(False)